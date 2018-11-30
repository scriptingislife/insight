import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

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
)