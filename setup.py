from setuptools import find_packages, setup

setup(
    name="restaurants_retrieval",
    packages=find_packages(include=["restaurants_retrieval"]),
    version="0.1.0",
    description="Python library for retrieving of the restaurants by a postcode of an area",
    author="Andriy Sydorenko",
    install_requires=[
        "requests",
        "python-slugify"
    ],
)
