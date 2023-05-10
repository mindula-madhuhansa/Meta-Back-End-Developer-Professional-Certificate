1. Which of the following statements is the correct command syntax to update a table in SQL?
    - [ ] UPDATE Table table_name;
    - [x] **UPDATE table_name;**
    - [ ] UPDATE column;
        > This is the right way to use the UPDATE command.

2. What is the missing SQL keyword in the following SQL statement to update the customer’s table?
    - [ ] ANY
    - [x] **SET**
        > SET is the right keyword in SQL to update the contact name with a new value.

3. Which of the following SQL statements can be used to update data for a student in the “Students” table?
    - [x] **UPDATE students SET name = 'Karl' WHERE ID = 18;**
    - [ ] UPDATE students WHERE ID = 18 SET name = 'Karl';
    - [ ] UPDATE students SET name = 'Karl' AND ID = 18;
        > This is the right syntax to update the student’s name in the “Students” table.

4. The following table contains data about customers. The customer data should be removed completely, but without deleting the table. Identify which statement can be used to delete all records of data from the customers table without deleting the table itself.
    
    | Customer ID | Customer Name |
    |-------------|---------------|
    | C1          | Karl          |
    | C2          | Jack          |

    - [ ] DROP TABLE customers
    - [x] **DELETE FROM customers;**
        > This SQL statement deletes all rows in the "customers" table, without deleting the table.

5. The 'WHERE' keyword is used in SQL to specify a condition to update or delete data from a table.
    - [x] **True**
    - [ ] False
        > WHERE is used to identify those records that fulfil a specified condition.
