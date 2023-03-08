from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="elasticsearchquerygenerator",
    version="1.1.0",
    description="""
    Create Complex Elastic Search Query in Seconds 
    Please see documentation for more details
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/elasticsearchquerygenerator.git",
    author="Badr Alboushy",
    author_email="badralboushy.scholar@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["elasticsearchquerygenerator"],
    include_package_data=True,
    install_requires=[]
)