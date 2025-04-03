# 📁 File Copy and Rename Tool

A simple Python script that copies files from a source folder to a destination folder while renaming them with a sequential numbering pattern.

## 🔍 Overview

This utility script helps you create renamed copies of your files with a consistent naming pattern (`prefix_number.extension`). Rather than modifying the original files, it creates copies in a separate destination folder, preserving your original files.

## ✨ Features

- 📋 Copies all files from a source folder to a destination folder
- 🔄 Automatically renames files during copying with sequential numbering
- 🏷️ Uses a customizable prefix for the new filenames
- 📂 Creates the destination folder if it doesn't exist
- 🔢 Maintains the original file extensions

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses only built-in `os` and `shutil` modules)

## 📋 Usage

1. Save the script as `copy_rename_files.py`

2. Modify the script with your folder paths and desired naming format:
   ```python
   folder_path = "/path/to/your/folder"  # Replace with your source folder path
   output_folder_path = "/path/to/your/output_folder"  # Replace with your destination folder path
   new_name_format = "fire"  # Change "fire" to your desired prefix
   ```

3. Run the script:
   ```bash
   python copy_rename_files.py
   ```


## ⚙️ Key Parameters

- `folder_path`: Source directory containing the files to copy and rename
- `output_folder_path`: Destination directory where renamed copies will be saved
- `new_name_format`: The prefix text to use in the new filenames

## 📋 Example

If your source folder contains:
- document.docx
- photo.jpg
- notes.txt

After running the script with `new_name_format="fire"`, the destination folder will contain:
- fire_1.docx
- fire_2.jpg
- fire_3.txt

## ⚠️ Important Notes

- The script preserves the original files
- The script processes all files in the source folder (not just specific file types)
- Files are numbered based on their order in the directory listing
- The script skips directories and only processes files
- Uses `shutil.copy2()` which preserves file metadata where possible

## 🚀 Customization Ideas

- Add file filtering to only process certain file types
- Implement error handling for failed copies
- Add a logging system for tracking operations
- Create a command-line interface for easier usage

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
