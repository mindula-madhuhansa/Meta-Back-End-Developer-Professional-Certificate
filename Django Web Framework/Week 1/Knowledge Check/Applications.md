1. Which of the following statements are true about a Django app? Select all that apply.
    - [ ] A Django app must have at least one model in it.
    - [x] **A Django app is reusable.**
        > A Django app can be installed in more than one project. An example is Django’s Admin app which can be a part of many projects.
    - [x] **There can be more than one app in a Django project.**
        > A single project may have one or more apps.
    - [ ] The app package folder contains a **settings.py** file where app-specific configuration is defined.

2. Can the startapp command be used with the django-admin utility?
    - [x] **Yes**
    - [ ] No
        > The startapp command option is available with Django-admin and the manage.py script.

3. Which of the following are features of a view? Select all that apply.
    - [ ] The view returns only an HTML response.
    - [x] **A view is mapped to a URL pattern.**
        > You need to specify which URL pattern invokes a particular view. This mapping is defined in the **urls.py** file of the app.
    - [x] **The request object is the mandatory argument for the view function.**
        > The view function receives the request command from the server context and processes the request data, namely parameters and the body.
    - [x] **A view is a user-defined function.**
        > It is a user-defined function in the **views.py** file under the app folder.

4. Which of the following statements about the **urls.py** file in the app folder is false? Select all that apply.
    - [x] **The **urls.py** in the apps folder is the same as **urls.py** in the project folder.**
        > Both are different. The app’s **urls.py** defines the URL mappings of the views in it. The **urls.py** of the project establishes the base URLs of the site.
    - [ ] The URL patterns in the app are defined with the path() function.
    - [ ] The **urls.py** file is not present in the app folder by default.
    - [x] **The **urls.py** file at the app-level is included in the urlpatterns list of the project.**
        > The URL definitions of the apps installed in the project must be included in the project-level **urls.py** file.

5. True or False. While working on multiple setting files in Django projects, django-admin is preferred over manage.py for running the Django commands in the command line.
    - [x] **True**
    - [ ] False
        > django-admin command is preferred in such cases as it allows you to give specific settings with the help of environment variable DJANGO_SETTINGS_MODULE
