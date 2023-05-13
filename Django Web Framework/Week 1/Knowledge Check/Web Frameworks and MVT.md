1. Which of the following statements apply to a template in Django? Select all that apply.
    - [ ] A Django template returns a response to the client browser.
    - [x] **A Django template is an HTML document.**
        > A template is an HTML script and is saved with the .html extension.
    - [x] **A Django template can have blocks of template language syntax in between the HTML script.**
        > The variable content in the HTML script is marked by blocks of Django Template Language statements.
    - [x] **A Django template represents the presentation layer of the web application.**
        > The variable context data is filled inside the web page to render a good-looking response on the client browser.

2. Does a template in Django correspond to the view layer in MVC architecture?
    - [x] **Yes**
    - [ ] No
        > Django follows MVT architecture in which the template is a view layer corresponding to the view layer in MVC.

3. Which of the following statements about the **view()** function is correct. Select all that apply.
    - [ ] **The View function interacts with the model.**
        > It reads the parameters from the request object and performs CRUD operations on the model.
    - [ ] **The View function is invoked by the URL dispatcher.**
        > Django uses the **URLConf** to identify the view that matches with the pattern of the client URL
    - [ ] **The View function populates the template with context data.**
        > It uses the request parameters and/or the data fetched from the model to be inserted in the template.
    - [ ] **The View function returns a HTTP response to the client.**
        > It reads the template and returns it to the client as the response.

4. True or False. Django's view layer performs the role of the Application tier in the MVT architecture.
    - [x] **True**
    - [ ] False
        > A view interacts with both the model and template. It also defines processing logic. Therefore, it is like the application tier in MVT architecture.

5. Which of the following statements are true about the model in a Django application? Select all that apply.
    - [ ] It defines the processing logic.
    - [x] **It represents the data layer of the application.**
        > The model defines attributes and the relationships of data to be processed by the application.
    - [x] **It reflects the database structure.**
        > The migration process uses the attributes of a model class to create a table in the database.
    - [x] **It interacts with the view layer.**
        > The view coordinates with the model to perform database operations.
