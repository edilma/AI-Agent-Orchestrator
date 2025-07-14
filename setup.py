#fill template to create a setup.py file for a Python package
from setuptools import setup, find_packages

setup(
    name="blog_agent_framework",
    version="0.1.0",
    author="Edilma Riano",
    description="An AI agent framework for generating and reviewing blog posts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)