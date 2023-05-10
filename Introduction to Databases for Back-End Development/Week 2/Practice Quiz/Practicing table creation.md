1. Which of the following SQL syntax statements can you use to create a table? Select all that apply.
    - [x] **CREATE  TABLE table_name;**
    - [x] **create  table table_name;**
    - [ ] CREATE  TABLE  table  name;
    - [ ] CREATE table_name TABLE;
        > These are the valid CREATE TABLE syntax.

2. Select all steps to create a table in the database.
    - [x] **Use the CREATE TABLE command.**
        > This is the SQL command to create a table in the database.
    - [x] **Select a database.**
        > This step is very important as each table must belong to a specific database.
    - [x] **Write the table name.**
        > The table name must be specified in the SQL create table statement
    - [ ] Use the FROM keyword.
    - [x] **Define the columns of the table with relevant data types.**
        > This step is particularly important to ensure only required data is stored in the database.

3. Identify which of the following SQL statements can be used to create a table called “Products” for an online store. The table must contain two columns named “ID” and “Quantity.” The values within both columns must be whole numbers.

    - [x] **CREATE  TABLE products (ID INT, quantity INT);**
    - [ ] CREATE  TABLE products (ID CHAR, quantity VARCHAR);
        > This is the correct syntax to create the required table.

4. Which of the following SQL statements can be used to build a table that stores data about cell phone products?
    - [x] **CREATE  TABLE cell_phone<br/>(<br/>&emsp;name  VARCHAR(100),<br/>&emsp;productionDate DATE,<br/>&emsp;price DECIMAL<br/>);**
    - [ ] CREATE  TABLE cell_phone<br/>(<br/>&emsp;name  VARCHAR(),<br/>&emsp;productionDate DATE,<br/>&emsp;price DECIMAL<br/>);
        > This is the right syntax to create the cell phone product table.

5. You need to create a table called "Players". The table must contain two columns. The first column is called "playername" and holds the names of each player as a text data type. The second column is called "playerAge" and contains the age of each player as a whole number value. Identify the correct syntax to create this table.
    - [x] **CREATE  TABLE Players<br/>(<br/>&emsp;playerName VARCHAR(100),<br/>&emsp;playerAge INT<br/>);**
    - [ ] CREATE  TABLE Players<br/>(<br/>&emsp;playerName VARCHAR(100),<br/>&emsp;playerAge DECIMAL<br/>);
        > This is the right syntax to create the customers table in SQL.
