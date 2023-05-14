1. Which of the following syntax is valid when using the **path()** function? Select all that apply.
    - [x] `path('login/', views.login)`
        > The urlpatterns contain a list of path objects. The path() function’s two mandatory arguments are the URL pattern string and the view function.
    - [x] `path('login/', views.login, name='login')`
        > The path() function may have an optional argument for the URL name. The first two arguments to this function are the URL pattern string and the path to the view function. You can pass name as a third optional argument for the URL name.
    - [ ] `path('login/', name='login')`
    - [ ] `path(views.login, 'login/')`

2. True or False. The view function calls the **render()** function to load a template and returns its response to the client.
    - [x] **True**
    - [ ] False
        > The **render()** function loads the template, populates the context data, and sends the function’s return value as a response.

3. True or False. The correct syntax to import the **path()** function in the **urls.py** file is **from django.urls import path**.
    - [x] **True**
    - [ ] False
        > The **path()** function should be imported from the **django.urls** module.

4. Yes or No. Is it mandatory to define views in the **views.py** file?
    - [x] **Yes**
    - [ ] No
        > It is not necessary to define views in a file named **views.py** to store view functions, although it is a common practice. You can use any file name, but ensure that it is imported into the **urls.py** file when updating the **urlpattern** list.

5. Which of the following statements about the  **include()**  function is true. Select all that apply.
    - [ ] The **include()** function includes, in the URL patterns, the URL mapping to a view function.
    - [x] **The **include()** function is defined in the **django.urls** module.**
        > This function is imported from this module into the urls.py file in the project’s package folder.
    - [x] **You should pass a string representing the path of the app's urls module to the **include()** function.**
        > The string argument should be the path to the app’s urls module. For example: include('myapp.urls').
    - [x] **The **include()** function is used to include the URL pattern definitions of an app in the project.**
        > It updates the project’s URL pattern list by including the pattern list of an app.
