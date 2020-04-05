# A Django Interface to the CMIP6 Data Request

This repository contains a django interface to the CMIP6 data request.
It is build on the database constructed in [zklaus-cmip6/sqlite-dreq](https://github.com/zklaus-cmip6/sqlite-dreq).
At the moment, only a rudimentary [admin interface](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/) is provided, but an extension to include more elaborate functionality is possible.

To try this interface, do the following:

1. Clone the repository with
   ```
   git clone https://github.com/zklaus-cmip6/django-dreq.git
   ```
   This will create a new directory `django-dreq`.
1. Change to that directory
   ```
   cd django-dreq
   ```
1. Use the provided `environment.yml` file to create a conda environment
   ```
   conda env create -f environment.yml
   ```
1. Activate the environment
   ```
   conda activate django-dreq
   ```
1. Change to the directory of the django site
   ```
   cd cmip
   ```
1. Run the server
   ```
   python manage.py runserver
   ```
1. Visit the admin interface at http://localhost:8000/admin and login using username `admin` and password `admin`.
