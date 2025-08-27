import os
import re
import sys


def rename_files(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    if os.path.isfile(path) and is_movie(path):
        new_name = jellyfy_filename(path)
        new_file_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_file_path)
    else:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and is_movie(file_path):
                new_filename = jellyfy_filename(filename)
                new_file_path = os.path.join(path, new_filename)
                os.rename(file_path, new_file_path)


def is_movie(path: str) -> bool:
    _root, extension = os.path.splitext(path)
    return extension.lower() in ['.mkv', '.mp4', '.mov', '.avi', '.wmv', '.webm', '.flv']


def remove_chars(text: str, bad_chars: str, space_chars: str) -> str:
    text = ''.join(' ' if c in space_chars else c for c in text) # replace with space
    return ''.join(c for c in text if c not in bad_chars) # full delete from text


def jellyfy_filename(filename: str) -> str:
    name = os.path.basename(filename)
    file_extension = os.path.splitext(filename)[1]
    year = find_leftmost_4_digits(filename)
    name = name.split(year)[0]
    name = remove_chars(name.strip(), bad_chars='()[]', space_chars='._')

    if year is None:
        return filename
    return f'{name} ({year}){file_extension}'


def find_leftmost_4_digits(text):
    match = re.search(r'\d{4}', text)
    if match:
        return match.group()


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        rename_files(path)


if __name__ == '__main__':
    main()
