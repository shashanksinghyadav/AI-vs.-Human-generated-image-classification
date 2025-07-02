from CNNclassifier.config.configuration import ConfigurationManager
from CNNclassifier.components.data_ingestion import DataIngestion
from CNNclassifier import logger
LEVEL_NAME="Data Ingestion"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
if __name__=='main':
    try:
        logger.info(f"-------------LEVEL {LEVEL_NAME} started---------")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"-------------LEVEL {LEVEL_NAME} completed---------")
    except Exception as e:
        logger.exception(e)
        raise e