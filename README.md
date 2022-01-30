****THIS IS NOT THE FINAL READ ME. FINAL ONE WILL BE UPLOADED WITHIN 1 WEEK FROM (24-01-2022)****

This is a fully functional College Attendance And AICTE points Trackers aka CAAT.
Lecturers can use it to add,modify and delete attendance and AICTE points and activities for their classes. 

Following is list of major tools that were utilized to develop the app:

	Backend
		Django
		PostgreSQL
		Pgadmin4

	Frontend
		HTML
		CSS
		Javascript
		
App Previews:




Setup
In root directory create a virtual Python environment for backend, (using virtualenv) named "env" here:
	
	virtualenv env


Activate virtual environment:

	Windows
		\env\Scripts\activate
	Linux/Mac
		source env/bin/activate

Install all backend dependencies from requirements.txt:

pip install -r requirements.txt

All app dependencies must be installed now.

NOTE

Configure the backend/dukaan/settings.py to connect your database to the app before running the app.






Now migrate all the tables to your db. In root dir:

	python manage.py makemigrations
	python manage.py migrate

All required tables should exist in db now.
NOTE - Populate the table either using db or the admin panel.


Run the App

	python manage.py runserver
That's it.
