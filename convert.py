import chardet
import argparse
import os

def check_file_encoding(file_path):
    encoding = ''
    confidence = 0.0
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
    print(f"File encoding: {encoding} with confidence: {confidence}")
    return encoding, confidence


def parse_args():
    parser = argparse.ArgumentParser(description=
                                     'Convert file encoding to UTF-8')
    parser.add_argument('root_dir', 
                        type=str, 
                        help='Root dir to all the files you want to convert')
    return parser.parse_args()


if __name__ == '__main__':
    # Parse args and confirm working dir
    args = parse_args()
    print(f"Working on root dir: {args.root_dir}, continue? (y/n)")
    user_input = input()
    if user_input == 'y':
        print("Start converting...")
    else:
        print("Abort")
        exit(0)

    # iterate through all files in the root dir recursively and convert them 
    # to UTF-8
    for dirpath, dirs, files in os.walk(args.root_dir):
        for file in files:
            file_path = os.path.join(dirpath, file)
            # judge the extension of the file
            file_extension = os.path.splitext(file_path)[1]
            if file_extension not in ['.v', '.txt', '.csv', '.py', '.xdc']:
                print(f"File {file_path} is not a text file, skip...")
                continue
            encoding, confidence = check_file_encoding(file_path)
            if encoding == 'utf-8':
                print(f"File {file_path} is already UTF-8, skip...")
                continue
            if encoding != 'utf-8' and confidence > 0.8:
                with open(file_path, 'r', encoding=encoding) as file:
                    raw_data = file.read()
                with open(file_path, 'w', encoding='UTF-8') as file:
                    file.write(raw_data)
                print(f"File {file_path} converted to UTF-8")

