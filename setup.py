from setuptools import setup, find_packages

VERSION="0.1.1dev1"

setup(
    name="aaew_couch",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'CouchDB',
        ],
    extras_require={
        'progress_bar': ['tqdm'],
        },

)


