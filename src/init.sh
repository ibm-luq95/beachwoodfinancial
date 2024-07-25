#!/usr/bin/bash
#export VIRTUAL_ENV=/beachwoodfinancial_development/venv
#export PATH="$VIRTUAL_ENV/bin:$PATH"
#source /beachwoodfinancial_development/venv/bin/activate 

echo "Waiting for server volume..."
cd /beachwoodfinancial_development/src



# setup frontend
echo "###############################################################"
echo "Waiting for frontend to setup..."
cd frontend
npm set progress true
pnpm install
pnpm run build
echo "###############################################################"

echo "###############################################################"
echo "Waiting for enter src folder ..."
cd ..
echo "###############################################################"

echo "###############################################################"
echo "Waiting for db to be migrated..."

python3 manage.py makemigrations -v 1

python3 manage.py migrate -v 1

echo "Waiting for reports migration to be ready..."
python3 manage.py migrate reports 0001_create_client_jobs_db_view -v 1

echo "Create createsuperuser"
python3 manage.py createsuperuser -v 1 --noinput --email=$DJANGO_SUPERUSER_EMAIL --password=$DJANGO_SUPERUSER_PASSWORD --user_type=$DJANGO_SUPERUSER_USER_TYPE --user_genre=$DJANGO_SUPERUSER_USER_GENRE


echo "###############################################################"

echo "###############################################################"
echo "Executing custom commands ..."
echo "Waiting for init and setup django site..."
python3 manage.py set_site -i


echo "Waiting for init beachwood site settings..."
python3 manage.py init_site_settings -i -v 2 -s 127.0.0.1:8000


echo "Waiting for init beachwood cache data..."
python3 manage.py init_cache_data -i -s 127.0.0.1:8000


echo "Waiting for create users groups..."
python3 manage.py create_groups
echo "###############################################################"


echo "###############################################################"
echo "Waiting for collect static..."
python3 manage.py collectstatic --noinput
echo "###############################################################"
# python3 manage.py createsuperuser --noinput

#gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
echo "###############################################################"
echo "Waiting for runserver..."
python3 manage.py runserver 0.0.0.0:8000
echo "###############################################################"
