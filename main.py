from CNNclassifier import logger
from CNNclassifier.pipeline.level_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNclassifier.pipeline.level_01_data_ingestion import DataIngestionTrainingPipeline
LEVEL_NAME="Data Ingestion Level"
try:
        logger.info(f"-------------LEVEL {LEVEL_NAME} started---------")
        

        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        
        logger.info(f"-------------LEVEL {LEVEL_NAME} completed---------")
except Exception as e:
        logger.exception(e)
        raise e
LEVEL_NAME="Prepare Base Model Level"

try:
        logger.info(f"-------------LEVEL {LEVEL_NAME} started---------")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        
        logger.info(f"-------------LEVEL {LEVEL_NAME} completed---------")
except Exception as e:
        logger.exception(e)
        raise e
