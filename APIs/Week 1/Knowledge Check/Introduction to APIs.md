1. Why is communicating over HTTPS more secure than HTTP?

   - [ ] There is only server-side encryption and client-side encryption
   - [ ] Both client- and server-side are encrypted but decryption is not performed.
   - [x] **Encryption and decryption are performed both on the client- and server-side.**
   - [ ] There is client-side encryption and server-side decryption
     > HTTPS is secure which means that there is encryption for data exchanged both at client- and server-side which can also be decrypted.

2. Which of the following HTTPS methods is used to partially update data?

   - [ ] GET
   - [ ] PUT
   - [ ] POST
   - [x] **PATCH**
     > PATCH is used to partially updating a resource.

3. Which of the following HTTP status codes inside the response header indicate server-side errors?

   - [ ] 100-199
   - [ ] 300-399
   - [x] **500-599**
   - [ ] 400-499
     > The status codes mentioned are used to indicate server-side errors to the client inside the response headers.

4. RESTful APIs are considered to be stateless. What this means is the state is saved **\_\_\_\_**.

   - [ ] Only on the server
   - [ ] On neither the client- nor server-side
   - [ ] Both on client and server
   - [x] Only with the client
     > The server does not contain any state of the API client making the request and cannot identify who is making the request.

5. Which of the following can be a layer in the RESTful API communication system that data encounters while being passed between the client and server? Select all that apply.
   - [x] **Load balancer**
     > Load balancers help in the efficient distribution of network traffic before the requests from client reach the server.
   - [ ] Headers
   - [x] **Firewall**
     > Firewalls are security systems over the network that help control and monitor the network traffic between the client and server based on security rules.
