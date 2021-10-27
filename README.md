"# CRUD-Django-Fidel" 

#Set and Activate Virtual environment
 1. python3 -m venv venv
 
 2. source djangoenv/bin/activate  

#Pip install dependancies
pip install -r requirements.txt

#Run development server
python3 manage.py runserver
python3 manage.py migrate

#Create super user
python3 manage.py createsuperuser


#Create branch for your changes

#Save any new changes to requirements
pip freeze > requirements.txt
