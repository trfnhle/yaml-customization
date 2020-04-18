import yaml
import os

# Define custom tag handler


def join_path(loader, node):
    seq = loader.construct_sequence(node)
    str_seq = [str(i) for i in seq]
    return os.path.join(*str_seq)


def join(loader, node):
    seq = loader.construct_sequence(node)
    str_seq = [str(i) for i in seq]
    return ''.join(str_seq)


# Set yaml config
yaml.add_constructor('!Join', join)
yaml.add_constructor('!JoinPath', join_path)
yaml.CLoader.add_constructor('!Join', join)
yaml.CLoader.add_constructor('!JoinPath', join_path)


