from spam_slack_bot.config.configuration import manager
from spam_slack_bot.components.prediction import prediction_stage

class stage04:
    def __init__(self):
        pass

    def main(self):
        config_manager=manager()
        config=config_manager.prediction_conf()
        st4=prediction_stage(config=config)
        st4.load_model()
        self.obj=st4

    def pred(self,mess:str):
        return self.obj.prediction(mess)
    

if __name__=='__main__':
    obj=stage04()
    obj.main()
    obj.pred("hello bro")