# Python SCM Reference Implementation

The python code for the app will live under `py`.

It will have the following subdirectories:
- `apps` : self contained django apps, may import from `lib`s 
- `lib` : utility functions, self contained computations, stateless, don't use django models, may import from other `lib`s
- `sdk` : kilo sdk type functions, that likely use django models, may import from `lib`s and `apps` 
- `services` : containers to run the things, like django server, consumer, internal tool, etc... imports from `apps`

## Creating self contained django apps

Create your django app in it's own django server, `makemigrations` or whatever else you need to do, then extract it [mostly following the official documentation](https://docs.djangoproject.com/en/4.1/intro/reusable-apps/). Finally, move it to the api dir. 

# Setup

Set up python 3.11 with `pyenv`. Set up pip and poetry. Make sure your poetry uses python 3.11 (poetry env use). 

# How to run the server
`cd /services/restserver`
`poetry install`
`poetry shell`
`python manage.py migrate`
`python manage.py runserver`

At this point the [app1](http://localhost:8000/app1) and [app2](http://localhost:8000/app2) links should work - return text and not an error.

# How to add new libraries

Add the library dependencies to your project with `poetry add PATH --editable`. This will allow you to change the code without having to re-compile or re-install the lib.

Run `poetry shell` before starting the server.

If you mess up, you may need to `poetry env info` and delete the poetry virtualenv then start over with `poetry install`.

# Cavets

No circular imports! 

# Contact

Javin
