from spam_slack_bot.entity.config import predict
from spam_slack_bot import logger
import joblib
class prediction_stage:
    def __init__(self,config:predict):
        self.config=config

    def load_model(self):
        self.model=joblib.load(self.config.model_path)
        self.tfidf_vectorizer=joblib.load(self.config.tfidf_vectorizer)
    
    def prediction(self,message:str):
        text=self.tfidf_vectorizer.transform([message])
        y=self.model.predict(text)
        ans=None
        if y==0:
            ans='Ham'
        else :ans='Spam'
        logger.info(f"prediction is {ans}")
        return y

        