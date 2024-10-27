from spam_slack_bot.entity.config import training
import numpy as np
from spam_slack_bot import logger
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from spam_slack_bot.utils.common import *
import joblib
class training_stage:
    def __init__(self,config:training):
        self.config=config
        create_dir([self.config.root_dir])
        
    
    def get_data(self):
        logger.info("getting data for training")
        self.spam=np.load(self.config.training_data_spam)
        self.ham=np.load(self.config.training_data_ham)
        y_spam=np.ones(self.spam.shape)
        y_ham=np.zeros(self.ham.shape)
        X=np.append(self.spam,self.ham)
        y=np.append(y_spam,y_ham)
        return X,y
    
    def vectorize(self):
        X,y=self.get_data()
        print(f"shape of X:{X.shape} y:{y.shape}")
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=self.config.test_size,stratify=y,random_state=self.config.random_state)
        self.tfidf_vectorizer = TfidfVectorizer(
        max_features=self.config.max_features,        # Increase feature space to cover more word variety
        ngram_range=(1,3),       # Capture unigrams, bigrams, and trigrams for context
        stop_words=self.config.stop_words,     # Remove common English stop words
        max_df=self.config.max_df,               # Ignore terms that appear in more than 90% of the documents (too common)
        min_df=self.config.min_df  
                                   # Ignore terms that appear in fewer than 2 documents (too rare)
)
        X_train_tfidf = self.tfidf_vectorizer.fit_transform(X_train)
        X_test_tfidf = self.tfidf_vectorizer.transform(X_test)
        return X_train_tfidf,X_test_tfidf,y_train,y_test
    
    def fitting(self):
        logger.info(">>>Model training has started <<<")
        svm_model=SVC(kernel=self.config.kernel,C=self.config.C,class_weight=self.config.class_weight)
        X_train_tfidf,X_test_tfidf,y_train,y_test=self.vectorize()
        svm_model.fit(X_train_tfidf,y_train)
        y_pred = svm_model.predict(X_test_tfidf)
        print(classification_report(y_test, y_pred, target_names=['ham', 'spam']))  

        joblib.dump(svm_model,self.config.root_dir+'svm_model.joblib')
        joblib.dump(self.tfidf_vectorizer,self.config.root_dir+'tfidf_vectorizer.joblib')
        logger.info("Trained model is saved!!!")








        