# Assist-Capacity-Exchange-Development-Task-one

This is the first task for T346641: Assist Capacity Exchange Development, aimed at getting you familiar with the basic structure of the development of the Capacity Exchange platform.  Objective of the task: Create a Django project with an app called bug and commit it in GitHub.

## Prerequisites

- Python 3.x installed on your system.
- Django 4.x 

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

Access the Django admin panel by navigating to http://127.0.0.1:8000/admin in your web browser.

Log in with the superuser credentials you created earlier.
Once logged in, you'll see the "Bugs" section listed on the admin dashboard.

Click on "Bugs" to expand it, then click on "Add" to create a new bug.

Fill out the form with the bug's details, then click "Save" to register the new bug in the database.