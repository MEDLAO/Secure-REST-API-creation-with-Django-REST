## Project : Create a secure RESTful API using Django REST

[**Français**](README-fr.md)
<p>
  <img src="pictures/softdeskapi-db-diagram.png" width="250" height="200" />
  <img src="pictures/softdeskapi-endpoints.png" width="250" height="200" />
  <img src="pictures/softdeskapi-postman-doc.png" width="250" height="200" />
</p>


### Table of contents :
1. Project Description/Scenario.
2. Compatible configurations.
3. Installing the program.
4. Features.
5. Authentication and permissions
6. Running the program.

## 1. Project Description/Scenario :

This project was carried out as part of the Python Developer training offered by OpenClassrooms.

SoftDesk, a software development and collaboration company, has decided to release an application
that allows reporting and tracking of technical issues (issue tracking system).
This solution is aimed at client companies in a B2B context.

This issue tracking application is available on web, Android, and iOS platforms and primarily
enables users to create various projects, add users to specific projects, create issues within 
those projects, and assign labels to these issues based on their priorities, tags, etc.

Consequently, the Sofdeskapi API provides various endpoints that will serve data 
across the three platforms.

## 2. Compatible configurations :

* Python 3
* Windows 10
* MacOS
* Linux

## 3. Installing the program :
This program uses the following Python libraries :

```
asgiref 3.6.0
Django 4.2
djangorestframewor 3.14.0
djangorestframework-simplejwt 4.7.2
PyJWT 2.6.0
pytz 2023.3
sqlparse 0.4.3

```

## 4. Features :

### Access to data through endpoints that are divided into five categories : 

  * Registration/Login
  * Projects
  * Issues
  * Comments
  * Contributors

  For a detailed explanation of the API and its endpoints,
  consult the [**documentation**](https://documenter.getpostman.com/view/25420128/2s93ecwqUU).

## 5. Authentication and permissions :
    
  * The **authentication** for the back-end is handled by **JWT** (JSON Web Token).
  * For the **authorization** and **access** part, multiple **permissions** have been implemented 
depending on the status of the user performing the request :
    * Every user must be authenticated to access the data.
    * **Project** :
      * **Reading** and **creating** are permitted for all authenticated users. 
      * **Editing** and **deletion** are permitted only allowed for the author of the project.
      * **Reading** and **creating** are only allowed for the contributors of the project
      associated with this issue.
      * **Editing** and **deletion** are only permitted for the author of the project 
      and the issue.
    * **Comment** :
      * **Reading** and **creating** are only allowed for the contributors of the project.
      * **Editing** and **deletion** are only permitted for the author of the project and 
      the comment.

## 6. Running the program :

1. Open a terminal (e.g., Cygwin for Windows, the Terminal for Mac) or in an IDE (e.g., PyCharm).
2. Clone the repository into a local directory :
  > $<b> git clone repository path</b> 
3. Navigate to this folder in the terminal.
4. Create a virtual environment with :
  > $<b> python -m venv <nom de l'environnement></b> 
5.  Activate the virtual environment via :
  > $ <b>source env/bin/activate</b>  (on MacOS et Linux) 

  > $ <b>env\Scripts\activate.bat</b> (on Windows)
6. Install the packages listed in the requirements.txt file (this file is located in the project folder) with:
  > $ <b>pip install -r requirements.txt</b> 
7. Run the development server with:
> $ <b>python manage.py runserver</b>
8. Visit the site at the following address and access the different endpoints:
      **http://127.0.0.1:8000/**
---