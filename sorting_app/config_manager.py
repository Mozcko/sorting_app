import os
import sys
import json
from typing import Dict, List

def get_base_path():
    """Returns the base directory, works for both dev script and PyInstaller executable."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable, so config.json should be next to the executable
        return os.path.dirname(sys.executable)
    else:
        # Running as a python script, config.json is in the project root
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = os.path.join(get_base_path(), "config.json")

def load_config() -> dict:
    """Loads the configuration from config.json."""
    if not os.path.exists(CONFIG_FILE):
        return {"categories": {}, "default_folder": "Other"}
    
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def get_category_for_extension(ext: str, config: dict) -> str:
    """Returns the target folder category for a given file extension."""
    ext = ext.lower()
    for category, extensions in config.get("categories", {}).items():
        if ext in extensions:
            return category
            
    return config.get("default_folder", "Other")

def get_categories(config: dict) -> List[str]:
    """Returns a list of all defined folder categories."""
    categories = list(config.get("categories", {}).keys())
    default = config.get("default_folder", "Other")
    if default not in categories:
        categories.append(default)
    return categories
