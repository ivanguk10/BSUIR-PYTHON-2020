from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='lab2',
    version='1.2',
    packages=find_packages(),
    test_suite="test_files.tests",
    author="Andrey Karpyza",
    author_email="andrey.karpyza.steam@gmail.com",
    url="*url*",
    description="lab2-files",
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.rst'), encoding="Utf-8").read(),
    entry_points={
        'console_scripts': [
            'vector = lab2_setupable.script_files:vector_exmpl',
            'json = lab2_setupable.script_files:json_exmpl',
            'decorator = lab2_setupable.script_files:decorator_exmpl',
            'singleton = lab2_setupable.script_files:singleton_exmpl',
            'sorting = lab2_setupable.script_files:sort_exmpl',
       ]
    }
)
