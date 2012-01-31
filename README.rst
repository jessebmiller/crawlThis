crawlThis
=========

crawlThis was built on top of Twango and the below is true for crawlThis...
Take a look at the Twango project here. https://github.com/dagray/twango


Twango uses virtualenv and pip to facilitate easy and reliable setup of new projects
Some conventions used by twango that might not be obvious to those used to django:

To begin, Run 

  > source bootstrap.sh

This will install the virtual environment needed to run the crawlThis test site and activate the environment.

to activate the environment after the initial bootstrap run

  > source env/bin/activate

to leave the environment run

  > deactivate

once the environment is active you may run the test server locally with
  
  > python manage.py runserver

manage.py is in src/

check http://localhost:8000 in your browser and you should see the crawlThis test site. Its just a list of links that each to to a list of links. Exciting.