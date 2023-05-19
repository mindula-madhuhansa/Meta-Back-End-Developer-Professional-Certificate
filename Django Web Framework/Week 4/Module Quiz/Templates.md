1. Which of the following sentences about templates are true? Select all that apply.
    - [x] **A template is a web page that has blocks of template language syntax inside the HTML script.**
        > The blocks of Django Template Language render dynamic content on the web page.
    - [ ] A template extracts the data from a model and generates a dynamic page.
    - [x] **A template helps to include conditional processing logic in a web page.**
        > The **{% if %}** tag allows a conditional logic to be put in the HTML script.
    - [ ] A template is the data layer of the application.

2. The view function loads a template and fills the context data in it.
    - [x] **True**
    - [ ] False
        > The view function loads the template by calling the **render()** function.

3. Which of the following tags are used for implementing template inheritance? Select all that apply.
    - [x] `{% extends %}`
        > The **{% extends %}** tag uses the named template as the base template.
    - [ ] `{% include %}`
    - [x] `{% block %}`
        > The **{% block %}** tag marks the inheritable content in the parent template.
    - [ ] `{% endfor %}`

4. True or false. To implement template inheritance, the parent template must have the name **base.html**.
    - [ ] True
    - [x] **False**
        > The parent template may have any name and must be used in the **{% extends %}** tag of the child template.

5. In which module is the **render()** function defined?
    - [ ] django.urls
    - [x] **django.shortcuts**
    - [ ] django.db
    - [ ] django.contrib
        > The **render()** function is defined in the **django.shortcuts** module.

6. Which of the following template filters returns a **titlecase** representation of a string?<br/>**Hint:**  **titlecase** makes words start with an uppercase character and the remaining characters lowercase.
    - [ ] upper
    - [ ] lower
    - [x] **title**
    - [ ] length
        > The title tag returns the titlecased string.

7. Putting one loop inside another is called nesting of loops. Can you use nested loops in a template?
    - [x] **Yes**
    - [ ] No
        > Nested for loops can be used in a template.

8. Complete the sentence. The view function passes a ______ as the context data to a template.
    - [ ] Python list
    - [ ] Python string
    - [x] **Python dict**
    - [ ] Python tuple
        > The context passed to the template must be a **dict** object.

9. What are the advantages of a class-based view? Select all that apply.
    - [x] **Code re-usability**
        > Class-based views implement the DRY principle.
    - [x] **Extensible code**
        > With the principle of class inheritance, class-based view functionality can be extended.
    - [ ] Class-based views are simple to implement
    - [ ] Implicit code flow

10. Suppose that a Django app named **myapp** has the Employee model. Which of the following statements about the generic **ListView** class are correct? Select all that apply.
    - [x] **A generic **ListView** class must be named **EmployeeList****
        > The class name is made up of the model's name appended by the generic view name.
    - [ ] A generic ListView class should set the model attribute to **myapp_Employee**
    - [x] **A generic **ListView** class lists all the rows in the Employee table**
        > The ListView is used to render the list of all records in a table.
    - [x] **A generic **ListView** class needs a template named EmployeeList.html**
        > The template with the name <name-of-model>List.html should be available in the templates folder.
