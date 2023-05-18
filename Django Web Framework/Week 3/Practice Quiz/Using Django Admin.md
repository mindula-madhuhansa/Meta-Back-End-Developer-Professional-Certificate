1. In the lab you completed, you created a superuser using the Django shell. Which of the follow commands is correct to create a superuser using the Django shell.
    - [ ] `python3 manage.py createsuperusers`
    - [ ] `python3 manage.py "createsuperuser"`
    - [ ] `python3 manage.py create superuser`
    - [x] `python3 manage.py createsuperuser`
        > Superusers are created using the keyword createsuperuser.

2. In the lab you completed, the command line displayed several prompts when you ran the command to create a superuser. Which of the following prompts were displayed? Select all that apply.
    - [x] **Email**
        > The next prompt that appears after **Username** is **Email**. To continue, you must supply an email in a valid email format.
    - [x] **Password**
        > Django creates prompts for **password** and password confirmation. You must complete this before you can continue.
    - [x] **Username**
        > The first prompt that appears is the **Username**. Django displays a message stating that if you leave this option blank, it will create a default username based on the account name of your device.
    - [ ] Name

3. In the lab you completed, you created the superuser called **admin**. When you login into the admin panel, which of the following permission levels for the **admin** user are selected by default? Select all that apply.
![permission admin](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8153c110-6db0-4041-8cfa-d3b18b6011faimage1.png?expiry=1684540800000&hmac=Lvh_zjeXGCgs2AjolHA78lalWqGkAynBQKpifGf4LjQ)
    - [x] **Staff status**
        > That’s right, the superuser by default has access to the admin site in addition to modifying the permissions and their assignment.
    - [x] **Active**
        > That’s right, superuser status by default treats the user as Active.
    - [x] **Superuser status**
        > The superuser status is the highest privilege given to a user in Django and is selected by default for the user created using the keyword createsuperuser.

