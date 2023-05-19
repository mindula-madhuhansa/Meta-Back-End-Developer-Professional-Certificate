1. In the lab you just completed, you created a folder called **partials** inside the **templates** folder. Inside the partials folder, you created a file called **_header.html**.<br/>This file required you to write code to load static content. Which of the following is the correct Django template language syntax needed to load static content on a web page?
    - [ ] `{{include static }}`
    - [x] `{% load static %}`
    - [ ] `{% include static %}`
    - [ ] `{{load static }}`
        > In a Django template tag, the load and static keywords are used to load static files. The location of the static files is defined in the **STATICFILES_DIRS** list in the **settings.py** file.

2. In the lab you completed, you worked with the file **base.html** to include the partial template **_header.html**. When adding the include tag to a template, which of the following statements is true. Select all that apply.
    - [x] **The include tag must be wrapped using the Django template syntax {% %}**
        > The **include** tag must be wrapped using the Django template syntax, e.g. **{% include 'partials/_header.html' %}**
    - [x] **If the partial template is located in a folder such as partials, the folder name must be passed with the template name.**
        > Normally the template name is relative to the template loader’s root directory. If you are passing the template name as a string argument, it must contain the relative path to the template. E.g. **{% include 'partials/_footer.html' %}**.
    - [x] **The template name can be passed as a string using single quotes.**
        > The template name can either be a variable or a hard-coded (quoted) string, in either single or double quotes.
    - [ ] The include tag must be placed inside block content **{% block content %}**.

3. In the lab you completed, you used the **extends** tag to extend the base layout (**base.html**).<br/>`{% extends 'base.html' %}`<br/>True or false. In the file **about.html**, you use the extends tag to signal that this template extends a parent template.
    - [x] **True**
    - [ ] False
        > The extends tag signals that this template extends a parent template. In the lab, the file **about.html** uses the extends tag with the value "**base.html**" as the name of the parent template to extend.
