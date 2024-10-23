from spam_slack_bot import logger
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class data_ingestion:
    root_dir:Path
    raw_data:Path
    source_url :str
    zip_data:Path
    unzipped:Path
    untarred:Path
    numpytext:Path

@dataclass(frozen=True)
class processing:
    root_dir:Path
    npy_data:Path
    processed_data:Path
    lemmatizing:bool


@dataclass(frozen=True)
class training:
    root_dir:Path
    training_data_spam:Path
    training_data_ham:Path
    test_size:float
    random_state:int
    max_features:int
    stop_words:str
    max_df:float
    min_df:float
    kernel:str
    C:float
    class_weight:str




