1. Which of the following is NOT a setting configuration that is added inside the **DATABASES** option for MySQL?
    - [ ] HOST
    - [ ] PORT
    - [ ] ENGINE
    - [x] **URL**
        > The URL is configured using other options, such as **HOST** and **PORT** and will not have a specific option called URL.

2. Which of the following is an advantage of the SQLite database, which is installed and configured by default with Django projects?
    - [ ] SQLite database is comparable to MySQL in terms of scalability, making it quite popular.
    - [ ] SQLite database is serverless.
    - [ ] SQLite database does not have a user management system.
    - [x] **SQLite database is open source and does not require a license for personal use.**
        > The open source and licensing model of SQLite is the reason why anyone can use it without added investment.

3. Which of the follow databases provide support to easily integrate with the Django applications? Select all that apply.
    - [x] **MariaDB**
        > MariaDB is another database widely used in Django projects and applications.
    - [x] **MySQL**
        > MySQL is perhaps the most popular database used in Django projects that require scalability and user management.
    - [x] **SQLite**
        > The most common among the options listed is that SQLite is shipped by default with Django applications.
    - [x] **Postgres**
        > Postgres is an excellent option for integration with Django and one of the most widely used.

4. Which of the following is NOT an advantage of using the MySQL database? Select all that apply.
    - [ ] Open-Source
    - [ ] Scalable
    - [ ] Secure
    - [ ] **Enhanced debugging tools**
        > While MySQL has many advantages, the lack of an efficient debugging tool is generally considered to be a drawback while using MySQL.
    - [ ] **Lightweight**
        > MySQL has plenty of configuration options but is not considered a lightweight database. SQLite databases used in Django qualify as lightweight.

5. Inside the **DATABASES** option while configuring the connection for MySQL inside the **settings.py** file, which of the following optional parameters can be added that will set **Initial command to issue to the server upon connection**?
    - [ ] HOST
    - [x] **init_command**
    - [ ] sql_mode
        > The **init_command** is an optional parameter that will set **Initial command to issue to the server upon connection**.
