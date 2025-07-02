from CNNclassifier.components.prepare_base_model import PrepareBaseModel
from CNNclassifier.config.configuration import ConfigurationManager
from CNNclassifier import logger

from CNNclassifier.entity.config_entity import PrepareBaseModelConfig
LEVEL_NAME="Prepare Base Model"
class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
if __name__=='__main__':
    try:
        logger.info("level 2 started")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info("level 2 completed")
    except Exception as e:
        logger.exception(e)
        raise e
