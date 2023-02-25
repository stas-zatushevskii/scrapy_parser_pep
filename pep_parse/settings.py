import pathlib
from datetime import datetime

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

FEEDS = {
    'results/pep_%(time)s.csv': {
        # Формат файла.
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

PATTERN = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = pathlib.Path(__file__).parents[1]
RESULTS = 'results'
FILE_NAME = (f"status_summary_" + 
                f"{datetime.now().strftime(PATTERN)}.csv")

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
