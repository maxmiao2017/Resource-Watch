# Always prefer setuptools over distutils
from setuptools import setup, find_packages
setup(name="rw_api_tools",
     install_requires=['pandas', 'requests'],
     packages=find_packages('src'),  # include all packages under src
    package_dir={'':'src'},# tell distutils packages are under src
      version="1.0.7"
     )
