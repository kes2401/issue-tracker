# Issue Tracker

[![Build Status](https://travis-ci.org/kes2401/issue-tracker.svg?branch=master)](https://travis-ci.org/kes2401/issue-tracker)

A data driven full stack Django application that is an issue tracker for the fictional UnicornAttractor web app. It allows users to register and log in to report bugs or to request new features. Users can also upvote and comment on bugs and features. New feature requests and new feature upvotes requirement payment through a checkout system that uses Stripe. Users can also view statistics based on the bugs and features contained within the database as well as view their own payment history in their own profile page.

This application was deployed on Heroku and uses Python on the back-end with the Django framework, along with PostgreSQL for database services. It also uses the Bootstrap framework on the front-end, with Chart.js used for building dynamic charts for statistics.

Built for the final project in the Full Stack Software Development diploma course at Code Institute, in the Full Stack Frameworks with Django module.

The live project can be viewed [here](https://issue-tracker-kes.herokuapp.com/).
 

## UX

...


##### User Stories

As a user I can:
- ...
- ...


## Features

##### Existing Features

- Feature 1 - ...
- Feature 2 - ...
- Feature 3 - ...

##### Future Features

- Feature 1 - ...
- Feature 2 - ...
- Feature 3 - ...


## Technologies Used

Languages, frameworks, libraries, and any other tools used to construct this project. 

- HTML 5
    - This project uses **HTML** to structure the content of the website.
- CSS 3
    - The project uses **CSS** to add additional styling to the site and refine responsive beahviour using media queries.
- [Bootstrap](https://getbootstrap.com/)
    - This project uses **Bootstrap** to provide the front-end grid framework and support responsive behaviour.
- JavaScript
    - The project uses **JavaScript** to add and remove content dynamically and to initialise Materialize components.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** to assist in DOM node selection and manipulation as well as in providing feedback to user interactions.
- [Python](https://www.python.org/)
    - This project uses **Python** as the server-side programming language to provide back-end logic and serve dynamic web pages to the browser.
- [Django](https://www.djangoproject.com/)
    - This project uses **Django** as the back-end framework to simplify configuration of the application and routing, to render HTML templates, work with client requests and to assist with user authorisation and authentication.
- [PostgreSQL](https://www.postgresql.org/)
    - This project uses **PostgreSQL** for databases services on the live application through the add-on provided through Heroku and for this I used the Psycopg PostgreSQL database adapter for the Python which can be found here [here](https://pypi.org/project/psycopg2/).
- [Stripe](https://stripe.com/)
    - This project uses **Stripe** to handle payments.
- [AWS S3](https://aws.amazon.com/s3/)
    - This project uses **AWS S3** storage service to store static files including all images, CSS stylesheets, JavaScript files and front-end code libraries used by the application.
- [Chart.js](https://www.chartjs.org/)
    - This project uses **Chart.js** to produce dynamic charts and graphs to provide statistics to users.


## Testing

...


## Deployment

GitHub was used for version control throught the development of the application and to host the code by pushing all code to the repo on GitHub.

This project was then deployed to Heroku to host the live application, following the steps below:

1. Log in to [Heroku](https://www.heroku.com/) and create a new app called 'issue-tracker-kes'
2. Log in to Heroku in the CLI
3. Add the remote Heroku repo
4. Create the `requirements.txt` file by running `pip freeze > requirements.txt` in the CLI
5. Create a `Procfile` by running `echo web: gunicorn issue_tracker.wsgi:application > Procfile` in the CLI
6. Set up S3 Bucket on AWS and update static file storage settings in the project's `settings.py` file
7. Collect all static files in the new AWS S3 storage object using the `python manage.py collectstatic` command in the CLI
8. Add Heroku app URL to the project's `ALLOWED_HOSTS` list 
9. Set environment variables in Heroku for the project's `SECRET_KEY`, `DATABASE_URL`, and `DJANGO_SETTINGS_MODULE`; `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`; and `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` keys and values
10. Set up Travis-CI for continuous integration testing and link to the project's GitHub repo
11. Push all code to remote Heroku repo
12. Restart all dynos on Heroku
13. Heroku account then connected to GitHub repository and set to automatically deploy from the repo's master branch to retrieve all code updates

The live project can be viewed [here](https://issue-tracker-kes.herokuapp.com/).


## Download & Run Locally

To download and run an instance of this project locally you should follow these steps:

1. Download all code from this repo either by cloning the repo or simply downloading and unzipping the .zip file
2. Run `pip install -r requirements.txt` in the CLI to install all required packages for the Django app
3. Set up a Stripe account (if you have none already) and record the Test values for Publishable and Secret keys
4. You will not necessarily need to use AWS S3 storage to run the project locally so you can comment out lines 142 - 154 inclusive in the `settings.py` file to leave the local static folder as the folder for static file storage
5. Create an `env.py` file in the project's root folder and uncomment the import of this file in the settings.py file
6. In the `env.py` file you use `os.environ.setdefault('<KEY>', '<VALUE>')` to set the environment variable's keys and values for:
    - `SECRET_KEY` (You can generate your own Secret Key [here](https://www.miniwebtool.com/django-secret-key-generator/))
    - `DJANGO_SETTINGS_MODULE` (value should be `issue_tracker.settings`)
    - `STRIPE_PUBLISHABLE`
    - `STRIPE_SECRET`
    _You should also set an environment variable called DEVELOPMENT with a value of 1 as there is logic in the `settings.py` file which will determine whether the project is being run in development or production, which will then determine if DEBUG mode should be True or False and also whether the local Django SQLite database should be used for the development environment._
7. Run `python manage.py createsuperuser` to create a Super User for the application who will be able to access the application's Admin dashboard
8. Run `python manage.py makemigrations` in the CLI to create migration files for the local database instance
9. Run `python manage.py migrate` to migrate those migrations to your local SQLite database
10. Run `python manage.py runserver localhost:8080` to run the local development server and then go to localhost:8080 in your browser

Please be aware that running your own local development version of the application will start with an empty database so you will have no recorded bugs or feature requests meaning you may need to create a number of dummy bugs and feature requests to experience the functionality available in the project, including the dynamic generation of charts and graphs on the 'Stats' page of the app.

The management of reported bugs and features is intended to be done through the project's Admin dashboard which can only be accessed by a Super User. This issue managements in the Admin dashboard involves updating and changing the status of individual issues, ie. from 'Pending' to 'In Progress', or 'In Progress' to 'Closed', and also setting the 'Date Closed' value on any given issue. This data impacts the generation of the statistics-based charts and graphs.


## Credits

#### Acknowledgements

Aside from the Code Institute course content I found the following resources to be beneficial while completing this project:
- The Django tutorial by The Net Ninja on YouTube was very helpful as an additional resource for learning the basics of Django, the playlist for which can be found [here](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
- The official Django documentation, found [here](https://docs.djangoproject.com/en/2.2/)
- The [Chart.js official documentation](https://www.chartjs.org/docs/latest/) and the ['Getting Started with Chart.js'](https://www.youtube.com/watch?v=sE08f4iuOhA) video tutorial on YouTube by Traversy Media were great for getting up and running quickly with Chart.js
- The [Yeti theme](https://bootswatch.com/yeti/) from Bootswatch was used with Bootstrap for development of the UI
- Finally, thank you to my mentor Aaron Sinnott for his advice and guidance throughout the project


## Contact

If you have any questions or comments relating to this project you can contact me by email at [keithscully83@gmail.com](mailto:keithscully83@gmail.com)