1. A conceptual database schema is a blueprint that defines how data is organized and related in a relational database.
    - [ ] False
    - [x] **True**
        > In general, the term database schema refers to the blueprint that illustrates the organization, grouping of and relationship between information in the database.

2. A conceptual database schema defines three essential parts. Select all that apply.
    - [x] **Tables**
        > Tables are the main components of the database schema.
    - [x] **Relationships**
        > Relationships between tables show how data are related in the database.
    - [x] **Attributes**
        > Attributes define the information required in each table.

3. A key advantage of developing a conceptual database schema is that it provides - in advance - a clear view of what tables are necessary and the way they will be connected.
    - [x] **True**
    - [ ] False

        > This is a major advantage of creating a database conceptual schema.

4. The foreign key is used to connect tables in a database schema.
    - [x] **True**
    - [ ] False

        > The foreign key is used to connect tables in a database schema.

5. A bookstore schema includes two tables: customers and orders implemented as follows:
<br/>`CREATE  TABLE Customers( CustomerID int  NOT  NULL, Name  VARCHAR(50), PRIMARY  KEY (CustomerID));`
<br/>`CREATE  TABLE Orders ( OrderID int  NOT  NULL, CustomerID int, PRIMARY  KEY (OrderID), FOREIGN  KEY (CustomerID) REFERENCES customers(CustomersID));`<br/><br/>
True or false. The two tables are connected through the OrderID attribute.
    - [ ] True
    - [x] **False**
        > The CustomerID is defined as a foreign key in this schema.
