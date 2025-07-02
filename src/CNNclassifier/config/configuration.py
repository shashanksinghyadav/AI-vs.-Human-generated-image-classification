from CNNclassifier.constants import *
from CNNclassifier.utils.common import read_yaml,create_directories
from CNNclassifier.entity.config_entity import PrepareBaseModelConfig
from CNNclassifier.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):
        self.params=read_yaml(params_filepath)

        self.config=read_yaml(config_filepath)
        
        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
        root_dir=config.root_dir,
        source_url=config.source_url,
        local_data_file=config.local_data_file,
        unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_input_shape=self.params.input_shape,
            params_learning_rate=self.params.learning_rate,
            params_include_top=self.params.include_top,
            params_weights=self.params.weights,
            params_classes=self.params.classes,
            params_pooling=self.params.pooling,
            params_ca=self.params.ca,
            params_name=self.params.name
        )

        return prepare_base_model_config