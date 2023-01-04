# Module imports
from setuptools import setup

# Arguments
version = "0.0.0"
python_version = "3.10.0"

# Long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# jutils package data
jutils_package_data = [
    'averages/*',
    'calculators/*',
    'converters/*',
    'cryptography/*',
    'formatting/*',
    'language/*',
    'logic/*',
    'sorters/*',
    'timers/*',
    'utilities'
]

# Run setup function
setup(
    name='jutils',
    version=version,
    description='A Python package of useful tools and utilities.',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jordan Welsman',
    author_email='jordan.welsman@outlook.com',
    url='https://pypi.org/project/jutils/',
    download_url='https://github.com/JordanWelsman/jutils/tags',
    package_data={'jutils': jutils_package_data},
    python_requires=python_version,
    # jutils package information
    classifiers={
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3'
    },
    keywords='python, averages, calculators, converters, cryptography, formatting, language, logic, sorters, timers, utilities'
)