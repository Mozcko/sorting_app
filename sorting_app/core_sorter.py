import os
import time
import shutil
import logging
from alive_progress import alive_bar

from . import config_manager
from .utils import get_unique_filename

def validate_folders(target_folder: str, config: dict):
    """Ensures that all category folders exist inside the target folder."""
    categories = config_manager.get_categories(config)
    print('Validating folders...')
    
    with alive_bar(len(categories)) as bar:
        for folder in categories:
            path = os.path.join(target_folder, folder)
            if not os.path.exists(path):
                os.mkdir(path)
            time.sleep(0.05)
            bar()

def sort_files(target_folder: str, config: dict):
    """Sorts all files in the target folder into their respective category folders."""
    categories = config_manager.get_categories(config)
    
    # Get a list of files to sort (excluding the category directories themselves)
    files_to_sort = []
    for filename in os.listdir(target_folder):
        filepath = os.path.join(target_folder, filename)
        if os.path.isfile(filepath) and filename not in categories:
            files_to_sort.append(filename)
            
    if not files_to_sort:
        print("No files to sort.")
        return

    print("Sorting files...")
    with alive_bar(len(files_to_sort)) as bar:
        for filename in files_to_sort:
            old_filepath = os.path.join(target_folder, filename)
            _, extension = os.path.splitext(filename)
            
            category = config_manager.get_category_for_extension(extension, config)
            category_path = os.path.join(target_folder, category)
            
            # Destination path handling collisions
            new_filepath = os.path.join(category_path, filename)
            new_filepath = get_unique_filename(new_filepath)
            
            try:
                shutil.move(old_filepath, new_filepath)
            except Exception as e:
                logging.error(f"Error moving {filename}: {e}")
                
            time.sleep(0.05)
            bar()
