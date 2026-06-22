# Sorting App

A modular program designed to automatically organize your Downloads folder (or any folder) by sorting files into categorized subfolders based on their extensions. It also includes an optional feature to compress images in-place to save disk space.

## Features
- **Automatic Sorting:** Organizes files into categories like `Images`, `Programming`, `Documents`, `Media`, etc.
- **Image Compression:** Optionally compresses images (reducing quality/size) before sorting them.
- **Customizable:** Easily change folder names or file extension mappings without touching code via `config.json`.
- **Cross-Platform:** Automatically detects the default Downloads folder on both Windows and UNIX-like systems.
- **Collision Handling:** Safely renames files instead of overwriting them if a file with the same name already exists in the destination folder.

---

## 🚀 Quick Start (For Regular Users)

You do not need Python installed to run this application!

1. Go to the **[Releases](../../releases)** page on this repository.
2. Download the `.zip` file for your operating system (Windows, MacOS, or Linux).
3. Extract the `.zip` file.
4. **Run it:**
   - **Windows:** Double-click `SortingApp.exe`
   - **MacOS/Linux:** Run the `SortingApp` executable
5. The interactive menu will open in your terminal!

**Customizing Sorting Rules:**
Inside the folder you extracted, you will see a `config.json` file sitting next to the executable. You can open this file in any text editor (like Notepad) to add your own custom file extensions and folder categories!

---

## 💻 Developer Guide (For Contributors)

If you want to run the source code directly or contribute to the project:

### Installation
1. Clone this repository to your local machine.
2. Ensure you have Python 3.10+ installed.
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage
Run the main script to start the interactive menu:
```bash
python main.py
```

### Building the Executable Locally
If you want to build the standalone executable yourself using PyInstaller:
```bash
pyinstaller --name SortingApp --onefile main.py
```
*The compiled executable will be placed in the `dist/` folder.*

### Project Structure
```text
sorting_app/
├── .github/                     # GitHub Actions workflows and Issue/PR templates
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