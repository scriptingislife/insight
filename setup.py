import setuptools
from setuptools.command.install import install
import os

CONF_CONTENT = """---
censys_uid: 
censys_secret: 
shodan_key: 
"""

with open("README.md", "r") as fh:
    long_description = fh.read()

class PreInstallCommand(install):
    def run(self):
        conf_file = os.path.join(os.path.expanduser("~"), ".insight")
        if not os.path.isfile(conf_file):
            print("Creating configuration file at {}".format(conf_file))
            with open(conf_file, 'w') as f:
                f.write(CONF_CONTENT)
        else:
            print("Configuration file .insight exists. Skipping creation...")
        install.run(self)

setuptools.setup(
    name="insight",
    version="0.0.1",
    author="Nathaniel Beckstead",
    author_email="nathaniel@scriptingis.life",
    description="Aids in profiling an IP or domain name by searching online services.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/becksteadn/insight",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={'install':PreInstallCommand},
    entry_points = {'console_scripts': ['insight=insight.insight:main']},
)