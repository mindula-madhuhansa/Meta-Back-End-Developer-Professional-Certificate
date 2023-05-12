1. Write an SQL statement to create a database called "SportsClub".<br/>
    > `CREATE DATABASE SportsClub;`

2. In the text field below, input the missing keyword (___) from the following SQL statement to create a table called "Players".<br/>
`CREATE ____ Players (playerID INT, playerName VARCHAR(50), age INT, PRIMARY  KEY(playerID));`<br/>
Run the complete SQL statement in MySQL to create the table in the club database.
    > **TABLE**

3. In the text field below, input the missing keyword (___) from the following SQL statement to insert data into the "Players" table.<br/>
`INSERT  INTO Players (playerID, playerName, age) ____ (1, "Jack", 25);`
    > **VALUES**

4. Insert three more records into the "Players" table that contain the following data:
   - (2, "Karl", 20)
   - (3, "Mark", 21)
   - (4, "Andrew", 22)
   <br/><br/>Once you have executed the INSERT INTO statement to enter these three records of data, run the following SQL statement:<br/>
   `SELECT playerName FROM Players WHERE playerID =  2;`<br/><br/>
   What is the playerName that appears on the screen?<br/>
    >    **Karl**
  
5. Write a SQL statement that outputs all players names in the "Players" table. When you run the right SQL query, you should have the following output result:<br/>
![playerName](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/iIMg7NzOTieDIOzczr4nog_cd84f779973a4eb4a1d68fc6f7d507e1_C1M5L1-IMAGE02.png?expiry=1683936000000&hmac=UEKec5RajPEVP2eYw2MxiKGFJoHHB7b5M5hRlOElkZ4)
    > `SELECT playerName FROM Players;`

6. The following table called "Players", contains four records of data. Write a SQL statement that updates the age of the player with ID = 3. The new age value should be '22'.<br/>
![player table](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Soy8Xu-bQcOMvF7vm3HDww_e0c86e055b064222a3049f418d42f1e1_C1M5L1-IMAGE03.png?expiry=1683936000000&hmac=h6euBPblfsKHL8iavYE_EYcFcprrCmeGQ5p2USlyFmk)
    > `UPDATE Players SET age = 22 WHERE playerID = 3;`

7. The following table called "Players", contains four records of data. Write a SQL statement that deletes the record of the player with ID = 4.<br/>
![players table](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/zbiSbbGDSLq4km2xgwi6pw_3e2660baf6884b99be60493db82450e1_C1M5L1-IMAGE04.png?expiry=1683936000000&hmac=U5LfWuBWOdQvVDvrqcGNCL7hqJxcQ7cwvXP-seCMMQg)
    > `DELETE FROM Players WHERE playerID = 4;`

8. Write an SQL statement that evaluates if the PlayerID in the following "Players" table is odd or even.<br/>
**Hint:** Assume X is a number. If the remainder of X divided by 2 is 0, then X is an even number otherwise X is an odd number. Remember to use the “%” symbol to get the remainder.
    
    | PlayerID | Name |
    |----------|------|
    | 1        | Karl |
    | 2        | Adam |
    | 3        | Anas |

    > `SELECT PlayerID % 2 FROM Players;`

9. Write an SQL statement that outputs all names of the players in the following "Players" table who are older than 25 years of age.
    
    | Age | Name |
    |-----|------|
    | 38  | Karl |
    | 25  | Adam |
    | 22  | Anas |

    > `SELECT Name FROM Players WHERE Age > 25;`

10. Review the following ER-Diagram. Write the missing part of the SQL statement to define a foreign key that links the course table with the department table.<br/>
![course table and department table](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/bQADBzaDQKiAAwc2g3CoUA_36dc38637ea449afafc0d7ec466e7ce1_C1M5L1-IMAGE07.png?expiry=1683936000000&hmac=fOMzSGoqCxgnwCBYnPzKsX3q_lOoM9S1h90NPcyprRo)
CREATE TABLE Course(<br/>courseID int NOT NULL, courseName VARCHAR(50), PRIMARY KEY (courseID),<br/> ____ ____ ( ____ ) ____ ____ ( ____ )<br/>);<br/>
**Hint:** write only the missing part in your answer.
    > `FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)`

11. What is a row of information about one specific staff member in a college database table referred to as?
    - [x] **A record**
    - [ ] A key
    - [ ] A column
        > Each row of the table will have a record of information that refers to a specific staff.

12. A sports club database includes a table called "Members" with two columns:
    - A 'member number' column that contains the phone number of each member
    - And a 'full name' column that contains the full name of each member.
    <br/>Choose the right data type for each column. Select all correct answers.
        - [ ] The Full name column data type is CHAR.
        - [x] **The Player number column data type is INT.**
        - [x] **The Full name column data type is VARCHAR.**
        - [ ] The Player number column data type is DECIMAL.<br/><br/>

13. In a football club the skill level of all new players must automatically be set at the default of level 1. Which SQL syntax is used to set this default level using the DEFAULT keyword?
    - [x] **level INT DEFAULT 1;**
    - [ ] DEFAULT level INT 1;<br/><br/>

14. Database constraints are used to limit the type of data value that can be stored in a table.
    - [x] **True**
    - [ ] False
        > The constraints ensure the accuracy and reliability of the data value that goes into the table.

15. The output result of the following SQL statement is the data of all customers from Italy.
<br/>`SELECT  *  FROM customers WHERE Country = "Italy";`
    - [x] **True**
    - [ ] False
        > The output result of this statement returns the data of all customers from Italy. The ‘*’ symbol means all columns in the table.

16. The output result of the following SQL statement returns the records of all customers from India in Alphabetical order from A to Z.
<br/>`SELECT  *  FROM students WHERE country = "India" ORDER  BY FirstName DESC;`
    - [ ] True
    - [x] **False**
        > The output result of this SQL statement returns the records of all customers from India in reverse Alphabetical order from Z to A. This is because the DESC keyword sorts the records in descending order.

17. What does the following SQL statement do?
<br/>`SELECT  *  FROM Players ORDER  BY Country, PlayerName;`
    - [ ] It orders the result by country and ignores the staff name.
    - [x] **It displays the results ordered by country first, then players name.**
        > It orders the result set by country first, but if some records have the same country name, it orders them by staff name.

18. The following table of data conforms with the first normal form.
    
    | Department ID | Department Name | Head of department | Course ID | Course Name  |
    |---------------|-----------------|--------------------|-----------|--------------|
    | D1            | Computing       | Dr Karl            | C1        | Database     |
    | D1            | Computing       | Dr Karl            | C2        | Python       |
    | D1            | Computing       | Dr Karl            | C3        | Web          |
    | D2            | Computing       | Dr Karl            | C4        | Java         |
    | D2            | Math            | Dr Mosa            | C5        | Math         |

    - [ ] True
    - [x] **False**
        > This table contains unnecessary repeating groups of data in the department ID, department name and head of department columns. These columns violate the rule of first normal form.

19. Which of the following represents the correct diagram that links the course table with the department table?<br/>
![diagram 1 and diagram 2](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/78a3dfa3-4bd8-4f27-99da-e8f93e00d4b7image1.png?expiry=1683936000000&hmac=Xz20T83X0N4DTYoNeeLrzIns6k_ZqD9hnnvtbaqgZfc)
    - [ ] Diagram 1
    - [x] **Diagram 2**
        > The DepartmentID foreign key connects the Course table with the Department table.

20. Identify the relationship between the tables in the diagram.<br/>
![course table and department table](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/ZyjEXmb5TESoxF5m-axE4Q_00410678a91e4df38f4175346cffd3e1_graded-assessment-question-20-image.png?expiry=1683936000000&hmac=yHu5n-4lh-M2iSxZpJgseTlma0zu9uFy8J3tfXdjJ2E)
    - [ ] Many-to-many relationship.
    - [x] **Many-to-one relationship.**
    - [ ] One-to-one relationship.
        > These diagrams show an example of a many-to-one relationship as many courses may belong to one department.
