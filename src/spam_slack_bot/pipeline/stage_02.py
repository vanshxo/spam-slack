from spam_slack_bot.config.configuration import manager
from spam_slack_bot.components.preprocess import process
from spam_slack_bot import logger
import numpy as np
STAGE_NAME="DATA PREPROCESSING STAGE"
class stage02:
    def __init__(self):
        self.spam=[]
        self.ham=[]
    
    def main(self):
        
        conf_manager=manager()
        config=conf_manager.preprocessing_conf()
        st2=process(config=config)
        st2.get_data()
        logger.info(f"Cleaning Spam data")
        for mess in st2.spam_data:
            mess=st2.clean_html(mess)
            mess=st2.remove_headers(mess)
            mess=st2.remove_urls(mess)
            mess=st2.remove_special_characters(mess)
            mess=st2.remove_common_phrases(mess)
            mess=st2.normalize_new_lines(mess)
            mess=mess.lower()
            mess=st2.remove_stopwords(mess)
            if st2.config.lemmatizing:
                mess=st2.lemmatizer(mess)
            else:
                mess=st2.stemming(mess)
            self.spam.append(mess)
        logger.info(f"Cleaning Ham data")
        for mess in st2.ham_data:
            mess=st2.clean_html(mess)
            mess=st2.remove_headers(mess)
            mess=st2.remove_urls(mess)
            mess=st2.remove_special_characters(mess)
            mess=st2.remove_common_phrases(mess)
            mess=st2.normalize_new_lines(mess)
            mess=mess.lower()
            mess=st2.remove_stopwords(mess)
            if st2.config.lemmatizing:
                mess=st2.lemmatizer(mess)
            else:
                mess=st2.stemming(mess)
            self.ham.append(mess)
        self.spam=np.array(self.spam)
        self.ham=np.array(self.ham)
        logger.info(f"saving Spam data to {config.processed_data+'spam.npy'}")
        st2.save_data(self.spam,config.processed_data+'spam.npy')
        logger.info(f"saving ham data to {config.processed_data+'ham.npy'}")
        st2.save_data(self.ham,config.processed_data+'ham.npy')


if __name__=='__main__':
    logger.info(f"{STAGE_NAME} IS STARTED")
    obj=stage02()
    obj.main()
    logger.info(f"{STAGE_NAME} IS COMPLETED")
