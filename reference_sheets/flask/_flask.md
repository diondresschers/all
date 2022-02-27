# Flask Reference Sheets

* Title: Flask Reference Sheets
* Creation date:  2022-02-27
* Target audience: People interested in Flask
* License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Copyright: Dion Dresschers
* Writer(s): Dion Dresschers
* Inspiration: [Miguel Grinberg - The New and Improved Flask Mega-Tutorial](https://courses.miguelgrinberg.com/courses/enrolled/336779)
* Original file(s): [all/_flask.md at main · diondresschers/all](https://github.com/diondresschers/all/blob/main/reference_sheets/flask/_flask.md) 
* Status: Concept
* Version: 2022-02-27v10_23

Equipment: 

* Device: Dell Latitude E5270
* Device name: e5270-win10
* Processor: Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz   2.50 GHz
* Installed RAM: 8.00 GB (7.67 GB usable)
* System type: 64-bit operating system, x64-based processor
* Edition: Windows 10 Pro
* OS build: 19043.1526
* Experience: Windows Feature Experience Pack 120.2212.4170.0

Software:

* Windows Subsystem for Linux (WSL)
  * DISTRIB_ID=Ubuntu
  * DISTRIB_RELEASE=20.04
  * DISTRIB_CODENAME=focal
  * DISTRIB_DESCRIPTION="Ubuntu 20.04.4 LTS"
  * NAME="Ubuntu"
  * VERSION="20.04.4 LTS (Focal Fossa)"
  * ID=ubuntu
  * ID_LIKE=debian
  * PRETTY_NAME="Ubuntu 20.04.4 LTS"
  * VERSION_ID="20.04"
  * HOME_URL="https://www.ubuntu.com/"
  * SUPPORT_URL="https://help.ubuntu.com/"
  * BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
  * PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
  * VERSION_CODENAME=focal
  * UBUNTU_CODENAME=focal

# Install Python

Install Python:

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/all$ sudo apt install python3`

Check:

```
dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/all$ python3 --version
Python 3.8.10
```

# Install Python PIP

Install Python PIP

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/all$ sudo apt install python3-pip`

Check:

```
dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/all$ python3 -m pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

# Install Python Virtual Environment

Install Python Virtual Environment

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/all$ python3 -m pip install virtualenv`

Check:

```
dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/all$ python3 -m virtualenv --version
virtualenv 20.13.2 from /home/dion/.local/lib/python3.8/site-packages/virtualenv/__init__.py
```

# Create a Flask Project Directory

In this case we name the project `openshebang`

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git$ mkdir openshebang`

Go inside of that directory:

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git$ cd openshebang`

From there create a Python Virtual Environment, and name it `venv_openshebang`:

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/openshebang$ python3 -m venv venv_openshebang`

Short the Linux prompt:

`dion@e5270-win10:/mnt/c/Users/dion/data/prive/git/openshebang$ $PS1='\u@\W $ '`

See the shortened prompt:

`dion@openshebang $ `

Activate the Python Virtual Environment:

`dion@openshebang $ . venv_openshebang/bin/activate`

See the prompt changing with the Virtual Environment:

`(venv_openshebang) dion@openshebang $ `

Install Flask inside the Virtual Environment:

`(venv_openshebang) dion@openshebang $ python3 -m pip install flask`

```
Collecting flask
  Downloading Flask-2.0.3-py3-none-any.whl (95 kB)
     |████████████████████████████████| 95 kB 2.9 MB/s
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.0.3-py3-none-any.whl (289 kB)
     |████████████████████████████████| 289 kB 3.1 MB/s
Collecting Jinja2>=3.0
  Downloading Jinja2-3.0.3-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 6.7 MB/s
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.0-py3-none-any.whl (15 kB)
Collecting click>=7.1.2
  Downloading click-8.0.4-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 4.1 MB/s
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, click, flask
Successfully installed Jinja2-3.0.3 MarkupSafe-2.1.0 Werkzeug-2.0.3 click-8.0.4 flask-2.0.3 itsdangerous-2.1.0
```

# `Hello World`

From your project folder (called `openshebang`), and your project Virtual Environment, create a folder where you app resides, called `app`:

`(venv_openshebang) dion@openshebang $ mkdir app`



## `Hello World` - `app\__init__.py`

Create inside that `app` folder a `__init__.py`-file:

`(venv_openshebang) dion@openshebang $ touch app/__init__.py`

Make sure the `__init__.py` looks like the below file:

`(venv_openshebang) dion@openshebang $ cat app/__init__.py`

```
from flask import Flask # Import the Flask class. You've installed 'flask' in the Virtual Environment.

app = Flask(__name__) # Instantiate a new Flask app, called `app`. # Based on the `__name__` Flask knows where to find other files.

from app import routes # Import Flask `routes` `. # Normally in Python you will do an `import` at the top. This is The bottom a workaround to 'circular imports', which is a common problem with Flask applications.
```

## `Hello World` - `app\routes.py`

Create inside the `app` folder a `routes.py`-file:

`(venv_openshebang) dion@openshebang $ touch app\routes.py`

Make sure the `routes.py` file looks like below file:

`(venv_openshebang) dion@openshebang $ cat app/routes.py`

```
from app import app # The first `app` is the `app`-directory, it's the Flask package, the second `app` is the instantiated

@app.route('/') # This is a Python decorator, this creates a mapping between an URL and a Python function.
@app.route('/index') # A second route.
def index():
```
## `Hello World` - `openshebang.py`

Create in the project directory called `openshebang`, the file `openshebang.py`, this resised above the `app` folder.

`(venv_openshebang) dion@openshebang $ touch openshebang.py`

Make sure the file looks like the file below:

`(venv_openshebang) dion@openshebang $ cat openshebang.py`

```
from app import app # The first `app` is the directory called `app`, the second is the `app` that is the instantiation off the Flask class.
```

## Run `Hello World`

We need to create a Linux Environment Variable called `FLASK_APP`.

First check if this has not been created yet, as there should be no results:

`(venv_openshebang) dion@openshebang $ env | grep -i flask`

Then create the Flask environment, so Flask knows which file to use to serve from:

`(venv_openshebang) dion@openshebang $ export FLASK_APP=openshebang.py`

See now that this Environment variable exists:

`(venv_openshebang) dion@openshebang $ env | grep -i flask`

See the results:

```
FLASK_APP=openshebang.py`
```

Now run Flask:

`(venv_openshebang) dion@openshebang $ flask run`

See the results and the URL to which we can make contact to the Flask webserver.

```
 * Serving Flask app 'openshebang.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

So open [127.0.0.1:5000/](http://127.0.0.1:5000/)

Also see the the `/index`-route does exists and points to the same Python function:

[127.0.0.1:5000/index](http://127.0.0.1:5000/index)

Notice that other URLs/routes don't exists:

[404 Not Found](http://127.0.0.1:5000/route_does_not_exist)

You can exit in the running Flask development server in the Linux console with `<CTRL> + <C>`-keys.









