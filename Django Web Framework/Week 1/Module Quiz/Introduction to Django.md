1. Which of the following are some of the differences between the commands django-admin and manage.py? Select all that apply.
    - [ ] There is no difference between **django-admin** and **manage.py**.
    - [x] **manage.py is more convenient to use than django-admin.**
        > **manage.py** runs inside the project folder. When using **django-admin**, you must set **--settings** variable to the required project's settings.py file.
    - [x] ****django-admin** is installed in the Python environment when you install Django with PIP utility. The **manage.py** file is created inside each Django project folder.**
        > You will find **manage.py** in the project folder and **django-admin** in Python’s scripts folder
    - [x] ****django-admin** is a command-line utility and **manage.py** is a Python script.**
        > **manage.py** should be run as a Python module. The **django-admin** is an executable file that is run in the terminal.

2. The **urls.py** file is present in the project package and the app package.
    - [x] **True**
    - [ ] False
        > The **urls.py** in the project folder defines the **URLConf**. The app’s **urls.py** is included in the project’s **urlpatterns** list.

3. What happens when the view function created inside the **views.py** file is modified while the development server is still running?
    - [ ] The webpage in the browser is automatically reloaded to reflect the new changes.
    - [ ] The development server will terminate.
    - [ ] The server will need to be restarted manually to reflect new changes.
    - [x] **The development server will automatically reload and changes will reflect on webpage reload.**
        > You will be able to see the changes server reload in the command prompt once you save the **views.py** file. On manually reloading the webpage, the new changes will be reflected.

4. Where is the **manage.py** file located?
    - [ ] Inside the project package folder
    - [ ] Inside the app package folder
    - [ ] Inside the scripts folder of the current Python environment.
    - [x] **Inside the project's outer container folder**
        > In the outer project folder, you’ll find the **manage.py** script along with the app package and the project package.

5. By default, Django's built-in development server runs on the local machine with IP address 127.0.0.1 and port 8000.
    - [x] **True**
    - [ ] False
        > The **runserver** command option for **django-admin** and manage.py starts the development server and listens to the incoming requests on port 8000 of the localhost by default.

6. Does the View layer in Django correspond to the View layer in MVC architecture?
    - [ ] Yes
    - [x] **No**
        > Django’s view layer performs the role of Controller in MVC architecture.

7. Which of the following statements is true about the view function? Select all that apply.
    - [x] **Interacts with the model layer**
        > The view performs the CRUD operations on the models.
    - [x] **Returns a response to the client**
        > The view does return a **HttpResponse** to the client.
    - [x] **Receives the request object from the server.**
        > The view function receives the request object from the server context.
    - [x] **Loads the template**
        > The view loads a template, fills the context data, and returns it to the client browser.

8. Which of the following statements are true about a model in Django? Select all that apply.
    - [ ] The Model defines the processing logic of the Django application.
    - [ ] A Django Template fetches the data from a Model and displays it on a web page.
    - [x] **A model is a Python class**
        > A model class represents a database table structure.
    - [x] **Model class attributes are used to create a database table.**
        > Django performs migration to construct a database table from the model attributes.

9. Which Python module is used from the command-line to create a virtual environment?
    - [ ] startapp
    - [ ] shell
    - [ ] pip3
    - [x] **venv**
        > The Python virtual environment is created with the command **python –m venv envname**.

10. Which of these pre-built apps are installed in a Django project by default? Select all that apply.
    - [x] **django.contrib.messages**
    - [x] **django.contrib.admin**
    - [ ] postgress app
    - [x] **django.contrib.auth**
        > These apps are added in INSTALLED_APPS by default.
