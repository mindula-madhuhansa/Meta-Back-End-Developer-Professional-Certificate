1. Which of the following SQL statements adds a $2.00 service fee to the total price in a table called "Orders", that lists the price of orders customers placed with a store?
    - [ ] SELECT total + 2 FROM the Orders TABLE;
    - [x] **SELECT total + 2 FROM Orders;**
    - [ ] SELECT total + 2 FROM Orders TABLE;
        > This is the right syntax to complete this task.

2. What does the following SQL statement do?
<br/>`SELECT total / 2 FROM Orders;`<br/><br/>

    - [ ] It returns the value of total price column in the second row.
    - [x] **It returns the result of total price divided by 2 for each cell in the total price column.**
        > It returns the result of total price divided by 2 for each cell in the total price column

3. The following SQL statement returns 2 percent of the total price:
<br/>`SELECT total % 2 FROM Orders;`<br/><br/>
    - [ ] True
    - [x] **False**
        > This SQL statement returns the remainder of the total price value divided by 2.

4. Which of the following SQL statements returns 50% of the total price? Choose all correct answers.
    - [x] **SELECT total * 0.5 FROM Orders;**
        > This statement returns 50% from the total price by multiplying the total price by 0.5.
    - [ ] SELECT total * 50 FROM Orders;
    - [x] **SELECT total / 2 FROM Orders;**
        > This statement returns 50% from the total price by dividing the total price by 2.
    - [ ] SELECT total / 50% FROM Orders;

5. Select the right SQL statement to display the values of the total prices that are greater than $140.

    - [ ] SELECT total FROM Orders WHERE total < 140;
    - [x] **SELECT total FROM Orders WHERE total > 140;**
    - [ ] SELECT total FROM Orders WHERE total >= 140;
        > This is the right syntax that shows the values of total prices greater than $140.

6. Does the following SQL statements sort the result-set of the total prices in ascending or descending order?
<br/>`SELECT * FROM Orders ORDER BY total;`<br/><br/>
    - [ ] Descending
    - [x] **Ascending**
        > The ORDER BY keyword in SQL sorts the records in ascending order by default.

7. The following SQL statement filters data based on ____
<br/>`SELECT * FROM customers WHERE Country = "Germany";`<br/><br/>
    - [ ] 'Germany' column with 'country' value
    - [x] **'Country' column with 'Germany' value**
        > The output result of this statement will be filtered based on the country column with Germany value.

8. In SQL you can sort records in descending order using the DESCENDING keyword.
    - [x] **False**
    - [ ] True
        > You need to use the DESC keyword.

9. The output of the following SQL query within the Orders table is: UK, UK, UK, France, France, Finland
<br/>`SELECT DISTINCT Country FROM Orders;`<br/><br/>
    - [ ] True
    - [x] **False**
        > The output result of this SQL query will be: UK, France, Finland

10. What does the following SQL statement do? 
<br/>`SELECT * FROM Orders ORDER BY country, total;`<br/><br/>
    - [ ] Orders the result by country and ignores the total price.
    - [x] **Orders the result by country first then total price.**
        > It orders the result by country first, but if some records have the same country, it orders them by lowest total price.
