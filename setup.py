#!/usr/bin/env python

from distutils.core import setup

setup(name="etcd-py",
      version="0.0.6",
      description="Client for Etcd",
      author="Kris Foster",
      author_email="kris.foster@gmail.com",
      maintainer="Kris Foster",
      maintainer_email="kris.foster@gmail.com",
      classifiers=("Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7"),
      packages=['etcd'],
      )
