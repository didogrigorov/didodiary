#!/bin/bash

# Download and install SQLite 3.41.0 (or the version you need)
wget https://www.sqlite.org/2023/sqlite-autoconf-3460100.tar.gz
tar -xvf sqlite-autoconf-3460100.tar.gz
cd sqlite-autoconf-3460100

./configure --prefix=/usr/local
make
make install
