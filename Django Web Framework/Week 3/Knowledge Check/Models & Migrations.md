1. True or False. The **on_delete** property in the **ForeignKey** field determines the action to take if the corresponding primary key in the related table is deleted.
    - [x] **True**
    - [ ] False
        > The **on_delete** option decides the action's nature when the corresponding primary key is deleted.

2. Complete the following sentence. If multiple objects of one model can be associated with multiple objects of another model, it is the case of a _________________.
    - [ ] One-to-many relationship
    - [ ] One-to-one relationship
    - [x] **Many-to-many relationship**
    - [ ] Many-to-one relationship
        > The above statement applies to the many-to-many relationship.

3. Which of the following statements about the **makemigrations** command is true? Select all that apply.
    - [ ] The **makemigrations** command executes the **migration** script.
    - [x] **The makemigrations command creates new migrations based on the changes in the model definitions.**
        > The **makemigrations** command prepares the script for the migrate command.
    - [x] **The makemigrations command helps with version control.**
        > The subsequent **makemigrations** commands create numbered **migration** scripts, so it is possible to fall back to the earlier database structure.
    - [ ] The **makemigrations** command creates a table in the database.

4. Suppose you create an app called **myapp** and a model called **Users**. When you run the **migrate** command to create a table in the database, what will Django automatically name this table?
    - [ ] Django automatically names this table with the name of the model.
    - [ ] Django does not automatically name this table. The table name must be specified using the **migrate** command.
    - [x] **Django automatically names this table using the app name and model name separated by an underscore, for example **myapp_users**.**
    - [ ] The name of the table is auto-numbered from 0001 onwards.
        > The database table name follows this format of appname, followed by an underscore, followed by the model name, all in lowercase.

5. Complete the following statement. The **showmigrations** command ______________.
    - [ ] shows the Migration class generated by **makemigrations**.
    - [x] **shows the pending migrations.**
    - [ ] shows the SQL script of migrations to be done.
    - [ ] shows the name of the table created.
        > The command shows the migrations that have been done and those that are pending.
