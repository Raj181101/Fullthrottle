Steps to Setup and to Run The Applications

1)Download Python 3.5 using this link(https://www.python.org/downloads/release/python-350/)
2)Install virtualenv (pip install virtualenv)
3)Activate virtualenv(run below commands to activate virtualenv)
        a)virtualenv venv
        b)cd venv
        c)cd scripts
        d)activate
4)Install requirements in requirements.txt file (pip install -r requirements.txt) use this command to install requirements
5)Run this command to create users (python manage.py users_creation 5 ) here in the place of 5 you can give as much number of users you want
6)Runserver now using command (python manage.py runserver)
7)Paste this url in browser for getting api data of usera and thier activity periods 'http://127.0.0.1:8000/api/users/'
8)Yoc can test it in postman by paste this url and select GET method and submit url you will get api data