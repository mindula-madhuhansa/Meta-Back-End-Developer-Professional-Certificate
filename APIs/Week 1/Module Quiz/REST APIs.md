1. What are the benefits of using pipenv? Choose all that apply.

   - [ ] It makes your project run faster
   - [x] **It creates a virtual environment for your project**
     > Pipenv automatically creates a virtual environment and installs all the dependencies inside it.
   - [ ] It makes your project more secure
   - [x] **It manages the dependencies**
     > Using pipenv you can manage the dependencies for your project.

2. What is the default port number used by Django webserver?

   - [ ] 8001
   - [x] **8000**
   - [ ] 443
     > 8000 is the default port number used by the Django webserver when you apply this command python manage.py runserver inside a Django project directory.

3. What does the following command do?
   `python manage.py startapp`

   - [ ] It creates a Django project
   - [x] **It creates a new Django app**
   - [ ] It installs Django
     > You can use this command inside a Django project to create a new Django app following the application name. If your app name is LittleLemonAPI, then you will have to apply this command python manage.py startapp LittleLemonAPI

4. Authentication and authorization are the same thing.

   - [ ] True
   - [x] **False**
     > Authentication and authorization are different things, and they play a very important role in securing your project. Authentication checks if the user can enter the system, and authorization checks if the authenticated user has the appropriate privilege to perform a task.

5. Which of the following HTTP status codes are used to indicate client-side and server-side errors? Choose all that apply.

   - [x] **503 - Service Unavailable**
     > This code is used when the server is down or cannot handle the request due to overloading.
   - [x] **403 – Forbidden**
         This code is used when client credential like the username and password, or the token is not valid.
   - [x] **404 Not Found**
     > This code is used when someone requests a non-existing item.
   - [ ] 301- Moved Permanently
   - [ ] 201 - Created

6. What are the valid **Accept** headers for requesting XML content? Choose all that apply.

   - [x] **application/xml**
     > A client can send the Accept: application/xml header to request XML content from the server.
   - [ ] code/xml
   - [x] **text/xml**
     > This is a valid header for requesting XML content from the server.
   - [ ] application/x-xml
   - [ ] application/xml-content

7. What can lead to data corruption in an API project? Choose all that apply.

   - [ ] Lack of caching
   - [x] **Lack of authorization**
     > The lack of a solid authorization layer can lead any user with a valid authentication token to access any API endpoints and they will be able to modify the data.
   - [x] **Lack of authentication**
     > Without authentication anyone can get in and modify the data.
   - [ ] Lack of throttling
   - [x] **Lack of data validation and sanitization**
     > Incorrect or malformed data may be stored in the database without proper data validation. Lack of sanitization can create security threats which can also corrupt the data.

8. Which of the following statements are valid for Insomnia? Choose all that apply.

   - [x] **It’s a REST API Client**
     > You can use Insomnia to make HTTP requests.
   - [x] **Insomnia can send different types of payloads**
     > While making an API call, you can send different types of payloads like JSON, Form URL Encoded Data using Insomnia.
   - [ ] Insomnia has a mobile client
   - [ ] Insomnia has a command line tool
   - [x] **Insomnia is cross-platform**
     > You can download Insomnia for multiple operating systems like Windows, macOS and Linux.

9. Which of the following API clients/tools has both web and desktop versions?

   - [ ] Curl
   - [ ] Insomnia
   - [x] **Postman**
     > Postman comes with a desktop app and offers a web version that can be used in your browser to make API calls.

10. What is the purpose of renderer classes in DRF?

    - [ ] Convert model instance to native Python data types
    - [ ] Quickly scaffold a CRUD API project
    - [x] **Convert serialized data to display as HTML, XML and JSON**
      > DRF comes with a few built-in renderer classes to convert serialized data and display it in various formats. You can also use third-party renderers in DRF.
