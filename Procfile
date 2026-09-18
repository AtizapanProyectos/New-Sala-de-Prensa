web: sh -c "python prensa/manage.py collectstatic --noinput && gunicorn --chdir prensa prensa.wsgi --bind 0.0.0.0:$PORT --log-file -"
