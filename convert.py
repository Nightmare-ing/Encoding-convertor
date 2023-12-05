import chardet

def check_file_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        print(f"File encoding: {encoding} with confidence: {confidence}")

check_file_encoding("../test.txt")
