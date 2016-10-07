**STEP 0 (Optional but recommended)**

Install mkvirtualenv globally:
sudo pip install virtualenvwrapper

Add mkvirtualenv script to your .bashrc folder (local folder may vary)
echo 'source ~/.local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc

mkvirtualenv --python=2.7.12 twitter_album (2.7.x, x may vary, but tested with Python 2.7.*)
activate your virtual space:
workon twitter_album


**STEP 1**
Set your Twitter consumer_key, consumer_secret, access_token_key, access_token_secret in datasource/tasker/ConfMixin.py file

**STEP 2**


pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver


**OTHER STUFFS:**

Tests:
./manage.py test

Admin UI:
python manage.py createsuperuser

Exit virtualenv
deactivate

**_NOTE_** django-cron may do not work properly with virtualenv.
To run it manually append to /twitter_album/urls.py:
`from datasource.tasker.TwitterTask import TwitterTask
TwitterTask()
`
Then run the server multiple times to populate your album
This is possibible because The tasker class is decoupled from django-cron model

**USING API**
(append `/api` before the url in your browser)
**USING FB SOCIAL SHARE**
(may not work in production because the facebook App Sdk is not registered)
