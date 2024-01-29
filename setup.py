import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='qlog',  
    version='0.0.1',
    author="Chris Dunne",
    author_email="contact@chrisdunne.net",
    description="A package for querying log files for evidence of compromise, by passing a CVE as a parameter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisdunne/qlog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['qlog=src.qlog:cli'],
    },
    install_requires  = ["os"],
 )