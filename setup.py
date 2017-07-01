from setuptools import setup, find_packages
from codecs import open
from os import path

from spammy.version import VERSION
__version__ = VERSION

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='spammy',
    version=__version__,
    description='spammy: Spam filtering at your service',
    long_description=long_description,
    url='https://github.com/tasdikrahman/spammy',
    download_url='https://github.com/tasdikrahman/spammy/tarball/' + __version__,
    license='GPLv3',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: Implementation :: CPython',
      'Programming Language :: Python :: Implementation :: PyPy',
      "Topic :: Text Processing :: Linguistic",
    ],
    keywords='spam filtering, spam, ham, machine learning, artificial intelligence',
    packages=find_packages(exclude=['docs', 'tests*', 'examples']),
    include_package_data=True,
    author='Tasdik Rahman',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='prodicus@outlook.com'
)
