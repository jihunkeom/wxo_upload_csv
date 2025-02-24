from utils import file_writer

async def process_filestream(filedetails, original_file_name):
    response = file_writer.save_file(
        base64_string=filedetails,
        original_file_name=original_file_name,
    )
    
    return response