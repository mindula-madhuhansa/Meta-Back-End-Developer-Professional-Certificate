1. The following SQL statement contains the syntax to create a product table with two columns ID and price:<br/><br/>CREATE TABLE product_table (ID, price);<br/><br/>
    - [ ] True
    - [x] **False**
    > This SQL statement does not define which data types must be assigned to each column.

2. You need to create a table for bank account records in a financial database. Which of the following SQL statements can you use to complete this task?
    - [x] **CREATE TABLE bank_account (account_number INT, balance DECIMAL);**
    - [ ] CREATE ENTITY bank_account (account_number INT, balance DECIMAL);
        > This is the right syntax to create the bank account table in SQL.

3. Select the right SQL statement to insert a new record of data into three columns of a table called "Games" with the following values:<br/><br/>GameID = 1, gameDate = 2022-10-10 and score = 3<br/><br/>
    - [x] **INSERT INTO games (GameID, gameDate, score) VALUES (1, “2022-10-10”, 3);**
    - [ ] INSERT INTO games (GameID, gameDate, score) CONSTRAINT (1, “2022-10-10”, 3);
        > This is the right SQL INSERT INTO statement to insert the new record of data.

4. A player with ID = 5, name = “Tina” and age = 23 must be added to the “Players” table for a soccer club database. Select the right SQL syntax to insert the player data into the table.
    - [ ] INSERT INTO TABLE Players (ID, name, age) VALUES (5, "Tina", 23);
    - [x] **INSERT INTO Players (ID, name, age) VALUES (5, "Tina", 23);**
        > This is the right SQL syntax to insert the new record of data into the players’ table.

5. A hockey team requires all available data on their players for an upcoming meeting. Choose the correct SQL statement to select all data available in the players’ table
    - [ ] SELECT * players;
    - [x] **SELECT * FROM players;**
        > This is the SQL statement to select all data from the players’ table.
