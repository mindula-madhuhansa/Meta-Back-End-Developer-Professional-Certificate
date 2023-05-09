1. Identify the correct data type for the Product Price column in the following table.
    
    | Product ID | Product Price |
    |------------|---------------|
    | P1         | 13.50         |
    | P2         | 22.75         |

   - [ ] product_price STRING
   - [x] **product_price DECIMAL**
   - [ ] product_price TINYINT
   - [ ] product_price INT
        > A decimal should be used as the data type in this column as the price may include a fraction value.

2. A “customer id” column in a customer table is expected to include thousands of customers and the data type should be numeric only. What data type should you use to define this column?

   - [ ] customerID TINYINT
   - [ ] customerID DECIMAL
   - [x] **customerID INT**
        > Integer is a numeric data type that can be used for big whole numbers, which are required here.

3. The data type for the “Number of students” column in the following table must be defined as an INTEGER data type to ensure that only numeric values are accepted.

    | Course      | Number of students |
    |-------------|--------------------|
    | Computing   | 50                 |
    | Design      | 30                 |
    | Engineering | 40                 |

   - [ ] False
   - [x] **True**
        > You should only have whole numbers in this column.

4. Which of the following pieces of data are examples of a DECIMAL data type? Select all correct answers.

   - [x] **75.50**
        > This is a number with a 0.50 fraction.
   - [x] **50.00**
        > This is a number with a 0.00 fraction.
   - [ ] 455
   - [ ] 550

5. The integer data type stores both negative and positive numbers.

   - [ ] False
   - [x] **True**
        > An integer is a whole number data type that can have a positive, negative or zero value.
