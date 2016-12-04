# CS4400
## Installation
First you have to check that the following is installed on your machine

 - Python 2.7 and PIP
 - [Bower](https://bower.io) - browser package manager (css/js libraries)
   - You will need to install Node and NPM to install Bower
   - Alternatively, you can ask Andrew how to work around this

After those are installed, `git clone` this repository to you local
machine and install its dependencies.

```
git clone <git repo url>
cd cs4400-project
pip install -r requirements.txt # Install Python dependencies
bower install # Install client-side (browser) dependencies (css/js)
```

## Setup
We have to configure our Flask webapp with the server credentials.
There is an example file at `app/db.py.example`. This needs to be
copied to `app/db.py` and filled in with the correct information.

```
cp app/db.py.example app/db.py
vim app/db.py # Replace the dummy values with SQL server credentials
```

Database migration scripts are in `migration` and need to be run on the
database before lauching the web app.

Example:
```
mysql -u <username> <schema> < migration/001-init.sql
# repeat for all scripts in migration
```

## Running the app

```
$ python manage.py runserver
$ ./manage.py runserver # this should also work
```

