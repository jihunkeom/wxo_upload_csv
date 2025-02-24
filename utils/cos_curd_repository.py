from utils.cos_client import get_cos_client


def upload_bytes_to_cos(
    data_bytes: bytes, 
    bucket_name: str,
    file_key: str,
    content_type: str = "application/octet-stream",
):
    try:
        cos_client = get_cos_client()
        
        cos_client.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=data_bytes,
            ContentType=content_type,
        )
        
        print(f"successfully uploaded {file_key} to {bucket_name}")
        
    except Exception as e:
        print(f"Failed to upload {file_key}: {str(e)}")
        raise
    
    
    