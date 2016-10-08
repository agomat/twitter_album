## Abstract
todo


## Install

Install guide.

### Step 0 (optional but recommended)

Install mkvirtualenv globally:

`sudo pip install virtualenvwrapper`

Add mkvirtualenv script to your **.bashrc** file (local folder may vary).

`echo 'source ~/.local/bin/virtualenvwrapper.sh' >> ~/.bashrc`
`source ~/.bashrc`

Create a new env:

`mkvirtualenv --python=2.7.12 twitter_album` (2.7.x, x may vary, tested with Python 2.7.*)

activate your virtual space:

`workon twitter_album`


### Step 1
Set your Twitter `consumer_key`, `consumer_secret`, `access_token_key`, `access_token_secret` in *datasource/tasker/ConfMixin.py* file.

Set your cool hashtag (`topic`) in the same file.

### Step 2

``` pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver
```

### Misc

Run tests:

`./manage.py test`

Admin UI:

`python manage.py createsuperuser`

Pick an username and a password. Point the browser to `/admin`.

Exit virtualenv:

`deactivate`

### Note
django-cron may do not work properly with virtualenv.
To run it manually append this to /twitter_album/urls.py:

`from datasource.tasker.TwitterTask import TwitterTask`
`TwitterTask()`

Then run the server multiple times to populate your album.
It's possible because the tasker class is decoupled from django-cron module.

**Facebook social button**: may not work in production cause the Button-App is not registered @Facebook.
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

## Desegn

todo

## Tasker

todo

## Views

todo