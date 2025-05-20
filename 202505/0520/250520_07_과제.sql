-- 과제   

/*
1. customers table에서 나라가 Germany 인 나라의 정보 전체
2. customers table에서 Austria, USA, Poland, Denmark에 사는 고객 리스트 
3. 각자 나라별로 고객이 몇명씩 있는지 확인  
4. 나라별로 고객이 5명이 이상인 나라 목록 
5. 나라이름이 B로 시작하는 나라들의 전체 합  
6. 나라는 UK  /  도시명은 London에 있는 고객 이름 목록 
7. 주문날짜가 '1996-07-01' ~ '1996-09-30' 일까지의 주문아이디와 고객이름  
8. 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기 
9. 배달자가 Federal Shipping 인 경우의 상품명 가격 수량만 출력  
*/

USE w3schools;

-- 보기용  
SELECT DISTINCT country FROM customers;
SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM orderdetails;
SELECT * FROM orders;
SELECT * FROM customers;

-- 1. customers table에서 나라가 Germany 인 나라의 정보 전체
SELECT * FROM customers;

SELECT * 
FROM customers
WHERE country = 'Germany';


-- 2. customers table에서 Austria, USA, Poland, Denmark에 사는 고객 리스트 
SELECT * FROM customers;

SELECT customerName, Country
FROM customers
WHERE country in ('Germany', 'USA', 'Poland', 'Denmark');


-- 3. 각자 나라별로 고객이 몇명씩 있는지 확인
SELECT * FROM customers;

SELECT country, count(*)
FROM customers
GROUP BY country;


-- 4. 나라별로 고객이 5명이 이상인 나라 목록
SELECT * FROM customers;

SELECT country, count(*) customer
FROM customers
GROUP BY country
HAVING customer >  5;


-- 5. 나라이름이 B로 시작하는 나라들의 전체 합
SELECT country FROM customers;

-- SELECT country, count(*)
-- FROM customers
-- GROUP BY country
-- HAVING country LIKE 'B%';

SELECT count(*)
FROM customers
WHERE country LIKE 'B%';



-- 6. 나라는 UK  /  도시명은 London 에 있는 고객 이름 목록
SELECT * FROM customers;

SELECT country, city, customerName
FROM customers
WHERE country = 'UK' AND city = 'London';


-- 7. 주문날짜가 '1996-07-01' ~ '1996-09-30' 일까지의 주문아이디와 고객이름
SELECT * FROM orders;

SELECT A.orderDate, A.orderID, B.customerName
FROM orders A
INNER JOIN customers B ON A.customerID = B.customerID
WHERE  YEAR(orderDate) = '1996' and  month(orderDate) IN ('07', '08', '09');


SELECT A.orderDate, A.orderID, B.customerName
FROM orders A
INNER JOIN customers B ON A.customerID = B.customerID
WHERE A.orderDate >= '1996-07-01' AND A.orderDate <= '1996-09-30';



-- 8. 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기 
SELECT A.orderDate, A.orderID, B.customerName
FROM orders A
INNER JOIN customers B ON A.customerID = B.customerID
WHERE  YEAR(orderDate) = '1996' and  month(orderDate) IN ('07', '08', '09')
ORDER BY B.customerName DESC;


-- 9. 배달자가 Federal Shipping 인 경우의 상품명 가격 수량만
SELECT * FROM products;
SELECT * FROM shippers;
SELECT * FROM orderdetails;

SELECT F.shipperName, B.productName, B.price, C.quantity
FROM categories A
INNER JOIN products B ON A.categoryID = B. categoryID
INNER JOIN orderdetails C ON B.productID = C.productID
INNER JOIN orders D ON C.orderID = D.orderID
INNER JOIN customers E ON D.customerID = E.customerID
INNER JOIN shippers F ON D.shipperID = F.shipperID
WHERE  F.shipperName = 'Federal Shipping';
