from distutils.core import setup

NAME = 'Insight'
DESCRIPTION = open('README.md').read()
URL = 'https://github.com/becksteadn/iprep'
EMAIL = 'nathaniel@scriptingis.life'
VERSION = None

REQUIRED = ['requests', 'argparse', 'PTable']

setup(
    name=NAME,
    version=VERSION,
    packages=['insight'],
    long_description=DESCRIPTION,
)