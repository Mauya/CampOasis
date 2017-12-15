# CampOasis Project

## Overview
This is a simple camping web application mainly for group campers such as youth groups, University student, sports teams,
schools clubs. The main addition is the facility to offer camping gear for hire at attractive costs. This reduces the
bulk young people have to take with them and allows more time for adventure. The Project name is CampOasis and backend is
sqlite3. This section helps you to get up and start your own project straight away. The project is developed with
python in pycharm.

## Tools for the App
* Django framework with SQLite3 database
* MySQL configuration
* Python 2.7 with Jetbrains Pycharm
* Package manager is pip
* VirtualEnv and virtualenvwrapper
* Version control using Github
* deployment by Heroku

### Setting up
* Install python 2.7
* Install pycharm
* Create new project
* In project interpreter select Django
* create virtual environment for CampersApp

### Prerequisites
* When using Pycharm you can start project using the command line
* Alternatively use the other option: select file --> create new Project and add Virtual environment from settings tab
* The project container/directory is CampersApp

'''django-admin startproject CampersApp'''

#### Working environment
When the project is created it contains:
* manage.py file - to manage development, runserver and make-migrations to database
* __init__.py indicates that this is a python package
* setting.py is used to configure the project
* urls.py is yhe basis to relate urls with the views
* wsgi.py is mainly used to configure Django deployment
* CampOasis folder also contains all the apps created, templates, static files and other files related to the project
* After this start the development server at Http://127.0.0.1:8000/
* In browser it will confirm that it worked, if not check that all processes have been done

#### Setting separate requirements and setting.py
Deemed good approach in Django project
* Requirements files - useful to control the version of packages used in the project. This is important when working
with others and also makes it easy when deploying
* to see packages installed:
```$ pip freeze ```
* The requirement folder include files for each environment:
    - base.txt (contains only the Django version)
    - dev.txt (for development)
    - staging.txt
    - production.txt (for deployment)
    - testing.txt (for testing and contains the selenium version used)

* Settings Files - used to set different configuration for each environment.
* the settings folder include:
    - __init__.py - indicates that this is a python package
    - base.py includes all settings that common in all environments. The other setting files inherit from base.by
    - dev.py (for development locally set DEBUG =True)
    - staging.py (to run staging version on the production, set DEBUG = False)
    - Production.py (for the production environment, set DEBUG = False)
    - testing.py  (for testing environment set DEBUG = True)

* Django SECRET_ kEY and Protection
    - Keep SECRET_KEY from version control (put in in separate file and put it in gitignore or include it inside
    the virtual environment). After setting this make sure to remove SECRET_KEY from base.py.

* for more in-depth settings refer to Django documentation

### Adding Apps
* apps can be added or removed from the project
    ``` python manage.py startapp accounts```

* Add app to INSTALLED_APPS IN base.py
    ``` INSTALLED_APPS = (
        ....,
        'accounts',
        )```

* Things to always remember especially if you are a beginner
    - Don't forget to migrate constantly ``` python manage.py migrate app```
    - always add work to github some files and database sqlite3 are included in gitignore (or any version of your choice)
    - Runserver to check that your code is running ok ``` python manage.py runserver```

### Adding Static Files
* the first thing is to check base.py in the INSTALLED_APP to see if ```django.contrib.staticfiles``` is include.
also include the STATIC_URL
* static files for this project include one project static folder which include
    - css
    - img

### Templates
* project comes with a templates folder. This contains all templates categorised by the original app.
* Ensure to update base.py and edit the TEMPLATES section as required
* the templates folder contain base.html as the main file from which other html files inherit the main outline.

### Testing
This part was a challenge for me but a few testing were included

### Debugging
* Django has an easy way of making you deal with issues by highlighting them and pointing out what you could do.
I still have new challenges to face especially with migrations and had to delete and start afresh.
* Most of the challenges initially came from using the namespace in urls. Later I realised i haven't read it enough
so I resorted  to ```name```  as in the LMS tutorials.
* some of the bug or errors were due to importErrors from either forms, models or views.
* In some cases it was improper import of modules in the settings.
* The vast majority and easy one were ```TypeErrors```

### Acknowledgements
* Mentor Yoni Lavi for helpful tips on debugging and structuring of the project
* The admin Team for dealing with my indecisions
* A few Student on slack for helping solve some of the issues with debugging
* My family for putting up with my late nights and stress.

### References
This project was a massive undertaking and a lot of other established work was used  or modified to create my own project.
* Django documentation - I used this mainly to understand concepts and setting up with latest versions and
comparing with previous.
    This is an [Django Documentation](https://docs.djangoproject.com/en/2.0/topics/migrations/) date 23/11/2017.
    - documentation was also used for reference on many other things minor and major throughout the project phase.
* [Django-Tutorial](http://www.marinamele.com/taskbuster-django-tutorial/). This was instrumental in setting up
my requirement, settings, templates and static files.
* [Booking Structure](https://github.com/bitlabstudio/django-booking/tree/master/booking). Booking app was a
major component of my project and this site helped me create a reasonable booking app. It has notes that explain
why each section is necessary. However, it was very complex and had its challenges to understand
* [Building shop](https://www.youtube.com/watch?v=jZ3DhppbUnM&t=14s). This video from packtpub.com was instrumental
and easy to follow in creating my own shop. I did find also that they explained concepts really well,
such as what are sessions, context processors and how we use them.
* [Code institute Tutorial Notes](http://lms.codeinstitute.net/course-status/). From stream 0-3 has been a source of
insight and understanding and sometimes components of code.
* Lastly, I cannot overlook video watch to learn and understand django and used to structure my own project.
    [Django Tutorial-thenewboston](https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)
    [Max Goodridge](https://www.youtube.com/watch?v=Fc2O3_2kax8&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj).
    Introduction to Django Web Framework for Python

#### Contributions
This is a Code Institute stream 3 Project and has one sole contributor
Sandra Kadungure


