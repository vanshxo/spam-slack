from spam_slack_bot.components.training import training_stage
from spam_slack_bot.config.configuration import manager

from spam_slack_bot import logger

STAGE_NAME='MODEL TRAINING STAGE'

class stage03:
    def __init__(self):
        pass

    def main(self):
        conf_manager=manager()
        config=conf_manager.training_conf()
        st3=training_stage(config)
        st3.fitting()

if __name__=='__main__':
    obj=stage03()
    obj.main()
