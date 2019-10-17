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

Reference: https://docs.djangoproject.com/en/2.2/topics/db/queries/

## Create the home view

Show all the quotes to the home view. Start with fetching all the quotes.

```python
quotes = Quote.objects.all()
```

Order the quotes. Draft quotes to the bottom.

```python
quotes = Quote.objects.all().order_by('is_draft')
```

## Change the template. List all quotes.

Introduction to django template system. See Template inheritance (extends, blocks)

Output variables in template. List all quotes with a for loop.

```python
{% block content %}

    {% for quote in quotes %}

        <blockquote
            {% if quote.is_draft %}
            class="draft"
            {% endif %}
            >

            <p>{{ quote.text }}
                {% if quote.is_draft %}
                    <i>(Draft)</i>
                {% endif %}
            </p>
            <footer>
                — {{ quote.author_name }}
            </footer>
        </blockquote>

    {% endfor %}

{% endblock content %}
```

Add some css. Change the style.css

```html
blockquote {
    margin: 0;
}

blockquote p {
    padding: 15px;
    background: #eee;
    border-radius: 5px;
}

blockquote p::before {
    content: '\201C';
}

blockquote p::after {
    content: '\201D';
}

.draft {
    opacity: 0.5;
}
```

## Show a single quote

Change the urls.py, views.py files.

Add a single.html template file.

## Show a single quote via dynamic routing

Make the route dynamic. Change views.py and urls.py accordingly.

```python

from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    path('quotes/<int:id>/', views.single_quote, name='single'),
]
```

## 404 error handling

Watch what happens if quote does not exist

Catch the exception:

```python
from django.http import Http404
...
    try:
        p = Quote.objects.get(pk=id)
    except Quote.DoesNotExist:
        raise Http404("Quote does not exist")
```

Or use the get_object_or_404 shortcut helper function:

```python
from django.shortcuts import get_object_or_404
...
quote = get_object_or_404(Quote, pk=id)
```

Add a 404.html template file. Shows only when DEBUG = False in settings.py

## Single quote styles

Override the default styles from base.html.

Create style_single.css file with some new fancy styling.

```html
@import url('https://fonts.googleapis.com/css?family=Special+Elite');

html, body {
    height: 100%;
    margin: 0;
}

body {
    font-family: 'Special Elite', cursive;
    background: #fffdf5;
    color: #3f3f5a;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

blockquote {
    font-weight: 100;
    font-size: 2rem;
    max-width: 600px;
    line-height: 1.4;
    position: relative;
    margin: 0;
    padding: .5rem;
}

blockquote:before,
blockquote:after {
    position: absolute;
    color: #f1efe6;
    font-size: 8rem;
    width: 4rem;
    height: 4rem;
}

blockquote:before {
    content: '“';
    left: -5rem;
    top: -2rem;
}

blockquote:after {
    content: '”';
    right: -5rem;
    bottom: 1rem;
}

cite {
    line-height: 3;
    text-align: left;
}
```

## Filter quotes

Add a form input to filter the quotes displayed.

Get the request input via request.GET dictionary

```python
query = request.GET.get('q', None)
```

Use the filter method get the quotes that match.

```python
quotes = Quote.objects.filter(text__contains=query)

```

## Get a random quote

Change the urls.py, views.py files to add the random route.

Use the same template file single.html. Add I'm feeling lucky option in index.html.

Fetch only the non draft quotes. Use the random module to make the random choice from the fetched quotes.

```python
import random

...
    quotes = Quote.objects.filter(is_draft=False)
    random_quote = random.choice(quotes)
```

## Create an author model (one to many relationship)

Create an Author model with a name text field.

```python
from django.db import models
from django.utils.timezone import now

class Author(models.Model):
    name = models.CharField(max_length=255, default='Unknown')

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField(blank=False, null=False)
    # author_name = models.CharField(max_length=255, default='Unknown')
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
```

Run the migrations.

Add Author model to admin site. Create Author model and assign it to some quotes.

Explore one to many relationship api.

```python
from main.models import Author, Quote

author = Author.objects.get(pk=1)
author.quote_set.all()
author.quote_set.filter(text__contains='value')

quote = Quote.objects.get(pk=1)
quote.author
quote.author.name
```

