**NOTE: All questions in this quiz relate to the following table of data.**<br/><br/>
![department and course table](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/vh5cOk03QIueXDpNN_CLkQ_90094eee11ef4cdd9204942366b1bae1_schemaExample.PNG?expiry=1683936000000&hmac=VRtSWYbkELB6hfeIUa7cDJsmNMKa385L5wWVAPWQ50A)

1. The table of data conforms with the first normal form.
    - [x] **False**
    - [ ] True
      > This table contains unnecessary repeating groups of data as shown in the department ID, name and head of department columns.

2. What steps can you take to make sure that the table complies with the first normal form? Select all that apply.
   - [x] **Assign a primary key to the table.**
      > A primary key is required to ensure that the table contains unique records of data.
   - [ ] Assign a foreign key to the table.
   - [x] **Decompose the table to avoid data redundancy.**
      > Decomposing the table removes any unnecessary duplication of data.

3. Assume that the table has been decomposed into two separate tables: “Departments” and “Courses”. Which attributes should be included in each of the new tables? Remember that the records of the two tables must be linked with a foreign key.
   - [ ] The “Departments” table should include the department ID, name, and head of department. The “Courses” table should include the course ID and course name.
   - [x] **The “Departments” table should include the department ID, name, and head of department. The “Courses” table should include the course ID, course name and department ID.**
      > The “Courses” table should include the department ID as a foreign key to link the two tables.

4. After the normalization process is completed and the “College” table is decomposed into two tables called “Departments” and “Courses”. Which of the following two diagrams represents the correct schema?
![diagram 1 and diagram 2](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/13234db6-d31e-4235-96a3-d4dd9da8f377image1.png?expiry=1683936000000&hmac=DJcZvI2dxjZMI8JICFDgq9eEtzk2roFqe6AozBAf1Sc)
   - [ ] Diagram 1
   - [x] **Diagram 2**
      > The Courses table is the child table. It includes the department ID as a foreign key, which connects the two tables.

5. Which of the following SQL statements can be used to create the Courses table in the new schema? Remember that the Courses table must be linked to the Departments table.
   - [ ] `CREATE  TABLE Courses`<br/>`(`<br/>&emsp;`CourseID VARCHAR(5),`<br/>&emsp;`CourseName VARCHAR(50),`<br/>&emsp;`DepartmentID VARCHAR(10),`<br/>&emsp;`PRIMARY  KEY (CourseID),`<br/>&emsp;`FOREIGN  KEY (DepartmentID)`<br/>&emsp;`REFERENCES Courses (DepartmentID)`<br/>`);`<br/><br/>
   - [x] `CREATE  TABLE Courses`<br/>`(`<br/>&emsp;`CourseID VARCHAR(5),`<br/>&emsp;`CourseName VARCHAR(50),`<br/>&emsp;`DepartmentID VARCHAR(10),`<br/>&emsp;`PRIMARY  KEY (CourseID),`<br/>&emsp;`FOREIGN  KEY (DepartmentID)`<br/>&emsp;`REFERENCES Departments (DepartmentID)`<br/>`);`
      > This is the right SQL syntax.
