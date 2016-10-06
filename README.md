STEP 0 (Optional but recommended)


Install mkvirtualenv globally:
sudo pip install virtualenvwrapper

Add mkvirtualenv script to your .bashrc folder (local folder may vary)
echo 'source ~/.local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc

mkvirtualenv --python=2.7.12 twitter_album (2.7.x, x may vary, but tested with Python 2.7.*)
workon twitter_album


STEP 1
Set your Twitter consumer_key, consumer_secret, access_token_key, access_token_secret in Tada.py file

STEP 2


pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver


OTHER STUFFS:

Tests:
./manage.py test

Admin UI:
python manage.py createsuperuser


ho ritenuto testare solo in model, per mancanza di  tempo e per prendere confidenza con l'ORM di Django (è stata utili per poi sviluppare la parte di salvataggio del cron)