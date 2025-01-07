# Unity Binary Cleaner

Unity Binary Cleaner is a tool designed to clean binary files from Unity-based games. These files often contain unnecessary data before specifying the Unity version, making them unreadable by tools like [AssetStudio](https://github.com/aelurum/AssetStudio). This script identifies and removes the unwanted content, allowing the cleaned files to be processed correctly.

## Features
- Automatically detects the hexadecimal pattern indicating the Unity version within binary files.
- Removes all content preceding the detected pattern, cleaning the file.
- Creates a backup of the original file before making any modifications.
- Configurable to work with various file formats, adapting to different extensions or extensionless files.
- Processes all matching files in a specified directory.

## How It Works
1. Place the script in the same directory as the binary files you want to clean.
2. Update the file format in the script if needed (default: `.bundle`).
3. Run the script to process all files in the directory.
4. Original files are renamed with a `.bak` extension, while the cleaned files retain their original names.

## Example Output
File: example.bundle

Bytes removed: 512

Original file renamed to: example.bundle.bak

Clean file saved as: example.bundle

## Requirements
- Python 3.x

## Usage
Edit the script and specify the unity version and format that corresponds to the file to be cleaned, see the example images below.

Run the script in the directory containing the files to clean. It will automatically process all matching files and create backups of the originals.

### Examples
Original .ys file with space or garbage (red square) before unity version definition (green line), which cannot be opened with AssetStudio.

(I know I know, I know you can modify the file manually with tools like HxD, but when you have more than 15000 files this becomes tedious, that's why I made this basic script, to process them in batch.)
![image](https://github.com/user-attachments/assets/6212027c-7e0b-4bc8-bb0e-cf88542c8bdd)

Then we need to specify the unity version hex in line 5 and the format file in line 28
![image](https://github.com/user-attachments/assets/72c688c3-1673-4eb4-9435-9add457f6fb5)

After executing the script we will have two files for each processed file, a .bak file that will contain the original file and a file in the specified format that will have no previous information before the unity version and should be able to run in AssetStudio.
![image](https://github.com/user-attachments/assets/b546d4ad-a108-46e7-adf2-c41cace51a2a)







### Default File Format
By default, the script processes `.bundle` files. To process other formats:
- Edit the `formatt` variable in the `process_all_bundles()` function.

### Notes
- Files with `.bak` extensions will be ignored to prevent accidental reprocessing of backups.
- The script is safe to use but make additional backups if necessary.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Disclaimer
This tool is provided "as is" without warranty of any kind. Use it at your own risk.
