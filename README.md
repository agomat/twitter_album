
![Screenshot of the product](http://oi63.tinypic.com/156dzrk.jpg)


## Abstract


You are dealing with an exercise project. The aim is to create a demon that uses the Twitter API to fetch a list of images.
It is intended to create an album based on a hashtag search.
The app should create an album, runs every 20min and fetches the last photos posted on twitter.
When the album reaches 100|200|300|400|501 photos it would be able to send an email.

The app exposes an API and a visual representation of the album.
You can:

1. Access a url in your browser that shows all the pictures
2. Access a REST api that shows you the data structure of the pictures in your album
3. Create a page and a link of the most 7 popular photos in the album and export it to Facebook
4. Get email notifications when the album reaches particulars numbers of photos
5. See the date/time when the photos were included


### Install - Step 0 (optional but recommended)

Install mkvirtualenv globally:

`sudo pip install virtualenvwrapper`

Add mkvirtualenv script to your **.bashrc** file (local folder may vary).

`echo 'source ~/.local/bin/virtualenvwrapper.sh' >> ~/.bashrc`
`source ~/.bashrc`

Create a new env:

`mkvirtualenv --python=2.7.12 twitter_album` (2.7.x, x may vary, tested with Python 2.7.*)

activate your virtual space:

`workon twitter_album`


### Install - Step 1
Set your Twitter `consumer_key`, `consumer_secret`, `access_token_key`, `access_token_secret` in *datasource/tasker/ConfMixin.py* file.

Set your cool hashtag (`topic`) in the same file.

### Install - Step 2

`pip install -r requirements.txt`
`python manage.py makemigrations app`
`python manage.py migrate`
`python manage.py runserver`


### Misc

Run tests:

`./manage.py test`

Admin UI:

`python manage.py createsuperuser`

Pick an username and a password. Point the browser to `/admin`.

Exit virtualenv:

`deactivate`

### Caveats
**django-cron** may do not work properly with virtualenv.
To run it manually append these lines to /twitter_album/urls.py:

`from datasource.tasker.TwitterTask import TwitterTask`
`TwitterTask()`

Then run the server multiple times to populate your album.
It is possible because the tasker class is decoupled from django-cron module.

Some exceptions are not handled (e.g. Authtentication error, Nertwork error, Range Xrate Limits error) because this is a demo exercise, not meant to go in production.

**Facebook social button**: may not work in cause the Button-App is not registered @Facebook.
You can found it in every page. As required, it is visible also in the filtering _7-most-rated_ page.

## Api usage

1. Get all photos
   `/api`
2. Get photos by topic/hashtag (#carnival example)
   `/api/topic/%23carnival`
3. Get the most 7 popular photos
   `/api/topic/%23carnival/7`
4. Get photos by owner
   `/api/owner/{<owner_display_name>}`

## High level Design

![Packages](http://oi63.tinypic.com/b9hx93.jpg)

The app is organised in 4 mainly "Packages".

1. _Twitter_album_
   That contains the settings and the urls whose Django looks when the app starts.

2. _Datasoruce/Tasker_
   It is a place that should contains the business logic related to the demon and it's work. The __TwitterCron__ class calls the __TwitterTask__ and uses the __DataAccess__ class to save model data. __DataAccess__ should be the only class - of this package - meant to communicate to the model.

3. _App_
   Contains the view logic (uses models and calls template of course). Provides an API.
   
4. _Templates_
   Django HTML templates

## Tasker entity

__TwitterTask__ class contains three methods:

1. _connect()_
   It does establish a connection to Twitter
   
2. _search()_
   It prepares the query (kv object) and calls _GetSearch_ Twitter API. The first time it searches the most recent image on Twitter. Once got it, next times it prepares a query based on that one Twitter-ID. It uses **max_id** parameter to get older photos.
   It uses *get_min_id_or_none()* accessory method to calculate the minimun Twitter-ID of local photos.
   The minimun ID will be considered as **max_id** for the current API invocation.
   So, the demon will always search for older photos. To search freshes photos change *Min* to *Max* in **DataAccess** class, or write an entropy that choose every time if it will search for older of newer photos .

3. _process_list()_
   Processes the list of results. It checks if exists the image url, the owner, and the favourite counter. Then it calls _save_photo_ to save the entity (the model will checks if the image urls exits already). 

## Views design

1. _CommonListsMixin_ 
   A simply _ContextMixin_ class that gets all topics (Album) and all owners. Will be used by other View classes.

2. _IndexView_
   Uses _CommonListsMixin_ mixin to fill the context about topics (Album) and owners for the left navigation bar. It also prints all the photos if the route starts with `/api`.

3. _TopicView_
   Uses _CommonListsMixin_ mixin to fill the context about topics (Album) and owners for the left navigation bar. It outputs all the photos of a given topic (hashtag). It also prints the data via API. If the route contains `.../7` it searches for the 7-most-rated photos of current album.

4. _OwnerView_
   Much like _TopicView_, but for the owners.