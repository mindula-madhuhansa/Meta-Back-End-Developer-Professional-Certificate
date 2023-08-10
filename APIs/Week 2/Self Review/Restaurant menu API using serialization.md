1. The **id** field attribute that acts as the primary key of the model **MenuItem** can be added inside the HTML Form created by DRF on the webpage.

   - [ ] True
   - [x] **False**
     > The **id** attribute will be auto-generated and the end-user will only enter other form fields such as **title, price** and **inventory**.

2. In the lab you have just created, if you go to the API endpoint **http://127.0.0.1:8000/api/menu-items** and update the field value of price to **Price : 12** , what will the updated value for **price** inside the JSON object be?

   - [x] **`"price": "12.00"`**
   - [ ] `"price": "12”`
   - [ ] `price: "12.00"`
   - [ ] `"price": 12.00`
     > Both the key and the value will be updated as strings. The value will have 2 decimal places added as configured for the attribute inside the **MenuItem** model.

3. What is the status message that is generated and displayed on the screen once you press the **POST** button after filling the correct form data inside the webpage at the endpoint, **http://127.0.0.1:8000/api/menu-items** ?
   - [ ] HTTP 404 Not Found
   - [ ] HTTP 200 OK
   - [x] **HTTP 201 Created**
     > The status code is a result of a **POST** request that was successfully used to send new form data to the database table.
