web: gunicorn supply_management.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn supply_management.wsgi