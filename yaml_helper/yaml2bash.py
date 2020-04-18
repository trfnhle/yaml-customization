
import argparse
from yaml_helper import yaml_configure  # This line to initialize yaml consctructor parser
import yaml

def main():
    parser = argparse.ArgumentParser(description='Parse yaml to bash variable')
    parser.add_argument('--yaml', type=str, required=True, help='Path yaml file')
    args = parser.parse_args()
    config = yaml.load(open(args.yaml), Loader=yaml.CLoader)
    # yaml_configure.print_yaml(config)
    text = yaml.dump(config['bash'],
                     indent=2,
                     allow_unicode=True,
                     Dumper=yaml.CDumper,
                     default_flow_style=False)
    print(text)

if __name__ == "__main__":
    main()
    # yaml_configure.print_json(config)
