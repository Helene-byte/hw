import os, stat
import fnmatch
import argparse

def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file,pattern):
                yield os.path.join(root, file)

def display_result(file_paths):
    """Displays founded file paths and file's permissions."""

    for file_path in file_paths:
        print(file_path, stat.filemode(os.stat(file_path).st_mode))
    # print('Found ' + count_sum(file_paths) + ' file(s).')

# def count_sum(file_paths):
#     return str(sum(1 for _ in file_paths))
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-p")
    args = parser.parse_args()
    display_result(finder(args.path, args.p))

if __name__ == '__main__':
    main()
