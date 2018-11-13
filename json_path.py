import json
import yaml

def write_to_config(config_path):
    with open(config_path, 'w', encoding='utf-8') as fd:
        json.dump({'file_paths': [r'e:\temp\t.hdf5', r'e:\профиль\t.hdf5', r'e:\профиль\тест.hdf5']},
                  fd,
                  ensure_ascii=False)

def read_from_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as fd:
        json_d = json.load(fd)
        return json_d['file_paths']

def read_file(path, mode='r', encoding='utf8'):
    with open(path, mode) as fd:
        for line in fd:
            print(line, end='')


if __name__ == '__main__':
    data = {'file_paths': [r'e:\temp\README.txt', r'e:\профиль\t.hdf5', r'e:\профиль\тест.hdf5']}

    # Write YAML file
    # with open('data.yaml', 'w', encoding='utf8') as outfile:
    #     yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
    #     # Read YAML file
    with open("data.yaml", 'r', encoding='utf-8') as stream:
        data_loaded = yaml.load(stream)
        read_file(data_loaded['file_paths'][0], 'r', )

    # import os
    # # write_to_config('config.txt')
    # path = read_from_config('config.txt')[1]
    # print(
    #     os.path.abspath('config.txt')
    # )
    # print(path)


