# CS4400
## Installation and Setup
First you have to check that the following is installed on your machine

 - Python 2.7 and PIP
 - [Bower](https://bower.io) - browser package manager (css/js libraries)
   - You will need to install Node and NPM to install Bower
   - Alternatively, you can ask Andrew how to work around this

After those are installed, `git clone` this repository to you local
machine and install its dependencies.

```
$ git clone <git repo url>
$ cd cs4400-project
$ pip install -r requirements.txt # Install Python dependencies
$ bower install # Install client-side (browser) dependencies (css/js)
```

## Running the app

```
$ python manage.py runserver
$ ./manage.py runserver # this should also work
```
