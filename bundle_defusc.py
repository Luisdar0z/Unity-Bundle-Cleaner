import os

def clean_binary_file(input_path, output_path):
    # The hex pattern we're looking for e.g. (UnityFS....5.x.x.2018.4.36f1.. = 55 6E 69 74 79 46 53 00 00 00 00 06 35 2E 78 2E 78 00 32 30 31 37 2E 34 2E 31 36 66 31 00 00)
    target_hex = bytes.fromhex('55 6E 69 74 79 46 53 00 00 00 00 06 35 2E 78 2E 78 00 32 30 31 37 2E 34 2E 31 36 66 31 00 00')
    
    # Read the binary file
    with open(input_path, 'rb') as file:
        content = file.read()
    
    # Find the position of the target pattern
    position = content.find(target_hex)
    
    if position == -1:
        raise ValueError('Pattern not found in the file')
    
    # Keep only the content from the pattern onwards
    cleaned_content = content[position:]
    
    # Write the cleaned content to the new file
    with open(output_path, 'wb') as file:
        file.write(cleaned_content)
    
    return position  # Return number of bytes removed

def process_all_bundles(directory="."):
    # Specifies the file format to work with
    formatt = '.bundle'
    # Get all files in the directory in the specified format (excluding .bak files)
    bundle_files = [f for f in os.listdir(directory) if f.endswith(formatt) and not f.endswith(f'{formatt}.bak')]
    
    if not bundle_files:
        print(f'No {formatt} files were found in the directory')
        return
    
    # Process each file
    for bundle_file in bundle_files:
        input_path = os.path.join(directory, bundle_file)
        # The cleaned file will have the original name
        cleaned_name = bundle_file
        # The original file will be renamed with .bak
        backup_name = f'{bundle_file}.bak'
        
        try:
            # First create the backup of the original file
            os.rename(input_path, os.path.join(directory, backup_name))
            
            # Now process the file
            bytes_removed = clean_binary_file(
                os.path.join(directory, backup_name),
                os.path.join(directory, cleaned_name)
            )
            
            print(f"File: {bundle_file}")
            print(f"  - Bytes removed: {bytes_removed}")
            print(f"  - Original file renamed to: {backup_name}")
            print(f"  - Clean file saved as: {cleaned_name}")
            print("-" * 50)
        except Exception as e:
            print(f"Error processing {bundle_file}: {str(e)}")
            print("-" * 50)

if __name__ == "__main__":
    #  Process all .formmatt files in current directory
    process_all_bundles()