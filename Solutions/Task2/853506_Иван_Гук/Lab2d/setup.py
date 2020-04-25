import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Lab2d-package-sovspace',
    version='1.0',
    author_email="vanyaguk135@gmail.com",
    description="Package of second lab tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivanguk10/BSUIR-PYTHON-2020",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)