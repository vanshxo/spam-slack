from spam_slack_bot.entity.config import processing
from spam_slack_bot.utils.common import *
import numpy as np
from bs4 import BeautifulSoup
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


class process:
    def __init__(self,config:processing):
        self.config=config
        self.spam_data=[]
        self.ham_data=[]
        self.spam_data=np.array(self.spam_data)
        self.ham_data=np.array(self.ham_data)
        nltk.download('stopwords')
        nltk.download('wordnet')
        create_dir([self.config.processed_data])

    def get_data(self):
        data_path=self.config.npy_data
        files=os.listdir(data_path)
        for file in files:
            if(file.startswith('spam')):
                data=np.load(data_path+f"{file}")
                
                self.spam_data=np.append(self.spam_data,data)
                print(self.spam_data.shape)
            else:
                data=np.load(data_path+f"{file}")
                self.ham_data=np.append(self.ham_data,data)
        
    
    def clean_html(self,email:list):
        soup=BeautifulSoup(email,"html.parser")
        return soup.get_text()
    
    def remove_headers(self,email:list):
        parts=email.split("\n\n",1)
        if(len(parts)>1):
            return parts[1]
        else:
            return email
        
    def remove_urls(self,email:list):
        url_patterns=r'http[s]?://\S+|www\.\S+'
        new=re.sub(url_patterns,'',email)
        return new
    
    def remove_special_characters(self,email_content):
    # Regular expression pattern to keep only letters and spaces
        cleaned_email = re.sub(r'[^A-Za-z\s]', '', email_content)
        return cleaned_email
    
    def normalize_new_lines(self,email_content):
    # Replace new lines with a space
        cleaned_email = email_content.replace('\n', ' ')
        # Also normalize spaces after replacing new lines
        cleaned_email = re.sub(r'\s+', ' ', cleaned_email)  # Replace multiple spaces with a single space
        return cleaned_email.strip()  # Strip leading and trailing spaces
    
    def remove_common_phrases(self,email_content):
    # List of common unsubscribe-related phrases (this can be expanded)
        common_phrases = [
            r'you are receiving this email',
            r'double optin',
            r'subscribe',
            r'unsubscribe',
            r'remove yourself',
            r'click here to remove',
            r'mailing list'
        ]

        # Join the phrases into a single regular expression pattern
        pattern = '|'.join(common_phrases)

        # Remove the phrases
        cleaned_email = re.sub(pattern, '', email_content, flags=re.IGNORECASE)

        return cleaned_email
    
    
    def remove_stopwords(self,mail):
        stop_words=set(stopwords.words('english'))
        words=mail.split()
        cleaned=[word for word in words if word  not in stop_words]
        return ' '.join(cleaned)
    
    def stemming(self,mail):
        stemmer=PorterStemmer()
        words=mail.split()
        stemmed=[stemmer.stem(word) for word in words]
        return ' '.join(stemmed)
    
    
    def lemmatizer(self,mail):
        lemma=WordNetLemmatizer()
        words=mail.split()
        lemmatized=[lemma.lemmatize(word) for word in words]
        return ' '.join(lemmatized)
    
    def save_data(self,data,save_path:Path):
        np.save(save_path,data)




    




