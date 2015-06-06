#!/bin/bash
 
NAME="clw"                                  # Name of the application
DJANGODIR=/projects/clw.com.ua/www             # Django project directory
SOCKFILE=/var/run/gunicorn.sock
USER=prog                                        # the user to run as
                                    # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=clw.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=clw.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
  --timeout=90
   --graceful-timeout=10
