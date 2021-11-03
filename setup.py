"""
This setup file is here in order to install and use the package on local machines

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="actristools",
    version="0.0.1",
    author="KStanley",
    author_email="stanley@iau.uni-frankfurt.de",
    description="tools for processing ACTRIS VOC data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kstanley2/actristools.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0',
        'numpy',
        'matplotlib',
        'scipy',
        'glob',
        'datetime'
    ]
)
