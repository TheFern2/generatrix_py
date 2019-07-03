from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Generatrix',
    version='1.0.0',
    author='Fernando A. Balandran',
    author_email='fredz0003@gmail.com',
    description='Generates repo contents markdown',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kodaman2/generatrix_py',
    entry_points={
        'console_scripts': [
            'gtrix = generatrix:main',
        ],
    }
)