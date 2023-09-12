#!/usr/bin/zsh

CWD=$(pwd)
PARENT="$(dirname $CWD)/src"
echo $PARENT
cd $PARENT
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py set_site -i
python3 manage.py init_site_settings -i -v 2 -s 127.0.0.1:8000
python3 manage.py init_cache_data -i -s 127.0.0.1:8000
python3 manage.py create_groups
python3 manage.py createsuperuser
