1. Consider the following code for the **urls.py** file at both the project level and the app level.<br/><br/>
**App-level urls.py:**<br/>
`urlpatterns = [`<br/>
&emsp;`path('home/', views.home, name="home"),`<br/>
`]`<br/><br/>
**Project-level urls.py:**<br/>
`urlpatterns = [`<br/>
&emsp;`path('little/', include('myapp.urls')),`<br/>
`]`<br/><br/>
Which URL do you need to type in the browser to load display the view function defined as **home**?
    - [ ] http://127.0.0.1:8000/little
    - [ ] http://127.0.0.1:8000/home
    - [ ] http://127.0.0.1:8000/home/little
    - [x] **http://127.0.0.1:8000/little/home**
        > The URL paths are mapped from project to app level, so the project level path will prefix the app level path.

2. In the lab you just completed, you worked in the **urls.py** file of an app called **myapp**. You needed to import the view module using the import statement.
Which of the following code snippets could you have used. Select all that apply.
    - [ ] `from myproject import views`
    - [ ] `from * import views`
    - [x] `from myapp import views`
        > The code **from myapp import views** implies importing the contents of the **views.py** file into the current urls.py file.
    - [x] `from . import views`
        > The dot (.) implies the current working directory and will successfully import the file **views.py** as it is in the same directory.

3. In the lab you just completed, you used the include() function in the project-level **urls.py** file. Which package is the include function imported from?
    - [x] You import the include() function from the django.urls package.
    - [ ] You import the include() function from the django.contrib package.
    - [ ] The include() function is present by default in the project level **urls.py** file and does not need to be imported.
        > The include() function along with the path() function are imported from the django.urls package.
