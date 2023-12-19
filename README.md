# Backend System for Cafe Coupon Management

## About the Project

- Most cafes issue coupons and provide free americanos for collecting 10 coupons (or stamps).
- However, these coupons are at risk of loss and have the disadvantage of causing paper waste.
- This coupon storage service in the form of a mobile app is created so that electronic coupons are automatically accumulated for each cafe when paying for coffee at a cafe.
- After that, the electronic coupon is used to receive benefits such as a cup of americano, thereby eliminating the risk of coupon loss and preventing paper waste from being caused.
<br />

## Built with

- JavaScript(Express Framework), Python
- MongoDB
- RESTful API, gRPC
<br />

## **Architecture**
![image](https://github.com/Cho-SangHyun/coupon-managing-server/assets/65762283/27b90498-5325-4af5-966e-3d29994d6031)
- Client Side uses RESTful API to send requests to API servers build with Express Framework.
- The API Server sends a request to the service written in Python using the gRPC.
- Python Service works with MongoDB to perform the tasks requested by API Server, and then returns the results to the API Server.
- API Server creates the appropriate response code and response values based on the results returned by Python Service.

<br />  


## API List

1. Look up coupons for a particular user

`GET` /users/{userId}/coupons  
<br />  

2. Look up coupons for a particular cafe among my coupons

`GET` /users/{userId}/coupons/{cafeName}  
<br />  

  
3. Add coupons for a particular user's particular cafe

`POST` /users/{userId}/coupons/{cafeName}    
<br />  

4. Use Coupons

`PATCH` /users/{userId}/coupons/{cafeName}  
<br />  

5. Look up coupon ranking by cafe

`GET` /users/ranking/{cafeName}  
<br />  

6. Look up cafe list

`GET` /cafes  
<br />  

7. Look up detailed cafe information

`GET` /cafes/{cafeName}  
<br />  

8. Register new cafe

`POST` /cafes  
<br />  

9. Modify cafe information

`PATCH` /cafes/{cafeName}  
<br />  

10. Delete cafe information

`DELETE` /cafes/{cafeName}  
