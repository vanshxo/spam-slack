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

