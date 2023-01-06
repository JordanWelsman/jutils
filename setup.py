# Module imports
from setuptools import setup

# Arguments
git_name = "jutils"
pypi_name = "juts"
version = "0.0.1"
python_version = ">=3.10"

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
    'pipelining/*',
    'sorters/*',
    'timers/*',
    'utilities'
]

# Run setup function
setup(
    name='juts',
    version=version,
    description='A Python package of useful tools and utilities.',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jordan Welsman',
    author_email='welsman@lbl.gov',
    url='https://pypi.org/project/jt/',
    download_url='https://github.com/JordanWelsman/jutils/tags',
    package_data={'jutils': jutils_package_data},
    python_requires=python_version,
    # jutils package information
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
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
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    keywords='python, averages, calculators, converters, cryptography, formatting, language, logic, pipelining, sorters, timers, utilities'
)