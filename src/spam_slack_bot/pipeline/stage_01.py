from spam_slack_bot.components.data_ingestion import data_ingest
from spam_slack_bot.config.configuration import manager
from spam_slack_bot import logger
STAGE_NAME='DATA INGESTION STAGE'
class stage01:
    def __init__(self):
        pass
    def main(self):
        conf_manager=manager()
        data_conf=conf_manager.data_ingest_conf()
        st1=data_ingest(data_conf)
        st1.data_download()
        st1.unzipping()
        st1.untarring()
        st1.saveAsNPY()


if __name__=='__main__':
    logger.info(f">>>{STAGE_NAME} is started<<<")
    obj=stage01()
    obj.main()
    logger.info(f">>>{STAGE_NAME} is completed<<<")

