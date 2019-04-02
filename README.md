# Patch

Hi! This is a patch to ns-3-AppStore to create a new application in the AppStore DB, by parsing details from the bakefile.


## Prerequisites

After cloning the Appstore repo and setting up locally, clone this repo and app put this folder scripts inside the folder src of ns-3-Appstore alongside apps, accounts, help and other django apps.

Our Objective is to create a script which works in django context.
For that we need the same environment like that of django application

It can be fulfilled by installing django_extensions
```
source venv/bin/activate
pip install django_extensions
```
We need to add django_extensions to installed apps. Now goto src/appstore/settings and do :
```
nano development.py
```
Add ```'django_extensions'``` to INSTALLED APPS
## Running the Script
I have used a virtual environment called **venv**. 
```
To activate virtual environment use following command in the homedirectory:
> source venv/bin/activate
```

Change directory to src
```
cd src
```
To parse the bakefiles move the .xml files to **scripts** folder

Now run the script using :
```
python manage.py runscript script
```
Enter the name of XML file without .xml extension
and the information from bakefile will be parsed and added to DB.

**Example:**

```
Starting Bakefile parser . . .
Please enter the name of xml file to read
(don't include .xml in name)
Name of xml file: <enter file name>
```
```
Starting Bakefile parser . . .
Please enter the name of xml file to read
(don't include .xml in name)
Name of xml file: sift-ns3
```

**Result :**
```
Name: sift-ns3
Title: sift-ns3
App type: M
Abstract: NA
Description: App description
Active: True
Stars:0
Votes:0
Downloads:0

App added to DB 

App Details in DB:
App ID: 9
```
## Conclusion

In src folder run:
```
python manage.py runserver
```
While the server is running goto [http://127.0.0.1:8000/admin/apps/app/](http://127.0.0.1:8000/admin/apps/app/) and check whether the app is added or not.

Thank You.
