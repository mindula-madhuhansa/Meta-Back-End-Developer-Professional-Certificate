1. A soccer club’s database includes a “Players” table. The table contains a “Player number” column that records the jersey number of each player in the team. Each jersey number is a whole number. Identify the correct data type for this column.
    - [ ] DECIMAL
    - [x] **TINYINT**

        > TINYINT is an integer data type that accepts whole numbers only.

2. In a sports club database, the “Players” table includes a date of birth column that records the date of birth for each player. The right SQL data type to define the player date of birth is DOB VARCHAR(100).
    - [ ] True
    - [x] **False**

        > DATE is the right data type in this case.

3. Which one of the following SQL statements makes use of the correct data types to create a "Players" table in a soccer club’s database?
    - [x] **CREATE  TABLE players<br/>(<br/>&emsp;playerNumber INT,<br/>&emsp;fullName VARCHAR(100),<br/>&emsp;date_of_birth DATE<br/>);**
    - [ ] CREATE  TABLE players<br/>(<br/>&emsp;playerNumber INT,<br/>&emsp;fullName VARCHAR(100),<br/>&emsp;date_of_birth CHAR<br/>);
    - [ ] CREATE  TABLE players<br/>(<br/>&emsp;playerNumber Decimal,<br/>&emsp;fullName VARCHAR(100),<br/>&emsp;date_of_birth DATE<br/>);

        > All columns have been defined with suitable data types.

4. A soccer club’s database includes a staff table with three columns: username, full name and title. The username contains alphanumeric values such as: “Staff001” and has a fixed length of eight characters. Select the right SQL syntax.
    - [x] **username CHAR(8)**
    - [ ] username VARCHAR(8)

        > This the right SQL syntax because the username has a fixed length of 8 characters.

5. The following SQL statement can be used to create a table called “Players”, with a default value of “Miami” for the city column.
<br/><br/>CREATE  TABLE players<br/>(<br/>&emsp;playerName VARCHAR(100),<br/>&emsp;city VARCHAR(50)<br/>&emsp;DEFAULT “Miami”, age INT<br/>);<br/><br/>
    - [ ] False
    - [x] **True**
        > This SQL statement can be used to create a table called “Players”, with a default value of “Miami” for the city column.
