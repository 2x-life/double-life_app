from setuptools import setup, find_packages

setup(
    name="doublelife",
    packages=find_packages(),
    version=0.1,
    install_requires=[],
    author="Adrien Gougeon",
    entry_points={
    'console_scripts': [
        'doublelife = doublelife.main:main',
        ]
    },
)
