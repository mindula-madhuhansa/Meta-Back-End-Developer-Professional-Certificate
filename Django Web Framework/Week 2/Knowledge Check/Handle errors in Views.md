1. True or False. To display a standard error message, you should set DEBUG=False in the **settings.py** file.
    - [x] **True**
    - [ ] False
        > When the DEBUG variable is set to True, you get the traceback, showing the trail of errors encountered by the application. Change it to False, so that the standard error is displayed.

2. What is the meaning of an HTTP response with a 404 status code?
    - [ ] The access is forbidden.
    - [ ] The user is not authorized.
    - [x] **The requested page is not found.**
    - [ ] The request is not completed.
        > HTTP status code 404 is defined to indicate that there is no view mapped to the client’s URL.

3. In which module is the **HttpResponseNotFound** class defined?
    - [ ] django.exceptions module
    - [ ] django.urls module
    - [ ] django.core.exceptions module
    - [x] **django.http module**
        > This class is similar to **HttpResponse**, but with status code = 404.

4. When is the **PermissionDenied()** exception raised?
    - [ ] The user is not authorized.
    - [x] **The user doesn't have the required permission enabled.**
    - [ ] The requested object is not found.
    - [ ] The view doesn't exist.
        > It is raised when the user doesn’t have the required permission on the model under process.

5. Can you override the default error views defined in the **django.views.default** module?
    - [x] **Yes**
    - [ ] No
        > You can override them by specifying the appropriate handler in the project’s **URLConf**.
