import random
import string
from utils.cos_curd_repository import upload_bytes_to_cos
import os
from dotenv import load_dotenv
import base64
import imghdr
import magic

load_dotenv()
bucket_name = os.getenv("BUCKET_NAME", None)


def get_file_type_from_base64str(base64_string):

    # Remove Base64 prefix if present (e.g., "data:image/png;base64,")
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]

    # Decode Base64 string to bytes
    file_bytes = base64.b64decode(base64_string)

    # Use imghdr to detect image type
    image_type = imghdr.what(None, file_bytes)

    # If imghdr detects webp, override it with manual checks
    if image_type == "webp":
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(file_bytes)

        # Force PNG/JPG correction
        if "jpeg" in mime_type:
            return "image/jpg"
        else:
            return "image/png"

    # Use magic as a final check
    mime = magic.Magic(mime=True)
    return mime.from_buffer(file_bytes)


def save_file(base64_string: str, original_file_name: str):

    try:
        # Remove Base64 prefix if present (e.g., "data:image/png;base64,")
        if "," in base64_string:
            base64_string = base64_string.split(",")[1]

        # Decode the Base64 string
        file_bytes = base64.b64decode(base64_string)

        filetype = get_file_type_from_base64str(base64_string)
        file_extenstion = filetype.split("/")[1]
        print(file_extenstion)
        if file_extenstion == 'plain':
            file_extenstion = 'txt'
        elif file_extenstion.endswith("wordprocessingml.document"):
            file_extenstion = "docx"
        elif file_extenstion.endswith("spreadsheetml.sheet"):
            file_extenstion = "xlsx"
        elif file_extenstion.endswith("presentationml.presentation"):
            file_extenstion = "pptx"
        filename = f"{generate_code()}.{file_extenstion}"
        upload_bytes_to_cos(file_bytes, bucket_name, original_file_name, filetype)
        return original_file_name
    except Exception as ex:
        raise ex


def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))