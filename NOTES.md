# Notes (quotes sample web application)

## File structure
* settings.py
* models.py
* urls.py
* views.py
* templates dir
* static dir

Get familiar with replit environment. Note that is a somewhat different (and more simplified) django installation

See the architecture. 

![architecture](https://mdn.mozillademos.org/files/13931/basic-django.png "Architecture")

Change something at templates (see the change).

## manage.py and the shell

Press F1 to open the menu. Select **Open Shell**

```
python manage.py
```

Notable commands
```
python manage.py shell
python manage.py makemigrations
python manage.py migrate
```

## Create the model

Create the first version of the Quote model
Add the text field and the author name

```python
text = models.TextField(blank=False, null=False)
author_name = models.CharField(max_length=255, default='Unknown')
```

## See the model in the Admin site

1. Create an admin superuser

```
python manage.py createsuperuser
```

2. Create an admin.py file to make the Quote model modifiable in the admin

```python

from django.contrib import admin

from .models import Quote

admin.site.register(Quote)
```

3. Explore the admin page
4. Add some Quotes (you can find some quotes here: https://www.keepinspiring.me/famous-quotes/)
5. Add str dunder method in model to look better in admin index page
```python

def __str__(self):
    return self.text
```

## Change the Quote model

Add is_draft boolean field to Quote model

```python
is_draft = models.BooleanField(default=False)
```

Note the default option.

Run the manage.py commands to make the migration.
```
python manage.py makemigrations
python manage.py migrate
```

Check the migrations generated file.

## Invoke the shell and play with the django model api

* Get all objects
* Get a single object
* Create an object
* Modify an object
* Save an object in db


## Create the home view

Show all the quotes to the home view. Start with fetching all the quotes.

```python
quotes = Quote.objects.all()
```

## Change the template

Introduction to django template system. See Template inheritance (extends, blocks)