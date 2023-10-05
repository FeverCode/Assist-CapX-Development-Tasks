# Assist-Capacity-Exchange-Development-Task-one

This is the first task for T346641: Assist Capacity Exchange Development, aimed at getting you familiar with the basic structure of the development of the Capacity Exchange platform.  Objective of the task: Create a Django project with an app called bug and commit it in GitHub.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Setup (Continuation) Second Task for T346641](#setup-continuation-second-task-for-t346641)
- [Usage (Continuation) Second Task for T346641](#usage-continuation-second-task-for-t346641)
- [Setup (Continuation) Third Task for T346641](#setup-continuation-third-task-for-t346641)
- [Usage (Continuation) Third Task for T346641](#usage-continuation-third-task-for-t346641)


## Prerequisites

- A computer running either Windows, MacOS or Linux.
- [Python 3.x](https://www.python.org/downloads/) installed on your system.
- [Django 4.x](https://www.djangoproject.com/download/) installed on your system.
- Basic knowledge of Python and Django.
- A GitHub account and basic knowledge of Git.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/FeverCode/Assist-Capacity-Exchange-Development-Task-one.git

2. Navigate to the project directory:

    ```bash
    cd Assist-Capacity-Exchange-Development-Task-one

3. Create and activate a virtual environment (venv) to 
    isolate project dependecies:     
    
    ```bash
    python -m venv venv
    
    source venv/bin/activate

4. Install the required Python packages:

    ```bash
    pip install -r requirements.txt

## Usage

* To run the project, execute the following command:

    ```bash
    python manage.py runserver
    ```

* Open the project on your broswer on http://127.0.0.1:8000/

## Setup (Continuation) Second Task for T346641
1. Structuring the Database:

* We have now created our models, we'll need to create a database schema.
* This is done by running migrations which tells django how to store our data.

* Run the following command to generate a migration file:

    ```bash
    python manage.py makemigrations
    ```
* Run the following command to apply the migration:

    ```bash
    python manage.py migrate
    ```
* Create a superuser for accessing the admin panel:

    ```bash
    python manage.py createsuperuser
    ```
* You will be prompted to enter a username, email address (optional), and a password. Remember these credentials as you'll use them to log into the admin panel.

* Now, run the development server again (if it's not already running):

    ```bash
    python manage.py runserver
    ```
## Usage (Continuation) Second Task for T346641

* Access the Django admin panel by navigating to http://127.0.0.1:8000/admin in your web browser.

* Log in with the superuser credentials you created earlier.
Once logged in, you'll see the "Bugs" section listed on the admin dashboard.

* Click on "Bugs" to expand it, then click on "Add" to create a new bug.

* Fill out the form with the bug's details, then click "Save" to register the new bug in the database.

## Setup (Continuation) Third Task for T346641
1. Creating Views and Templates:
    * We have created views to register a new bug, view a specific bug, and list all registered bugs.
    * Corresponding templates have been created to provide a user interface for these views.

2. URL Configuration:
    * URL patterns have been added to `urls.py` to map URLs to the new views.
    
3. Form for Bug Registration:
    * A `forms.py` file has been created with a `BugForm` class to handle the form submission for bug registration.

## Usage (Continuation) Third Task for T346641
* To register a new bug, navigate to http://127.0.0.1:8000/ in your web browser.

* Fill out the form with the bug's details, then click "Submit" to register the new bug.

* To view the list of registered bugs, navigate to http://127.0.0.1:8000/bugs in your web browser.

* Click on a bug to view its details.
    To view the details of a specific bug, navigate to http://127.0.0.1:8000/bug/<bug_id> in your web browser, replacing <bug_id> with the ID of the bug you want to view.
