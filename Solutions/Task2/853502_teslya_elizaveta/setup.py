from setuptools import setup, find_packages


setup(name='benninoda',
      version='1.0',
      url='https://github.com/benninoda/Python-LW',
      author='Lizaveta Teslya',
      author_email='lizabenninoda@outlook.com',
      description='Lab 2, python',
      long_description=open('readme.md', 'r').read(),
      packages=find_packages(),
      python_requires='>=3.6',
      test_suite='pytest', install_requires=['pytest'])
