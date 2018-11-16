import yaml


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