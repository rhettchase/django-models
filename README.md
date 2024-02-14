# LAB - Class 27

## Project: Django Models

### Project Description

This django built web app utilizes Django Model to allow data to persist using Python objects (models). The models define the structure of stored dta, including the field types, max size, default values, etc. The model is added to `admin` and allows snacks to be added via the Admin panel.

The testing suite verifies status code and the correct template is used. It also includes a `setUp` method that sets up the preconditions for the tests.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Using Models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
- [Django Admin](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)

### Setup

- `pip install -r requirements.txt`
- `npm install`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

- Clone repo
- Install dependencies (see above)
- See the page in browser by running `python manage.py runserver`
- Open the page via the local server address specified in the terminal

##### Add snack to the database

- In separate terminal, create superuser with command `python manage.py createsuperuser`
- Visit the `/admin` path and login with the superuser username and password you created
- In the `Snacks` menu click `add` then fill in the snack information (name, purchaser, description)

#### How to use your library (where applicable)

- N/A

#### Tests

- `python manage.py test`
