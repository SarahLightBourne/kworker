from pathlib import Path
from ..utilities import get_env_var

TG_TOKEN = get_env_var('TG_TOKEN')
CATEGORIES = Path(get_env_var('CATEGORIES_PATH', 'config/categories.json'))
