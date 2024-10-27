from spam_slack_bot.constants import *
from spam_slack_bot.utils.common import *
from spam_slack_bot.entity.config import data_ingestion,processing,training,predict

class manager:
    def __init__(self):
        self.config=readYaml(CONFIG_FILE_PATH)
        self.params=readYaml(PARAMS_FILE_PATH)
        create_dir([self.config.artifacts_root])

    def data_ingest_conf(self)->data_ingestion:
        self.data_config=self.config.stage_01
        return data_ingestion(root_dir=self.data_config.root_dir,
                              raw_data=self.data_config.raw_data,
                              source_url=self.data_config.source_url,
                              zip_data=self.data_config.zip_data,
                              unzipped=self.data_config.unzipped,
                              untarred=self.data_config.untarred,
                              numpytext=self.data_config.numpytext
                              )
    def preprocessing_conf(self)->processing:
        self.preprocessing_config=self.config.stage_02
        return processing(root_dir=self.preprocessing_config.root_dir,
                          npy_data=self.preprocessing_config.npy_data,
                          processed_data=self.preprocessing_config.processed_data,
                          lemmatizing=self.params.lemmatizing
                          )
    
    def training_conf(self)->training:
        self.training_config=self.config.stage_03
        return training(root_dir=self.training_config.root_dir,
                        training_data_spam=self.training_config.training_data_spam,
                        training_data_ham=self.training_config.training_data_ham,
                        test_size=self.params.test_size,
                        random_state=self.params.random_state,
                        stop_words=self.params.stop_words,
                        max_df=self.params.max_df,
                        min_df=self.params.min_df,
                        kernel=self.params.kernel,
                        C=self.params.C,
                        class_weight=self.params.class_weight,
                        max_features=self.params.max_features)
    
    def prediction_conf(self)->predict:
        self.predict_config=self.config.stage_04
        return predict(root_dir=self.predict_config.root_dir,
                       model_path=self.predict_config.model_path,
                       tfidf_vectorizer=self.predict_config.tfidf_vectorizer
        )




