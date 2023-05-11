1. Which of the following is a key aim of database normalization? Select all that apply.
    - [x] **Avoid errors during data modifications**
        > The data normalization process aims to maintain data consistency by avoiding errors in data modification.
    - [x] **Minimize data duplication**
        > The data normalization process aims to eliminate unnecessary data duplications.
    - [x] **Simplify data queries**
        > The data normalization process aims to simplify data queries from the database.

2. True or false. The first normal form allows for the storage of multiple values in table fields.
    - [ ] True
    - [x] **False**
        > The first normal form allows for the storage of atomic values of a column (also known as a single instance of data).

3. Partial Dependency occurs when a non-primary key attribute is functionally dependent on part of a composite key. This action violates which of the three normal forms?
    - [ ] First normal form
    - [x] **Second normal form**
    - [ ] Third normal form
        > Partial dependency violates the second normal form.

4. True or false. Transitive dependency occurs when a non-key attribute determines the values of one or more other attributes, violating the third normal form criteria.
    - [x] **True**
    - [ ] False
        > Transitive dependency occurs when a non-key attribute determines the values of one or more other attributes.

5. What actions should you take to ensure that a database is in first normal form? Select all that apply.
    - [ ] Connect your table with other tables in the database using a foreign key.
    - [x] **Eliminate repeating groups of data within individual tables.**
        > Eliminating repeating groups of data is essential to meet the first normal form.
    - [x] **Create a separate table for each set of related data.**
        > It is important to have a separate table for related data, so you can maintain data consistency.
