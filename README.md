# 카페별 쿠폰 관리 백엔드 시스템

## About the Project

- 대부분의 카페는 쿠폰을 발급하며, 쿠폰(또는 도장)을 10장 모으면 아메리카노를 무료로 주는 서비스 등을 시행 중이다.
- 그러나 이 쿠폰들은 분실의 위험이 있으며, 종이쓰레기를 유발한다는 단점이 있다.
- 모바일 앱 형태의 쿠폰보관 서비스를 만들어서, 카페에서 커피 결제 시 자동으로 해당 앱에 카페별로 전자쿠폰이 누적되게끔 한다
- 이후 해당 전자쿠폰을 사용하여 아메리카노 1잔 등의 혜택을 받게 함으로써 쿠폰 분실의 위험을 없애고, 종이쓰레기가 유발되는 것을 막는다.
<br />

## Build with

- Java, Python
- Redis, MongoDB
- RESTful API, gRPC
<br />

## **Architecture**
<img width="1591" alt="Untitled" src="https://github.com/Cho-SangHyun/coupon-managing-server/assets/65762283/1d1dfc8f-7c23-44e9-9d41-a3fff8267f06">

<br />  


## API List

1. 내 쿠폰 조회

`GET` /coupons/{member_id}  
<br />  

2. 내 쿠폰 중 특정 카페에 대한 쿠폰 조회

`GET` /coupons/{member_id}/{cafe_id}  
<br />  

3. 새 쿠폰 추가

`POST` /coupons/{member_id}/{cafe_id}    
<br />  

4. 쿠폰 사용

`DELETE` /coupons/{member_id}/{cafe_id}  
<br />  

5. 쿠폰 랭커 TOP 10 조회

`GET` /coupons/ranking  
<br />  

6. 카페 목록 조회

`GET` /cafes  
<br />  

7. 카페 정보 상세 조회

`GET` /cafes/{cafe_id}  
<br />  

8. 신규 카페 등록

`POST` /cafes  
<br />  

9. 카페 정보 수정

`PATCH` /cafes/{cate_id}  
<br />  

10. 카페 정보 삭제

`DELETE` /cafes/{cate_id}  
<br />  

11. 카페 이용자 순 TOP 10 조회

`GET` /cafes/ranking  
