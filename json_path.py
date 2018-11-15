import json


def write_to_config(config_path):
    with open(config_path, 'w', encoding='utf-8') as fd:
        json.dump({'file_paths': [r'e:\temp\t.hdf5', r'e:\профиль\t.hdf5', r'e:\профиль\тест.hdf5']},
                  fd,
                  ensure_ascii=False)

def read_from_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as fd:
        json_d = json.load(fd)
        return json_d['file_paths']




if __name__ == '__main__':
    data = {'file_paths': [r'e:\temp\README.txt', r'e:\профиль\t.hdf5', r'e:\профиль\тест.hdf5']}



    # import os
    # # write_to_config('config.txt')
    # path = read_from_config('config.txt')[1]
    # print(
    #     os.path.abspath('config.txt')
    # )
    # print(path)


