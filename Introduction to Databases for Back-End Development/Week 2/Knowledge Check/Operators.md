1. Add a 0.25 cent service fee to each value in the Total column. Complete the task using a SQL SELECT statement that includes a suitable operator.
    <br/>&emsp;&emsp;`SELECT total + 0.25 FROM invoices;`<br/><br/>

2. Apply a discount to your customers' totals by deducting 0.15 cent from each value in the Total column. Complete the task using a SQL SELECT statement that includes a suitable operator.
    <br/>&emsp;&emsp;`SELECT total - 0.15 FROM invoices;`<br/><br/>

3. Double the value of each record in the Total column. Complete the task using a SQL SELECT statement that includes the multiplication operator "*".
    <br/>&emsp;&emsp;`SELECT total * 2 FROM invoices;`<br/><br/>

4. Deduct 50% from each value in the Total column by dividing the total column by 2. Complete the task using a SQL SELECT statement that includes the division operator "/".
    <br/>&emsp;&emsp;`SELECT total / 2 FROM invoices;`<br/><br/>

5. Use the modulus operator "%" to get the remainder of the total column value divided by 2.
    <br/>&emsp;&emsp;`SELECT total % 2 FROM invoices;`
