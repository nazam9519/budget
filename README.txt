Budget App
Nabil, Ralph

OS Notes:
Linux WSL(Dev) Ubuntu 20.04.01 LTS
RasPI(Prod) Linux raspi 5.4.51-v71 armv71

Webserver Notes:
apache2 configuration is in /etc/apache2/sites-enabled
routes are defined in /var/www/flaskapp
logs are defined in /var/log/apache2 (root access needed)

Installation Notes:
Ansible will be used for most installation procedures, the .yml should be self documenting. Currently missing Apache2 config but it installs postgres and python fine.

To test locally python venv will be used. 
This requires the installation of a few pieces:
postgres (listens on port 5432)
pip3 packages:
	flask(see /ansible/roles/flask) or just run pip3 install flask ansible configuration will be needed.. if using wsl then all will have to be run manually(as far as i know)
	sqlalchemy for ORM(pip3 install flask-sqlalchemy)-	
		psycopg2 needs to be installed for data connection to postgres to properly work
		pip3 install psycopg2-binary==2.8.6 <-- must specify binary version 


python -m venv
