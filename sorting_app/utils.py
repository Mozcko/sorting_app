import os

def get_download_path() -> str:
    """Returns the default downloads path for the current operating system."""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def get_unique_filename(filepath: str) -> str:
    """
    If a file already exists at `filepath`, returns a new filepath with a number appended.
    E.g. file.txt -> file (1).txt
    """
    if not os.path.exists(filepath):
        return filepath

    directory, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    
    counter = 1
    new_filepath = os.path.join(directory, f"{name} ({counter}){ext}")
    while os.path.exists(new_filepath):
        counter += 1
        new_filepath = os.path.join(directory, f"{name} ({counter}){ext}")
        
    return new_filepath
