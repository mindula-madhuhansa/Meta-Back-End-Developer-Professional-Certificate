1. In the lab you completed, you worked with the for template tag to loop over each item of an array, making the item available in a context variable. Which of the following code snippets to implement the for template tag is correct?
    - [x] `{% for item in menu %}`<br/>
`<h2>{{ item.name }}</h2>`<br/>
`{% endfor %}`<br/>
    - [ ] `{% for item in menu.menu %}`<br/>
`<h2>{{ item.name }}</h2>`<br/>
`{% endfor %}`
    - [ ] `{% for item in menu.menu %}`<br/>
`<h2>{{ item.name }}</h2>`<br/>
`{% end for %}`<br/>
    - [ ] `{% for item in menu.menu %}`<br/>
`<h2>{{ item.name }}</h2>`<br/>
        > The iteration is performed over the menu object directly and the necessary syntax for the template language is added.

2. What will be the correct syntax for the piece of code which will add a condition to check if the **menu** dictionary items are present inside the template?
    - [ ] `{% if 'menu' %}`
    - [ ] `{ if menu }`
    - [x] `{% if menu %}`
        > The piece of code will iterate till all the menu items present inside the menu object are covered.

3. In the lab you completed, you worked with the **Menu** model to create an object from the database by constructing a **QuerySet**.<br/>True or false. You can use the **all()** method to return a **QuerySet** of all the objects in the database.And, you can refine the initial **QuerySet** by adding filter conditions.
    - [x] **True**
    - [ ] False
        > The **QuerySet** returned by the **all()** method describes all objects in the database table. If you need to select only a subset of the complete set of objects, you can refine the initial **QuerySet** by adding filter conditions such as **filter** and exclude.
