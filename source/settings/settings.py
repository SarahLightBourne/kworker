from pathlib import Path
from ..utilities import get_env_var

TG_TOKEN = get_env_var('TG_TOKEN')
CREATOR_ID = int(get_env_var('CREATOR_ID'))
CREATOR_NICKNAME = get_env_var('CREATOR_NICKNAME')

CHOSEN_ONES = get_env_var('CHOSEN_ONES_PATH', 'config/chosen_ones.json')
CATEGORIES = Path(get_env_var('CATEGORIES_PATH', 'config/categories.json'))
LOG = Path(get_env_var('LOG_PATH', 'logs/'))
