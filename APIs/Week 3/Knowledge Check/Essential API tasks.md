1. What are the benefits of filtering? Choose all that apply.

   - [x] **Reduces extra load on the database server**
     > Using proper filtering, the API code fetches only the essential records from the database, which saves the database server from consuming extra CPU and memory.
   - [x] **The client can get only necessary data**
     > With filtering, the client can request and receive only the data it needs.
   - [x] **Reduces bandwidth consumption**
     > Since the API server delivers only essential data and strips out everything that is unnecessary, it can save a lot of bandwidth.
   - [ ] Increases API security

2. Filtering, sorting, searching and pagination cannot be done together.

   - [ ] True
   - [x] **False**
     > In DRF you can implement filtering, sorting, searching and pagination together for an API endpoint.

3. Which of the following settings in the **settings.py** file is used to paginate 5 items per page?

   - [ ] `'PAGE_ITEMS': 5`
   - [ ] `'PER_PAGE': 5`
   - [x] **`'PAGE_SIZE': 5`**
     > This is the correct setting you need to add in the **REST_FRAMEWORK** section in the **settings.py** file to paginate 5 items per page.

4. Which of the following statements about sorting are true? Choose all that apply.

   - [x] **Multiple fields are separated by a comma in the query string**
     > If you are sorting by multiple fields, you need to separate them with a comma.
   - [x] **Adding a hyphen in front of a field name sorts it in descending order**
     > When you add a hyphen in front of a field name in the query string, then it is sorted in descending order.
   - [ ] DRF can automatically sort the API output
   - [x] **You can sort by multiple fields at once.**
     > If you included multiple fields in your function or class-based views, then you will be able to sort by multiple fields.

5. Where can you implement caching? Choose all that apply.

   - [x] **Web server**
     > Web servers can cache the output to reduce database loads. There are dedicated caching tools like Redis or Memcached that can be used in the web server, besides database or file-based caching.
   - [x] **Database server**
     > Database servers can implement query caching to cache the output of the SQL queries.
   - [ ] Firewall
   - [ ] Load balancer
