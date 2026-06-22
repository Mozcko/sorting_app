# Sorting App

A modular Python program designed to automatically organize your Downloads folder (or any folder) by sorting files into categorized subfolders based on their extensions. It also includes an optional feature to compress images in-place to save disk space.

## Features
- **Automatic Sorting:** Organizes files into categories like `Images`, `Programming`, `Documents`, `Media`, etc.
- **Image Compression:** Optionally compresses images (reducing quality/size) before sorting them.
- **Customizable:** Easily change folder names or file extension mappings without touching the Python code via `config.json`.
- **Cross-Platform:** Automatically detects the default Downloads folder on both Windows and UNIX-like systems.
- **Collision Handling:** Safely renames files instead of overwriting them if a file with the same name already exists in the destination folder.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the main script to start the interactive menu:

```bash
python main.py
```

From the menu, you can:
1. **Sort Downloads folder:** Quickly sort all files based on the rules in `config.json`.
2. **Sort and Compress images:** First compresses all compatible images, then sorts the folder.
3. **Change folder to sort:** Specify a custom directory to sort instead of the default Downloads folder.

## Configuration (`config.json`)

You can fully customize how files are sorted by editing the `config.json` file. 

Example configuration:
```json
{
  "categories": {
    "Images": [".jpg", ".png", ".jpeg", ".webp"],
    "Documents": [".txt", ".pdf", ".docx"]
  },
  "default_folder": "Other"
}
```
* **`categories`**: Maps folder names to a list of file extensions.
* **`default_folder`**: The fallback folder for any file extensions not explicitly listed in the categories.

## Project Structure
```
sorting_app/
├── sorting_app/                 # Main package directory
│   ├── cli.py                   # Handles the user interface and menu
│   ├── core_sorter.py           # Logic for categorizing and moving files
│   ├── compressor.py            # Image compression functions
│   ├── config_manager.py        # Loads user configurations
│   └── utils.py                 # OS path helpers and file utilities
├── tests/                       # Unit tests
├── config.json                  # Default sorting rules & extensions
├── main.py                      # Entry point script
└── requirements.txt             # Project dependencies
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU](https://choosealicense.com/licenses/gpl-3.0/#)