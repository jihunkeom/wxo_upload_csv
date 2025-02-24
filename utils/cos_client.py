from ibm_botocore.client import Config
import ibm_boto3
import ssl
from dotenv import load_dotenv
import os

load_dotenv()


def get_cos_client():
    load_dotenv()
    ssl._create_default_https_context = ssl._create_unverified_context

    COS_ENDPOINT = os.getenv("COS_ENDPOINT", None)
    COS_API_KEY_ID = os.getenv("COS_API_KEY_ID", None)
    # Your service instance CRN
    COS_INSTANCE_CRN = os.getenv("COS_INSTANCE_CRN", None)
    
    cos_client = ibm_boto3.client(
        "s3",
        ibm_api_key_id=COS_API_KEY_ID,
        ibm_service_instance_id=COS_INSTANCE_CRN,
        config=Config(signature_version="oauth"),
        endpoint_url=COS_ENDPOINT,
    )
    return cos_client