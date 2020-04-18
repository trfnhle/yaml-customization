"""Setup NLP as service libarary."""

import os
import pip
import sys

from distutils.version import LooseVersion
from setuptools import find_packages
from setuptools import setup

if LooseVersion(sys.version) < LooseVersion("3.6"):
    raise RuntimeError(
        "NLP as service requires python >= 3.6, "
        "but your Python version is {}".format(sys.version)
    )

if LooseVersion(pip.__version__) < LooseVersion("19"):
    raise RuntimeError(
        "pip>=19.0.0 is required, but your pip version is {}. "
        "Try again after \"pip install -U pip\"".format(pip.__version__)
    )

requirements = {
    "install": [
        "setuptools>=38.5.1",
        "pyyaml>=5.3.1"
    ],
    "setup": [
        "pytest-runner",
    ],
    "test": [
        "pytest>=3.3.0",
        "hacking>=1.1.0",
        "flake8>=3.7.8",
        "flake8-docstrings>=1.3.1",
    ]
}

entry_points = {
    'console_scripts': [
        'yaml2bash = yaml_helper.yaml2bash:main'
    ]
}

install_requires = requirements["install"]
setup_requires = requirements["setup"]
tests_require = requirements["test"]
extras_require = {k: v for k, v in requirements.items()
                  if k not in ["install", "setup"]}

dirname = os.path.dirname(__file__)
setup(name="yamlhelper",
      version="0.0.0",
      url="https://github.com/l4zyf9x/yaml-customization",
      author="Trinh Le Quang",
      author_email="trinhle.cse@gmail.com",
      description="Python YAML helper",
      long_description=open(os.path.join(dirname, "README.md"),
                            encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      license="MIT License",
      packages=find_packages(include=["yaml_helper*"]),
      install_requires=install_requires,
      setup_requires=setup_requires,
      tests_require=tests_require,
      extras_require=extras_require,
      entry_points=entry_points,
      classifiers=[
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Intended Audience :: Science/Research",
          "Operating System :: POSIX :: Linux",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ],)
