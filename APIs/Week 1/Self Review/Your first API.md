1. In the lab you completed, you used **@csrf_exempt** as a decorator for the view **books()**. Which of the following is the correct statement to import the **csrf_exempt decorator**?

   - [x] **`from django.views.decorators.csrf import csrf_exempt`**
   - [ ] `from django.views.decorators import csrf_exempt`
   - [ ] `from django.decorators.csrf import csrf_exempt`
   - [ ] `from django.views import csrf_exempt`
     > The location of the **csrf_exempt** is inside the **csrf subpackage** placed inside the **django.views.decorators** package. **csrf_exempt** is used to bypass CSRF validation while generating Django templates.

2. Which of the following options below were updated as strings inside the configuration option **INSTALLED_APPS** in the **settings.py** file?

   - [ ] Book
   - [ ] BookList
   - [ ] rest_framework
   - [x] **BookListAPI**
     > The app **BookListAPI** needs to be registered to signal the use of the app **BookListAPI** for use inside the Django project.

3. Which of the following attributes were added inside the **models.py** file while creating the **Book** model? Choose all that apply.

   - [x] **title**
     > The **title** attribute was added to the Book model to specify the title of the book.
   - [x] **author**
     > The **author** attribute was added to the Book model to specify the name of the book’s author.
   - [x] **price**
     > The price attribute was added to the Book model to specify the price of the book.
   - [ ] indexes
