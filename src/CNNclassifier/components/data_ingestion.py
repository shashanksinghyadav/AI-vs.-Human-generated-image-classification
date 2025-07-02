import os
import urllib.request as req
import requests
import zipfile
import io
import zipfile
from CNNclassifier import logger
from CNNclassifier.utils.common import get_size
from pathlib import Path
import re
from CNNclassifier.entity.config_entity import DataIngestionConfig

def extract_filename(content_disposition):
    match = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^\";\n]+)"?', content_disposition)
    return match.group(1) if match else None
def get_confirm_token(response):
    for k, v in response.cookies.items():
        if k.startswith('download_warning'):
            return v
    return None
def download_from_gdrive_url(url, output_path):
    response = requests.get(url, stream=True)

    # Try to extract filename from headers if output_path not provided
    if output_path is None:
        content_disp = response.headers.get("Content-Disposition", "")
        output_path = extract_filename(content_disp) or "downloaded_file"

    # Save file
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

    print(f"Downloaded to: {output_path}")
    return output_path, response.headers
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=download_from_gdrive_url(self.config.source_url,self.config.local_data_file)
            logger.info(f"{filename} downloaded! with following info:\n {headers}")
            print(filename)
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)