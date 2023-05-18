1. In the lab you completed, before you used the command to load static, you updated the **STATICFILES_DIRS** option with a value. Which of the following values is correct?
    - [ ] "myproject/static"
    - [x] "**myapp/static"**
    - [ ] "static"
        > The location of the static files in the lab you completed was inside the static directory of the 'myapp' directory.

2. In the lab you completed, you used the **render()** function inside the **views.py** file. Before using the render function, you must import it from a package. Which of the following import statements is correct?
    - [x] `from django.shortcuts import render`
    - [ ] `from django.contrib import render`
    - [ ] `from django.template import render`
        > The **django.shortcuts** package hosts the properties for the **render()** function.

3. In the lab you created. Which of the following is the correct syntax for adding a static image inside a Django template?
    - [ ] `<img  src={% static'img/grill.jpg' %}>`
    - [ ] `<img  src="{ static'img/grill.jpg' }">`
    - [x] `<img  src="{% static'img/grill.jpg' %}">`
    - [ ] `<img  src="{%'staticimg/grill.jpg' %}">`
        > The format inside the Django template that is used matches the required format for adding a static image inside the template.
