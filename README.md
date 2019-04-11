# Ledger Web

Ledger Web was initially created to bridge the gap between a
smartphone and [Ledger CLI](https://ledger-cli.org/) by exposing a
HTTP API.  Since then it evolved into a more general web UI for
Ledger.

## Screenshots

### Charts

[![](https://raw.githubusercontent.com/vifon/ledger-web/master/examples/Charts.png)](https://raw.githubusercontent.com/vifon/ledger-web/master/examples/Charts.png)

### API replacement rules

[![](https://raw.githubusercontent.com/vifon/ledger-web/master/examples/Rules.png)](https://raw.githubusercontent.com/vifon/ledger-web/master/examples/Rules.png)

### Ledger register

[![](https://raw.githubusercontent.com/vifon/ledger-web/master/examples/Register.png)](https://raw.githubusercontent.com/vifon/ledger-web/master/examples/Register.png)

## Installation

1. Clone the repository and install the dependencies:

        git clone https://github.com/vifon/ledger-web
        cd ledger-web
        virtualenv .venv
        . .venv/bin/activate
        pip install -r requirements.txt

2. Set up the database.

        ./manage.py makemigrations
        ./manage.py migrate

3. Set the access credentials:

        ./manage.py createsuperuser
        ./manage.py runserver

   Follow the instructions on screen and the enter
   http://localhost:8000/admin

   Add a new entry in the *Ledger paths* table for your user, pointing
   it to your Ledger file.

   If you want to use the HTTP API, add an access token too.  A token
   should be between 32 and 256 characters long.  You'll need to
   generate it yourself, for example with `pwgen 256 1`.

4. Customize `ledger/settings.py`, specifically you may be interested
   in the last 3 options.

5. Check that everything works at http://localhost:8000/

6. Enable the production mode in `ledger/settings.py`:

    - Set `DEBUG = False`.
    - Generate a new `SECRET_KEY`, for example with [this snippet](https://gist.github.com/sandervm/2b15775012685553f0e2).
    - Enter your domain and possibly a localhost in `ALLOWED_HOSTS`.
    - Set `STATIC_ROOT`, for example `'/var/www/ledger' + STATIC_URL`
      and run `./manage.py collectstatic`.
      
7. Set up a WSGI server (for example Gunicorn):

        pip install gunicorn
        gunicorn -w 4 -b 127.0.0.1:1234 ledger.wsgi
        
8. Set up a reverse proxy in a HTTP server, for example Nginx, a
   config file included in `examples/ledger.nginx.conf`.

## Copyright

Copyright (C) 2019  Wojciech Siewierski

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
