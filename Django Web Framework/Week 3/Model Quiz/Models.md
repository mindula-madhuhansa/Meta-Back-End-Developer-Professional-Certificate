1. The **sqlmigrate**  command generates the SQL query that will be executed when the migration is done.
    - [x] **True**
    - [ ] False
        > The **sqlmigrate** shows the text of the corresponding SQL query to be executed.

2. Which of the following sentences about the primary key is correct? Select all that apply.
    - [ ] The primary key attribute of the model should be an integer.
    - [x] **The primary key attribute of the model should not be null.**
        > A null value for the primary key is not allowed.
    - [x] **The primary key attribute of the model should be unique for each instance.**
        > For each instance of the model, the primary key's value must be unique.
    - [x] **The primary key attribute of the model can be a string.**
        > The data type of the primary key field can be a CharField or TextField.

3. To use MySQL with Django, what actions need to be taken?
    - [ ] Set 'USER': 'root'
    - [x] **Install mysqlclient**
        > The MySQL driver for Python must be installed.
    - [x] **Set 'ENGINE': 'django.db.backends.mysql'**
        > This enables MySQL to be used as the backend for the current project.
    - [ ] Set 'PORT': '8000'

4. Which of the following statements are about the **ForeignKey** type is correct? Select all that apply.
    - [x] **A field of the ForeignKey type is used to establish a many-to-one relationship.**
        > The ForeignKey attribute establishes a many-to-one relationship between two models.
    - [x] **A field of the ForeignKey type is used to establish a one-to-many relationship.**
        > The ForeignKey attribute establishes a one-to-many relationship between two models.
    - [ ] A field of the ForeignKey type is used to establish a many-to-many relationship.
    - [ ] A field of the ForeignKey type is used to establish a one-to-one relationship.

5. Which of the following built-in field types of a model stores numeric data? Select all that apply.
    - [x] **FloatField**
        > This field stores a number with a floating point.
    - [ ] URLField
    - [ ] CharField
    - [x] **IntegerField**
        > This field stores an integer.

6. The Django form is rendered in a tabular manner with a tag in the template. Identify the correct tag.
    - [ ] {{ form.as_div }}
    - [ ] {{ form.as_p }}
    - [x] **{{ form.as_table }}**
    - [ ] {{ form.as_ul }}
        > This tag renders the form as an HTML table.

7. Which of the following expressions extracts the data in the form submitted by the user?
    - [x] **request.POST**
    - [ ] request.GET
    - [ ] form.cleaned_data
    - [ ] form.is_valid
        > The view function retrieves the form data with this attribute of the request object.

8. Which of the following statements about a staff user is correct? Select all that apply.
    - [ ] A staff user cannot create a new user
    - [x] **A staff user cannot modify the permissions enabled for a user.**
        > The staff user has the privilege to be able to log in to the admin site.
    - [ ] A staff user can log in to the admin site
    - [x] **A staff user can create a group**
        > A user with staff privilege can create a group.

9. True or False. A superuser is allocated all permissions automatically to add, delete, and change the details of other users.
    - [x] **True**
    - [ ] False
        > The superuser indeed has access to all the permissions.

10. Which command option of the **manage.py** script is used to create an admin user for the Django admin site?
    - [ ] runserver
    - [x] **createsuperuser**
    - [ ] shell
    - [ ] createuser
        > The **createsuperuser** command creates a user with the given username.

