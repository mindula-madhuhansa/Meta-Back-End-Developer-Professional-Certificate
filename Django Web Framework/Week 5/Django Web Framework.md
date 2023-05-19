1. Which one of the following network configurations does NOT need to be provided explicitly to the web framework to establish a connection with an external database such as MySQL?
    - [ ] Address
    - [x] **Database version**
    - [ ] Database name
    - [ ] Port
        > While the configurations for the Database version may be passed internally, we do not need to provide the Database version explicitly to the web framework to establish a connection with the database.

2. Which of the following tags in the Django template language are relevant to the Template Inheritance? Select all that apply.
    - [ ] csrf_token
    - [ ] static
    - [x] **include**
        > Include tag is used to render sub-templates along with the HTML.
    - [x] **extends**
        > The extends tag allows you to replace blocks or content from a parent template.

3. If you run the code below, what will the generated output be for the specified view on the web page?<br/>
`def home(request):`<br/>
`...`<br/>
`return HttpResponse("Hello")`<br/>
`return HttpResponse("World")`<br/><br/>
    - [ ] World
    - [x] **Hello**
    - [ ] Hello World
        > Django will use the first return statement and step out of the function.

4. Which one of the following statements is correct?
    - [ ] A Django project can contain only one view and multiple apps.
    - [ ] A Django project can contain only one view and app per project.
    - [x] **A Django project can contain multiple views and multiple apps.**
    - [ ] A Django project can contain multiple views and only one app.
        > Theoretically, we can create as many apps in a project and views in an app as we like!

5. Which one of the following is NOT a command that can be executed in the command line using the script **manage.py**?
    - [ ] runserver
    - [x] **settings**
    - [ ] showmigrations
    - [ ] shell
        > While settings for Django can be accessible from the file **settings.py**, there is no such command declared for the keyword **settings** inside the script of **manage.py**.

6. When performing migrations, what is the expected output produced if you run the following query on the command line?<br/>
`python3 manage.py sqlmigrate`<br/><br/>
    - [ ] It will show the operations and dependencies performed in migrations.
    - [x] **It will show the SQL queries run during the migrations.**
    - [ ] It will run the SQL queries required to perform migrations.
        > SQL queries in earlier migrations are displayed that show translations that ORM has performed from the command executed inside Django. The queries are not executed separately when you execute the command using **sqlmigrate**.

7. Which of the following are the built-in path converters used for URL configuration in Django? Select all that apply.
    - [ ] boolean
    - [ ] float
    - [x] **slug**
        > Slug matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters.
    - [x] **str**
        > Str matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn't included in the expression.
    - [x] **path**
        > Path matches any non-empty string, including the path separator, '/'.

8. What special character matches zero or more characters while using Regular Expressions?
    - [x] ***(star)**
    - [ ] #(hash)
    - [ ] ^(caret)
    - [ ] +(plus)
        > The star (*) character will match all strings containing zero or more characters of the type defined.

9. Using the helper function in Django, which of the following is valid code to create a new user in Django?<br/>**Note**: **mario** is the username, **pass@123** is the password and **mario@littlelemon.com** is the email address.
    - [ ] `User.objects.create_user('mario', 'pass@123', ' mario@littlelemon.com ')`
    - [ ] `User.objects.create_user('mario@littlelemon.com ', 'mario', 'pass@123')`
    - [x] `User.objects.create_user('mario', 'mario@littlelemon.com', 'pass@123')`
    - [ ] `Mario.objects.create_user('mario@littlelemon.com ', 'pass@123')`
        > The appropriate order of passing arguments inside the **create_user()** function is username, email and password.

10. What are the advantages of using the built-in SQLite database with Django?
    - [ ] Security and authentication
    - [ ] Scalability
    - [x] **Suitable for small, low-risk projects**
        > SQLite is lightweight and has sufficient features to meet the requirements of small projects.
    - [x] **Rapid prototyping**
        > Since SQLite is a lightweight database, it can be used for rapidly creating prototypes without spending much time establishing additional connections.
