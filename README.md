# Visitor Management System

## Project Overview

UWA has several physical sites outside of the Crawley campus that allow visitor access. Currently, there is no robust system to keep track of visitors, which presents potential security and health & safety issues.

The goal of this project is to supply a robust tracking system that logs visitor movements, such that those in charge can keep track of who is present at a site, increase accountability for those using the sites, and present site usage data to management for data analysis purposes. The system will be applied across multiple sites, and as such must be robust enough to handle multiple situations as outlines in the requirements breakdown.

Some sites are more sensitive and require robust entry/exit protocols, while others are less sensitive and simply require visitors to register when they enter and exit the site. The method by which our system is applied at the site-level is outside the scope of this project; our aim is only to supply the system so that it can be accessed by visitors on their personal devices via a QR code, or via a tablet at the front desk when the site is considered sensitive. How the system is applied at any given location is considered the responsibility of those at that individual site.

## Running the Web App on a Linux Server

First make sure your system is up to date by running:

```shell
$ sudo apt-get update
$ sudo apt-get -y upgrade
```

Make sure that you have installed the latest version of Python first. To see which version of Python you have installed, open a terminal and run:

```shell
$ python --version
```

If you don't have Python installed on your device, then you can easily install with the following commands:

```shell
$ sudo apt-get install python
```

Also check if you have the latest version of pip.

```shell
$ python3 -m pip install --user --upgrade pip
$ python3 -m pip --version
```

You can install python virtual environment via:

```shell
$ python3 -m pip install --user virtualenv
```

Create a new working directory and `cd` into it. Then create a virtual environemnt inside by running:

```shell
$ python3 -m venv env
```

The above command uses `venv` to create a virtual Python installation in the `env` folder.

Once the virtual environment is created you can activate it by running:

```shell
$ source env/bin/activate
```

Clone the repository into your working directory and install the required dependencies.

```shell
$ pip install -r requirements.txt
```

Now you are ready to run the django server. You can `manage.py` within the vms directory. To run the server"

```shell
$ python3 manage.py runserver
```

Open your browser to access the web app:

```shell
http://localhost:8000/
```

## Directory Structure
The web app has two main sections. The ```survey``` app contains models, views and controller that the visitors will interact with. '```survey``` has its own static, template, routes, forms, and urls.

The next main section is the admin area where the admins interact with. We have customized the default django admin for this purpose. These customizations are included in separate static and template folders within the ```vms``` directory.

## Resources

[Django Docs](https://docs.djangoproject.com/en/3.2/)
