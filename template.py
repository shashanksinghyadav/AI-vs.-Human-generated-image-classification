import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
project_name="CNNclassifier"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/__init__.py",

    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "templates/index.html",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
   
]
for filepath in list_of_files:
    filepath= Path(filepath)# linux path to windows path conversion
    filedir,filename=os.path.split(filepath)# path directory and filename tuple

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating director-{filedir} for the file-{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file-{filename}")
    else:
        logging.info(f"{filename} already exists.")