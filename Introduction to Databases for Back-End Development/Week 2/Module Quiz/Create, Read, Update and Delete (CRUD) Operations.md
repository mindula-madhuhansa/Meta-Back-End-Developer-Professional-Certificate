1. The following SQL clause creates a table named staff within a database:<br/><br/>CREATE staff TABLE;<br/><br/>
    - [ ] True
    - [x] **False**
        > The table name should be written after the TABLE keyword.

2. The following SQL statement creates a table named staff, with two columns called name and address:<br/><br/>CREATE TABLE staff (name VARCHAR(100), address VARCHAR(100));<br/><br/>
    - [ ] False
    - [x] **True**
        > This is the right syntax to create the staff table with name and address columns in SQL.

3. What is the SQL command to add a new record of data in the staff table?
    - [ ] INSERT staff INTO;
    - [ ] ADD INTO staff;
    - [x] **INSERT INTO staff;**
        > The INSERT INTO command is used to insert new records in a table.

4. Which is the right command syntax to update the staff table in SQL?
    - [x] **UPDATE staff;**
    - [ ] UPDATE Table staff;
        > This is the right way to use the UPDATE command.

5. EDIT command is used to modify data in a database table.
    - [x] **False**
    - [ ] True
        > The UPDATE command is used to modify data in the database.

6. Which one of the following SQL statements updates the staff email address for the individual named “Karl” in the staff table?
    - [ ] UPDATE staff WHERE ID = 16 SET email = 'Karl@email.com';
    - [ ] UPDATE staff SET name = 'Karl@email.com' WHERE email = 'Karl';
    - [x] **UPDATE staff SET email = 'Karl@email.com' WHERE name = 'Karl';**
        > This is the right syntax to update the staff email in the staff table.

7. Select the right keyword to complete the missing part of the following statement:
    - [x] **VALUES**
    - [ ] DATA
        > VALUES is the correct SQL keyword to use here to insert a new record in the staff table.

8. A staff table consists of three columns called name, email and age. Which of the following SQL statements selects all available data in all three columns in the staff table?<br/>Select all correct answers.
    - [x] **SELECT * FROM staff;**
    - [ ] SELECT name, email AND age FROM staff;
    - [x] **SELECT name, email, age FROM staff;**
        > You can use this syntax to select all the columns available in the staff table.

9. The following SQL statement returns all staff phone numbers from the staff table:<br/><br/>SELECT phoneNumber FROM staff;<br/><br/>
    - [ ] False
    - [x] **True**
        > This is the right SQL statement to return the staff phone numbers.

10. Which of the following SQL statements deletes all records of data from the staff table without deleting the table itself?<br/>Select all correct answers.
    - [x] **DELETE FROM staff;**
    - [ ] DROP TABLE staff;
    - [x] **TRUNCATE TABLE staff;**
        > This SQL statement deletes the data inside the customers table, but not the table itself.
