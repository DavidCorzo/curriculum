import yaml


def read_yaml_and_writing_to_about():
    with open("info.yml", 'r') as stream:
        try:
            master = yaml.safe_load(stream)
            error = False
        except yaml.YAMLError:
            error = True
        stream.close()

    return master, error
