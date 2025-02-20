import os
import re
import sys

def rename_files(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    if os.path.isfile(path):
        new_name = jellyfy_filename(path)
        new_file_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_file_path)
    else:
        for i, filename in enumerate(os.listdir(path)):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                new_filename = jellyfy_filename(filename)
                new_file_path = os.path.join(path, new_filename)
                os.rename(file_path, new_file_path)

def jellyfy_filename(filename: str) -> str:
    name = os.path.basename(filename)
    file_extension = os.path.splitext(filename)[1]
    year = find_leftmost_4_digits(filename)
    name = name.split(year)[0]
    name = name.replace(".",' ')
    name = name.replace(')','')
    name = name.replace('(','')
    name = name.replace('_',' ')
    name = name.strip()
    if year is None:
        return filename
    return f"{name} ({year}){file_extension}"

def find_leftmost_4_digits(text):
    match = re.search(r'\d{4}', text)
    if match:
        return match.group()
    return None

def main():
    if (len(sys.argv)) == 2:
        path = sys.argv[1]
        if os.path.isfile(path):
            rename_files(path)
        else:
            rename_files(path)

if __name__ == "__main__":
    main()