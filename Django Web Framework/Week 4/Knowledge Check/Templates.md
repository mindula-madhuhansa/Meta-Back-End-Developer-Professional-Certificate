1. Which of the following configurations inside the **settings.py** file need to be enabled and set to **True** for Django to search for templates inside the subdirectory named **TEMPLATES**?
    - [ ] ALLOWED_HOSTS
    - [ ] **APP_DIRS**
    - [ ] STATIC_URL
    - [ ] BASE_DIR
        > The settings for **APP_DIRS** inside **TEMPLATES** within the **settings.py** file need to be set to the value **True** for Django to enable the search for templates.

2. Complete this sentence. Code re-usability in Django is undertaken with the help of partial templates. This is known as _____________________________
    - [ ] Template Language
    - [x] **Template Inheritance**
    - [ ] Template Polymorphism
        > Django uses partial templates for undertaking template inheritance, where code blocks can be reused in other templates.

3. Suppose you are using Django Template Language and you need to count the number of items in a list. Which filter can you use?
    - [ ] slice
    - [ ] first
    - [ ] wordcount
    - [x] **length**
        > As the name suggests, the **length** filter works with the list and returns the count of items inside it.

4. Which of the following arguments can be passed to the **render()** function inside the **views.py** file? Select all that apply.
    - [x] **The relative path to the template**
        > The relative path of the template is passed inside the **render()** function that tells Django where the view function needs to be rendered.
    - [x] **A dictionary of variables to be passed inside the template**
        > The variables inside the template can be passed in a dictionary object inside the **render()** function.
    - [ ] The HttpResponse object
    - [x] **The request object**
        > A request object is typically used to build the **context**. **Context** is the translation of objects in a Django readable string format.

5. True or False. Django template language mainly consists of the following components: **Tags**, **Filters**, **Comments**, and the **Template Engine**.
    - [ ] True
    - [x] **False**
        > The statement is not true because the template engine is not a part of the template language but a support in Django middleware that bridges the gap between Python and HTML. The fourth component type is called **Variables**.
