import os
import time
from alive_progress import alive_bar
from PIL import Image

downloads_folder=""

def main():
    global downloads_folder
    downloads_folder=get_download_path()

    print(downloads_folder)
    menu()

def get_download_path():
    #Returns the default downloads path for Linux or windows
    
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def validate_folders():
    folders=['Images', 'Programming', 'Pages', 'Documents', 'Media', 'Executables', 'Archives', 'Spreadsheets', 'Other']
    print('Validating folders')
    with alive_bar(len(folders)) as bar:
        for folder in folders:
            if os.path.exists(os.path.join(downloads_folder, folder)):
                time.sleep(0.1)
                bar()
            else:
                path=os.path.join(downloads_folder,folder)
                os.mkdir(path)
                time.sleep(0.1)
                bar()

def print_menu():
    
    os.system("clear")

    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Sort Downloads folder")
    print("2. Sort and Compress images")
    print("3. Change folder to sort")
    print("4. Exit")
    print(67 * "-")
    

def menu():
    running = True
    while running:
        print_menu()
        op = input('Choose an option [1-4]: ')
        
        if op == '1':
            validate_folders()
            sort()
        elif op == '2':
            validate_folders()
            sort(True)
        elif op == '3':
            global downloads_folder
            downloads_folder=input('Input the new folder to sort: ')
        elif op == '4':
            print("Good bye")
            running = False
        else:
            print('Invalid option, choose a valid option [1-4]')
            time.sleep(1)

def sort(compress=False):
    # this is just for the looks
    # it counts how many images and files are in total
    images=0
    files=0
    for filename in os.listdir(downloads_folder):
        name, extension=os.path.splitext(downloads_folder + filename)
        # images extensions bmp, gif, ico, jpeg, jpg, png, raw, tif, tiff.
        if extension in ['.jpg', '.png', '.jpeg', '.webp', '.bmp', '.gif', '.ico', '.raw', '.tif', '.tiff']:
            images+=1
            files+=1
        else:
            files+=1

    if compress:
        # it selects only the images and compress them
        # and prints an alive bar to check the progress
        print("Compressing images ")
        with alive_bar(images) as bar:
            for filename in os.listdir(downloads_folder):
                name, extension=os.path.splitext(os.path.join(downloads_folder, filename))

                if extension in ['.jpg', '.png', '.jpeg', '.webp', '.bmp', '.gif', '.ico', '.raw', '.tif', '.tiff']:
                    picture = Image.open(os.path.join(downloads_folder, filename))
                    picture.save(os.path.join(downloads_folder, filename), optimize=True, quality=60)
                    time.sleep(0.1)
                    bar()

    # It sorts all the files inside the Downloads folder depending on the type 
    # and prints an alive bar to check the progress of the process
    print("Sorting files")
    with alive_bar(files) as bar:
        for filename in os.listdir(downloads_folder):
            name, extension=os.path.splitext(os.path.join(downloads_folder, filename))

            if filename in ['Images', 'Programming', 'Pages', 'Documents', 'Media', 'Executables', 'Archives', 'Spreadsheets', 'Other']:
                bar()
                continue
            
            # Moves the images to the Images folder
            if extension in ['.jpg', '.png', '.jpeg', '.webp', '.bmp', '.gif', '.ico', '.raw', '.tif', '.tiff']:
                images_folder = os.path.join(downloads_folder, 'Images')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(images_folder, filename))

            # Programming Files
            elif extension in ['.c', '.cpp', '.cs', '.java', '.js', '.json', '.py', '.sql', '.swift', '.vb', '.asp',
                              '.aspx', '.css', '.htm', '.html', '.jsp', '.php', '.xml']:
                programming_folder = os.path.join(downloads_folder, 'Programming')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(programming_folder, filename))

            # Pages folder
            elif extension in ['.afdesign', '.ai', '.cad', '.cdr', '.drw', '.dwg', '.eps', '.odg', '.svg', '.vsdx',
                             '.afpub', '.indd', '.pdf', '.pdfxml', '.pmd', '.pub', '.qxp']:
                pages_folder = os.path.join(downloads_folder, 'Pages')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(pages_folder, filename))

            # Documents folder
            elif extension in ['.doc', '.docx', '.odt', '.pages', '.rtf', '.txt', '.wpd', '.wps', '.ppt', '.pptx', '.odp']:
                documents_folder = os.path.join(downloads_folder, 'Documents')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(documents_folder, filename))

            # Media files
            elif extension in ['.aif', '.mov', '.mp3', '.mp4', '.mpg', '.wav', '.wma', '.wmv']:
                media_folder = os.path.join(downloads_folder, 'Media')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(media_folder, filename))

            # Executables files
            elif extension in ['.app', '.bat', '.bin', '.cmd', '.com', '.exe', '.vbs', '.x86', '.apk', '.jar', '.app',
                              '.appimage', '.run', '.pyc', '.vbe', '.jse']:
                executables_folder = os.path.join(downloads_folder, 'Executables')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(executables_folder, filename))

            # Archives files
            elif extension in ['.7z', '.rar', '.tar', '.tar.gz', '.zip']:
                archives_folder = os.path.join(downloads_folder, 'Archives')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(archives_folder,filename))

            # spreadsheet folder
            elif extension in ['.csv' , '.numbers', '.ods', '.xls', '.xlsx']:
                spreadsheets_folder = os.path.join(downloads_folder, 'Spreadsheets')
                os.rename(os.path.join(downloads_folder,filename), os.path.join(spreadsheets_folder,filename))
    
            # Other folder
            else:
                others_folder = os.path.join(downloads_folder,'Other')
                os.rename(os.path.join(downloads_folder, filename), os.path.join(others_folder, filename))

            time.sleep(0.05)
            bar()


if __name__ == "__main__":
    main()
