from CNNclassifier import logger
from CNNclassifier.pipeline.level_01_data_ingestion import DataIngestionTrainingPipeline
LEVEL_NAME="Data Ingestion Level"
if __name__=='main':
    try:
        logger.info(f"-------------LEVEL {LEVEL_NAME} started---------")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        
        logger.info(f"-------------LEVEL {LEVEL_NAME} completed---------")
    except Exception as e:
        logger.exception(e)
        raise e