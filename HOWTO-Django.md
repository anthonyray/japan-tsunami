# Projet Japan Tsunami


## 1. Django Server
In this tutorial we're using Ubuntu 14 as OS.

---
### 1.1 Installation
First install python environment used for Django framework:
```
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
```
Then install django:
```
sudo pip install Django
```
---
### 1.2 Create project
Go in the folder where you want to put your code, __/home__ is better than /usr/www. Then type:
```
django-admin.py startproject mysite
```
---
### 1.3 Setup Database
(TODO)

---
### 1.4 Model
* ####Create a model

For each app you want to create for your project you need a model. The model folder can be putted anywhere in the python path, but in our case, as we don't need several app, so we will put in our project folder next to manage.py:
```
python manage.py startapp japan_map
```
Here is the content of our folder:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    japan_map/
        __init__.py
        admin.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```
* ##### Activate model

Edit the mysite/settings.py file again, and change the INSTALLED_APPS setting to include the string 'polls'. So it’ll look like this:
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'japan_map'
)
```
When you make changes __in__ your model, to notify django we made some changes, run:
 ```
 python manage.py makemigrations japan_map```

---
### 1.5 Create view
Set up the views.py in your model. Simple example:
```python
from django.http import HttpResponse


def japan_map(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    ```

---
### 1.6 Manage urls
You have __two__ kind of urls.py files: the __urls.py of your project__, will redirect url requests to __urls.py of your apps__, witch you have to build.
For example let's say we want "http://localhost:8000/ms_bgd_project/japan_map" to show our view of the japan map witch correspond
```python
from django.conf.urls import patterns, url

from japan_map import views

urlpatterns = patterns('',
    url(r'^$', views.japan_map, name='japan_map'),
)
```


---
### 1.7 Sockets




# 2 References
[Django tutorial](https://docs.djangoproject.com/en/1.7/intro/tutorial01/)

[Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
