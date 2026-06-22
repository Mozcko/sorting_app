import time
import logging

from . import config_manager
from . import core_sorter
from . import compressor
from . import utils

def print_menu():
    utils.clear_screen()
    print(30 * "-", "MENU", 30 * "-")
    print("1. Sort Downloads folder")
    print("2. Sort and Compress images")
    print("3. Change folder to sort")
    print("4. Exit")
    print(67 * "-")

def main():
    logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
    
    config = config_manager.load_config()
    target_folder = utils.get_download_path()
    
    print(f"Current target folder: {target_folder}")
    
    running = True
    while running:
        print_menu()
        print(f"Target folder: {target_folder}\n")
        
        op = input('Choose an option [1-4]: ')

        if op == '1':
            core_sorter.validate_folders(target_folder, config)
            core_sorter.sort_files(target_folder, config)
            input("\nDone! Press Enter to continue...")
        elif op == '2':
            core_sorter.validate_folders(target_folder, config)
            compressor.compress_images_in_folder(target_folder)
            core_sorter.sort_files(target_folder, config)
            input("\nDone! Press Enter to continue...")
        elif op == '3':
            new_folder = input('Input the new folder to sort: ')
            import os
            if os.path.exists(new_folder) and os.path.isdir(new_folder):
                target_folder = new_folder
            else:
                print("Invalid folder path.")
                time.sleep(1)
        elif op == '4':
            print("Good bye")
            running = False
        else:
            print('Invalid option, choose a valid option [1-4]')
            time.sleep(1)

if __name__ == "__main__":
    main()
