import argparse

CSV_IN_FILE_PATH = 'DataCollector01.csv'
CSV_OUT_FILE_PATH = 'data.csv'

def machine_name(source:str):
    first_double_slash_idx = source.find('\\\\')
    slash_idx = source.find('\\', first_double_slash_idx + 3)
    return source[first_double_slash_idx:slash_idx+1]

def convert():
    with open(CSV_IN_FILE_PATH) as file:
        header = file.readline()
        str_to_remove = machine_name(header)
        with open(CSV_OUT_FILE_PATH, 'w') as wfile:
            wfile.writelines(header.replace(str_to_remove, ''))
            lines = file.readlines()
            wfile.writelines(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("-f", "--filename", type=str)

    args = parser.parse_args()
    if args.filename:
        CSV_IN_FILE_PATH = args.filename
    if args.output:
        CSV_OUT_FILE_PATH = args.output  

    convert()
