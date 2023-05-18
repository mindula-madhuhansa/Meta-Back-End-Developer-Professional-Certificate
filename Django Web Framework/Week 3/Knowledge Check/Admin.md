1. Which of the following actions can be performed using Django Admin in the browser? Select all that apply.
    - [ ] Configure URLs for specific views
    - [x] **Add and update Django administrative users**
        > We can add, update and delete new users using the Django admin panel.
    - [x] **Set user permissions for Django users**
        > Permissions can be added and revoked for users created for the Django project.
    - [ ] Change configuration settings for the Django project

2. What is the default URL for the Django admin panel?
    - [x] [**http://127.0.0.1:8000/admin/**](http://127.0.0.1:8000/admin/)
    - [ ] [http://127.0.0.1:8000/adminuser/](http://127.0.0.1:8000/adminuser/)
    - [ ] [http://127.0.0.1:8000/administrator/](http://127.0.0.1:8000/administrator/)
    - [ ] [http://127.0.0.1:8000/adminsuperuser/](http://127.0.0.1:8000/adminuser/)
        > The URL has the suffix **admin** by default, with settings inside the Django project that can be changed.

3. True or False. When creating a user from the command line, you can define a weak password by bypassing the password validation. However, if you perform this action using the Django admin panel in your browser, you must define a strong password.
    - [x] **True**
    - [ ] False
        > The password validation can be bypassed when Django prompts a message such as “Bypass password validation and create user anyway? [y/N]:” and then selects “y” as a choice that stands for Yes.

4. Which of the following types of users are listed under Permissions in the Django admin panel? Select all that apply.
    - [x] **superuser**
      > The active option is under the permission level for users inside the Django admin panel.
    - [x] **Active**
        > The Active option is under the Permission level for users inside the Django admin panel.
    - [x] **Staff**
        > The Staff option is under the Permission level for users inside the Django admin panel.
    - [ ] Inactive

5. True or False. Django users are assigned permissions. Over and above this, you can customize permissions for specific models, views, and templates.
    - [x] **True**
    - [ ] False
        > Django can customize permissions for models, templates and views individually.
