1. In what way can you validate the **price** field to not be less than 5 in a serializer? Choose all that apply.

   - [x] **By adding this line of code in the serializer:<br/>`price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=5)`**
     > You can validate the minimum and maximum value of a field in this way in the serializer.
   - [ ] By using a **validate_price_lt** method
   - [ ] By using a **validation** method
   - [x] **By adding<br/>`'price': {'min_value': 2} in the extra_kwargs section`**
     > You can validate the minimum and maximum price by adding such conditions in the extra_kwargs section inside the Meta class in a serializer.
   - [x] By using a **validate** method
     > You can validate field data by writing a validate method inside the serializer class.

2. How can you limit an API endpoint in such a way that only **POST, PUT, PATCH** and **DELETE** calls will be throttled, but GET calls will not be throttled? Choose all that apply.

   - [ ] This cannot be done
   - [x] **By writing a custom throttle class and overriding the **get_throttles** method**
     > You need to write a custom throttle class and then override the get_throttles method inside a class-based view to achieve this.
   - [x] **By writing a custom throttle class and using it inside a @throttle_classes decorator.**
     > You can write a custom throttle class and use it inside the @throttle_classes policy decorator after using the @api_view(['POST','PUT','PATCH','DELETE']) API decorator.
   - [ ] By writing a scoped throttle class and set it up in the **settings.py** file

3. For token-based authentication, you need to install the Djoser library because DRF doesn’t support such authentications by default.

   - [ ] True
   - [x] **False**
     > DRF has excellent support for token-based authentication that doesn’t require a third-party library.

4. How can you enable support for sorting the API output by two fields: age and gender?

   - [x] **By manually parsing the query string**
     > If the field names are passed in the query string to an API you can manually parse that value and write code to sort the API output accordingly.
   - [x] **By adding this line of code<br/>`ordering_fields=['age','gender'] in a class-based view`**
     > You can add as many fields as you want in a public attribute called ordering_fields in a class-based view and DRF will automatically process it if the appropriate filter backend is set up in the settings.py file.
   - [ ] By adding this **@ordering_fields(['age','gender'])** above a function-based view
   - [ ] No code change is required. Just add **‘OrderingFilter'** in the settings.py file and DRF will process it automatically.

5. Which of the following are valid endpoints automatically created by Djoser?

   - [ ] /user/confirm/
   - [ ] /user/
   - [x] **/users/**
     > Djoser automatically creates this endpoint for you.
   - [x] **/users/me/**
     > Djoser automatically creates this endpoint for you. Using this endpoint, an authenticated user can fetch the account details.
   - [ ] /user/me/

6. You can manually expire a JWT access token any time you want.

   - [ ] True
   - [x] False
     > You cannot expire a JWT access token manually. It automatically expires after the default expiration time.

7. How can you assign users to a user group? Choose all that apply.

   - [ ] By making a call to /users/groups endpoint
   - [x] **By using the users.set() method in a Group object**
     > You can manually add any user to any group by using the users.set() of a group object.
   - [ ] Using Djoser library
   - [ ] By manually modifying the database records
   - [x] **From the Django admin panel**
     > You can create groups and then assign users to it from the Django admin panel.

8. Which of the following prefixes should you use to successfully authenticate a token using SimpleJWT library?

   - [ ] Auth
   - [ ] Auth Token
   - [x] **Bearer**
   - [ ] Token
     > You need to prepend the word ‘bearer’ before the actual token to make sure the JWT processes it properly and successfully authenticate if the token is valid. If you are using an external REST API clients like Insomnia or Postman, this is done automatically.

9. What happens when you blacklist a JWT refresh token?

   - [x] **It cannot be used to generate new access tokens anymore.**
     > When a refresh token is blacklisted, it cannot be used to generate a new access token anymore.
   - [ ] It expires
   - [ ] It blocks the user who bears this token
   - [ ] It cannot be used to generate new refresh tokens
   - [ ] It also blacklists the access token

10. Which of the following prefixes must you use with tokens to successfully authenticate an API call in plain DRF?

    - [ ] Bearer
    - [x] **Token**
    - [ ] Auth Token
    - [ ] Auth
      > You need to prepend the word ‘token’ before the actual token to make sure DRF processes it properly and successfully authenticates if the token is valid.

11. Which external package can you use to sanitize HTML tags from user input data?

    - [x] **Bleach**
      > You can use the bleach package in your DRF projects to sanitize input data when they contain HTML tags.
    - [ ] Cleaner
    - [ ] Sanitizer
