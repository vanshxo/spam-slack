from spam_slack_bot.entity.config import data_ingestion
from spam_slack_bot import logger
from gdown import download
import numpy as np
import zipfile
import tarfile
from spam_slack_bot.utils.common import *
class data_ingest:
    def __init__(self,config:data_ingestion):
        
        self.config=config
        create_dir([self.config.root_dir])
    
    def data_download(self):
        url=self.config.source_url

        down_url='https://drive.google.com/uc?id='
        file_id=url.split('/')[-2]
        final_url=down_url+file_id
        create_dir([self.config.raw_data])
        logger.info(f"starting data download from gdrive {self.config.raw_data}")
        download(final_url,self.config.zip_data)
        logger.info(f"the data file is downloaded at {self.config.raw_data}")

    def unzipping(self):
        with zipfile.ZipFile(self.config.zip_data,'r') as file:
            file.extractall(self.config.unzipped)

    def untarring(self):
        data_path=self.config.unzipped
        files=os.listdir(data_path)
        files.sort()
        files=files[:-1]
        for file in files:
            path=os.path.join(data_path,file)
            with tarfile.open(path,'r') as f:
                f.extractall(self.config.untarred)
        
    def saveAsNPY(self):
        file_path=self.config.untarred
        files=os.listdir(file_path)
        save=self.config.numpytext
        create_dir([save])
        
        
        vec=[]
        for file in files:

            f =os.listdir(os.path.join(file_path,file))
            
            emails=[]
            for mess in f:
                
                with open(os.path.join(file_path,file,mess),'r',encoding='latin-1') as text:
                    emails.append(text.read())
            np.save((save+f'{file}.npy'),np.array(emails))




    


        
        