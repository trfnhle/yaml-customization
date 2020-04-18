# yaml-customization
Some helpful tool to working with YAML

# Install
- `git clone https://github.com/l4zyf9x/yaml-customization.git` and `cd yaml-customization`
- `pip insall -e .`
- Then `cd examples/yaml2bash` to run example
- Run `bash execute.sh`


# Frequently question

## Import error with yaml
- If import CLoader raise `AttributeError: module 'yaml' has no attribute 'CLoader'` then following step to fix:
  - Clone repo from github `https://github.com/yaml/pyyaml.git`
  - Follow instruction from repository [pyyaml](https://github.com/yaml/pyyaml) Or you could follow next step
  - `cd pyyaml`
  - Make sure you install gcc `sudo apt-get install gcc`
  - Finally `python setup.py --with-libyaml install`
