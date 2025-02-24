from pydantic import BaseModel
from typing import List

class FileData(BaseModel):
    filedata: str
    original_file_name: str
    
    
class MultipleFileData(BaseModel):
    files: List[FileData]
    
