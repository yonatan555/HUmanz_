# Humanz_Assignment , Backend implemntaion

Implemented using MongoDB database and Express (Node js) framework in VSC.

This API support the 4 next functions: Post Get Delete Filter(by Client Parameters)
I used MongoDB database to store my data.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
EXTRA: I used a python script to send 50(sampled data that appears in task) POST requsts to server.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run this program type
first: npm i
(for installing packeges)

second: npm start
(for running the server)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4 options to execute POST | GET | DELETE requests,
while the program is running.

2 GET requests(for filtering and get the whole clients)

---get all clients---
	
GET - for getting all clients from mongoDB database, 
go to website and copy the next line ,for example
GET REQUEST :  http://localhost3000/api/clients
This will pressent the whole clients.

---filter all clients who match the query---
	
GET - for getting clients who answer the requirement,
      make a query in the path line web
go to website and copy the next line ,for example
GET REQUEST :  http://localhost3000/api/client/?city=Los Angeles&country=United States
This will go to mongoDB and query it , return the appropriated data to user.


POST - Save a new client , and insertion into MongoDB Database 
This tested by PostMan tool by sending Json files to server 
POST REQUEST :  http://localhost3000/api/client/add

Then send json file with these fileds : 

fullName(String) , id(Number) , phoneNumber(String),ipAddress (String).
Example : 


{

   "fullName": "Ron Shamay",
   
   "id": 206087702,
   
   "ipAddress": "12.102.47.77",
   
   "phoneNumber" : "+972-12516427"
 
}



DELETE- delete a client , from mongodb database
This tested by PostMan tool by sending DELETE request with id(TEHUDAT ZEHOT) parameter to server.
go to website and copy the next line ,for example
DELETE REQUEST :  http://localhost3000/api/client/760444406

Backend Extras have acomplished.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
