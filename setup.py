#!/usr/bin/env python

from distutils.core import setup


def read(filename):
    return open(filename, 'rb').read().decode('utf-8')

setup(name="etcd-py",
      version="0.0.6",
      description="Client for Etcd",
      #long_description=read("README.rst"),
      author="Kris Foster",
      author_email="kris.foster@gmail.com",
      maintainer="Kris Foster",
      maintainer_email="kris.foster@gmail.com",
      url="https://github.com/transitorykris/etcd-py",
      download_url="https://github.com/transitorykris/etcd-py/archive/master.zip",
      classifiers=("Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7"),
      #license=read("LICENSE"),
      packages=['etcd'],
      )
