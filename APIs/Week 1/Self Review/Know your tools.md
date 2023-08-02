1. Which of the following configuration options in Insomnia were used in this Exercise? Choose all that apply.

- [x] **Creating a **GET** request.**
  > You learned how to create a GET request using Insomnia.
- [ ] Creating a Base Environment.
- [x] **Creating a **POST** request with JSON Data.**
  > You learned how to send a JSON object as an output using Insomnia.
- [x] **Creating a **POST** request with Form Data.**
  > You learned how to create a POST request for sending form data using Insomnia.

2. Using the Filter response body option in Insomnia, which of the following filters can be used to obtain the month field **[“july”]** as the output when used over the JSON object below? **Choose all that apply.**
   `{`
   `"title": "Lord of the Rings",`
   `"author": "JRR Tolkien",`
   `"published" : {`
   `"year": 1954,`
   `"month": "july",`
   `"day" : 29}`
   `}`

- [ ] `$.json.month`
- [ ] `$.json.published."month"`
- [x] **`$[json][published][month]`**
  > The filter used will be able to access the value of the month property and return the desired result.
- [x] **`$.json.published.[month]`**
  > The filter used will be able to access the value of the month property and return the desired result.

3. Which of the following JSON objects will return a valid JSON output that is not null while making a POST request.

- [x] **`{ "title": "Lord of the Rings" }`**
- [ ] `{ "title": Lord of the Rings }`
- [ ] `{ title: "Lord of the Rings" }`
- [ ] `{ "title": "Lord of the Rings" ,}`
  > This is a correct format that will produce the JSON output.
