import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="lab_2_zhevniak",
    version="1.0",
    author="Katerina Zhevniak",
    author_email="starlet7@tut.by",
    description="Full implementation of the second lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Linux",
    ],
    python_requires='>=3.6',
)