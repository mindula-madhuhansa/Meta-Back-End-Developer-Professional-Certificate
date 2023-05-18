1. In the lab you completed, you changed the settings inside the **settings.py** file to use MySQL instead of the default SQLite database.<br/>Inside the setting DATABASES, which of the following actions do you need to perform?
    - [ ] Add the MySQL settings above the settings for SQLite.
    - [ ] Add the MySQL settings below the settings for SQLite.
    - [x] **Replace the existing settings for SQLite with the settings for MySQL.**
        > Under the option for '**default**' in the list, you must replace the code containing the settings for the SQLite database with the code containing the settings for MySQL.

2. To configure a MySQL database to work with Django, you must run terminal commands in the shell to configure mysql credentials. Which of the following flags are valid for configuring mysql credentials? Select all that apply.<br/>Tip: Remember that a flag the format of -flag, e.g.**-m.**
    - [ ] -e
    - [ ] -P
    - [x] **-p**
        > You use the flag **-p** to specify the password of the MySQL account that you want to connect.
    - [x] **-u**
        > You use the flag **-u** to specify the user name of the MySQL account that you want to connect.

3. True or False. The settings you create for username and password inside the MySQL shell must match those inside the **settings.py** file. These settings are placed as "**USER**" and "**PASSWORD**" keys in the option for **DATABASES**.
    - [x] **True**
    - [ ] False
        > The options for username and password are matched inside the Django settings, and that is how Django can validate the database it will use.
