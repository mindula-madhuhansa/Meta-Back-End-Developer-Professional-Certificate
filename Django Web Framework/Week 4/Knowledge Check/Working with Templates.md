1. Which of the following is the syntax used for ending a comment inside the Django Template Language?
    - [ ] `{ endcomment }`
    - [x] `{% endcomment %}`
    - [ ] `{% end comment %}`
    - [ ] `{% "endcomment" %}`
        > The Django syntax for beginning a comment is **{% comment ‘optional note’ %}**. The Django syntax **{% endcomment %}** is the right way to end a comment inside the template language.

2. True or False. In the code below, for the menu object passed inside the template, the syntax for the conditional statement used inside DTL tags is correct.<br/>
`{% if menu %}`<br/>
`First block of HTML content`<br/>
`{% else %}`<br/>
`Second block of HTML content`<br/>
`{% end if %}`<br/>
    - [ ] True
    - [x] **False**
        > The code ends with a tag for **endif** that has an improper syntax. The correct syntax is **{% endif %}**, where **endif** is a single keyword.

3. What will the correct syntax be for adding variables inside Django using the Django template language?
    - [ ] { }
    - [x] **{{ }}**
    - [ ] {% %}
    - [ ] {{ % % }}
        > The variables are enclosed inside double curly brackets.

4. The **csrf token** with the syntax **{% csrf_token %}** stands for Cross-site Request Forgery. What is it primarily used for?
    - [ ] The **csrf token** prepares Django to create Dynamic templates.
    - [x] **The **csrf token** informs Django that the page visited is secure.**
    - [ ] It's used for rendering templates using Django template language
        > It is a tag present that provides easy-to-use protection against attacks. When present, it signals Django that the page is safe.

5. True or False. The **{% include %}** tag imports the base template components in the child template.
    - [ ] True
    - [x] **False**
        > The definition above is for the **extends** keyword. **Include** is a keyword used when we load the template to be included in the current context. For example: **{% include "home.html" %}**.
