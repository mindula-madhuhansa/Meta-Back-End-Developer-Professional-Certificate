1. Which are the necessary steps to follow to use DRF in your Django project? Choose all that apply.

   - [ ] Change your database to MySQL
   - [x] **Install the DRF package**
     > You need to install DRF in your Django project by applying the following command:<br/>`pipenv install djangorestframework`
   - [ ] Create a new Django app
   - [x] **Add DRF in the settings.py file**
     > Add rest_framework in the INSTALLED_APP section inside the settings.py file.

2. What are the advantages of using DRF? Choose all that apply.

   - [x] **Serializers**
     > Serializers are one of the biggest features of DRF. Serializers are used for converting model instances to native Python data types and to convert and map user input to the models effectively and efficiently.
   - [ ] Secures API endpoints automatically
   - [ ] Generate PDF files quickly
   - [x] **Browsable API view**
     > You can use Browsable API views and make GET, POST, PUT, PATCH and DELETE calls straight from the browser when you are using DRF.
   - [x] **CRUD Helpers**
     > DRF comes with different ViewSets and Generic classes to help you build functioning CRUD API endpoints with just a few lines of code.

3. You can use a single API endpoint for different HTTP methods.

   - [x] **True**
   - [ ] False
     > Using the API views and decorators, you can configure an API endpoint to accept multiple HTTP methods like **GET, POST, PUT, PATCH** and **DELETE**.

4. In the urls.py file, which of the following URL patterns is correct for a class-based view that extends the APIView class like this?
   `class BookView (APIView):`

   - [x] **`path('books',views.BookList.as_view())`**
   - [ ] `path('books',views.BookList.get())`
   - [ ] `path('books',views.BookList)`
     > You need to use as_view() after the class name to map it properly in the URL patterns.

5. If you automatically want to create a root API endpoint to display all your API endpoints in one place, which router class will you use?
   - [ ] RootRouter
   - [ ] SimpleRouter
   - [x] **DefaultRouter**
     > DefaultRouter comes with all the benefits of a SimpleRouter and creates a root API endpoint automatically.
