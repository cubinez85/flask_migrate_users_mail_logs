# flask_migrate_users_mail_logs
pip install python-dotenv
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login
pip install email-validator
pip install flask_mail
pip install mysql-connector-python
pip install Flask-Bcrypt
# for change table:
ALTER TABLE post DROP FOREIGN KEY post_ibfk_1;
# PermissionError: [Errno 13] Permission denied: '/var/www/project_flask/logs/project_flask.log'
sudo chown -R cubinez85:cubinez85 logs/
