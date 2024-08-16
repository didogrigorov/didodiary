#!/usr/bin/env bash
# Download and install SQLite 3.41.0 (or the version you need)
wget https://www.sqlite.org/2024/sqlite-autoconf-3460100.tar.gz
tar -xvf sqlite-autoconf-3460100.tar.gz
cd sqlite-autoconf-3460100

./configure --prefix=/usr/local
make
make install
cd ..
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
