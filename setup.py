import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    "numpy",
    "Pillow"
]

setup(
	name='pMTRLe',
	version='0.0.1',
	description='PyGame Reinforcement Learning Environment',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
	url='https://github.com/jupilogy/PyGame-Learning-Environment',
	author='Jupy, forked from Norman Tasfi',
	author_email='jupiterian.is@gmail.com',
	keywords='',
	license="MIT",
	packages=find_packages(),
        include_package_data=False,
        zip_safe=False,
        install_requires=install_requires
)
