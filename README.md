# OASIS
This project [oasis](https://reservebooking-f88a92f8cf30.herokuapp.com/) is a minimalistic site that showcases booking reservation . 
<!-- ![home](/assets/images/finterface.png) -->
# User Experience (UX)
Key information for the app
this section provides insight into the UX process, focusing on who the app is for, the main aims of the project and how the app can help users meet their needs
<!-- 
![exit](/assets/images/exit.png) -->

# Project goals:<br>
 User able to book reservastions
<!-- ![input](/assets/images/inputinterface.png)  -->
<br>

Users able to book for tables and rooms at the same
<!-- ![option](/assets/images/priceoption.png) -->
<br>

Users get rervation Id after booking

# Features:<br>
Login
![input](assets/1705656646441.png) <br>

Signup
![input](assets/1705656564950.png) <br>

booking reservations
![input](assets/1705656725812.png) <br>

   Date and Time booking<br>
   Multiple guest<br>


booking cancelations<br>
![input](assets/1705656799278.png) <br>


# Assumptions:<br>
all rooms and tables are the sameand have thesame size and design
<br>

There infinite numbers of rooms hence eliminating double booking
<br>



# Responsiveness<br>

screen w-1700
![input](assets/1706248149105.png) <br>



screen w-1500
![input](assets/1706248200995.png) <br>

screen w-600
![input](assets/1706248224114.png) <br>

screen w-350
![input](assets/1706248249632.png) <br>






# Deployment<br>
``` make a new file name Procfile and do not put any extension in it. It is a file required by Heroku

. For our app we can write the following command "web: gunicorn name_of_your_app.wsgi -log-file -" in the procfile

. pip install gunicorn

. login into heroku in the browser

. Make a new heroku app

. update settings.py file ALLOWED_HOSTS = ["your_app_name.herokuapp.com"]

. With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service

so run pip install whitenoise


Add it in MIDDLEWARE in settings.py file

MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
   ...
]

.Make a new Github Repo and add all of your code in it.

.Using Heroku Postgres
Go to your app dashboard and in the Resources section search for Postgres and click add.


. Now paste the following code below DATABASES in settings file

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


.Currently, your database is empty and you might want to fill it.

Open terminal
type → heroku login
After the login run the following commands
heroku run python manage.py makemigrations
heroku run python manage.py migrate ...

# Credits<br>
Full credit goes to code institute for the template provided to make this project a possiblityl



