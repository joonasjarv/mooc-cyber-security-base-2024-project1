# Cyber Security Base 2024 Project I

This repository contains a website for [Cyber Security Base Project I course](https://cybersecuritybase.mooc.fi/module-3.1).

## Installation

The website is implemented using Python & Django as recommended in the course description. The Django [starter website](https://docs.djangoproject.com/en/5.1/intro/tutorial01/) is used as a basis for this website.

To set up the project, follow these steps:

1. Install libraries

See [Cyber Security Base installation guide](https://cybersecuritybase.mooc.fi/installation-guide) if you do not have Python and Django libraries installed.

2. Clone the repository

```
git clone https://github.com/...
cd mooc-cyber-security-base-2024-project1/mysite
```

3. Set up the database

```
python3 manage.py migrate
```

1. Start the development server

```
python3 manage.py runserver
```
Application should now be running on http://127.0.0.1:8000/. The admin panel can be accessed from http://127.0.0.1:8000/admin/.


## Creating an admin user

To create an admin user, run:
```
python3 manage.py createsuperuser
```
and follow the prompts. For further information see [this documentation](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user).
