1. You can use the **ModelForm** class to automatically generate an HTML form by using a Model.<br/>In the **models.py** file of lab just completed, you created a class called **Booking** containing five attributes:<br/>
&emsp;first_name<br/>
&emsp;last_name<br/>
&emsp;guest_count<br/>
&emsp;reservation_time<br/>
Inside the **forms.py** file, you created another class called **BookingForm**. Inside this class, you created another class called **Meta** and declared the attributes models and fields inside it.<br/><br/>Regarding the **fields** attribute, which of the following is the correct code snippet to indicate that all fields in the model should be used?
    
    - [ ] `fields = "_all_"`
    - [x] `fields = "__all__"`
    - [ ] `fields = "all"`
        > To indicate that all fields in the model should be used, set the **fields** attribute to the value of **"__ all__"**.

2. In the lab you just completed, you created an HTML form by placing code to generate the form elements from the **ModelForm** class.<br/><br/>
book.html<br/>
`<form  action=""  method="post">`<br/>
&emsp;`<!-- Insert form elements -->`<br/>
&emsp;`<input  type="submit"  id="button">`<br/>
`</form>`<br/><br/>
views.py<br/>
`def book(request):`<br/>
&emsp;`form = BookingForm()`<br/>
&emsp;`context = {'form': form}`<br/>
&emsp;`return render(request, 'book.html', context)`<br/><br/>Which of the following code snippets to render the form elements are correct? Select all that apply.
    
    - [ ] `{form}`
    - [ ] `form`
    - [x] `{{form}}`
        > The double curly brackets surrounding the form object is the appropriate way to add a variable passed inside a template
    - [x] `{{form.as_p}}`
        > The as_p inside form.as_p will render the contents of the form as an HTML paragraph tag. The double curly brackets are used when passing a variable to the template such as the form object
      
3. Based on the entries inside the Model Form you have generated, what is the name of the table created visible under the **db.sqlite3** database?
    - [ ] myapp_booking_form
    - [x] **myapp_booking**
    - [ ] myappbookingform
    - [ ] myapp_bookingform
        > The auto-generated name for the database table has the naming convention of app-name followed by the name of the model form.
