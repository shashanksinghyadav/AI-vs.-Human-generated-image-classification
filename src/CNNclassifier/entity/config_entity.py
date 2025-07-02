from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_input_shape: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    params_pooling: str
    params_name: str
    params_ca: str