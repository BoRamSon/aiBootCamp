
/*
< JOIN 복습  >

- inner join (교집합)
- left outer join (왼쪽집합이 다 출력)
- right outer join (오른쪽집합이 다 출력)
- cross join (카테시안곱, 조인조건이 없을 때 n by m)
- self join (자기 테이블끼리 조인을 한다.)

*/

USE w3schools;

SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM orderdetails;
SELECT * FROM customername;

SELECT ORDERID, A.customerid, customername
FROM customers A
JOIN orders B ON A.customerID = B.customerID
WHERE A.customername LIKE '%Handel%';



-- 제품명을 도출하려면???  ->   orders, products, orderdetails
-- 10258, 10263, 10351, 10368, 10382, 10390, 10402, 10403, 10430

SELECT * FROM orders;
SELECT * FROM orderdetails;


SELECT A.orderID, A.productID, productName, Quantity  -- 나는 어떤 물건을 몇개 구매했는데 알고 싶어서 이렇게 
FROM ORDERdetails A
JOIN products B ON A.productID = B.productID
WHERE ORDERID IN (10258, 10263, 10351, 10368, 10382, 10390, 10402, 10403, 10430);


SELECT A.productID, productName, Quantity
FROM ORDERdetails A
JOIN products B ON A.productID = B.productID
WHERE ORDERID IN (          -- 이게 바로 subquery 입니다. / ORDER ID가 이 서브쿼리 결과 내에 존재하는가????
				SELECT ORDERID					-- 존재하는 것만 가져와
				FROM customers A
				JOIN orders B ON A.customerID = B.customerID
				WHERE customername LIKE '%handel%'
);



/*
< JOIN 이론 >

- inner join 의 경우에는 from 절 데이블과 join절 테이블 구분 필요 없음... 데이터 개수가 좀 작은 테이블이 앞쪽에 오는 것이 좋다. (권고사항)
- join
	- for문, nested loop join => hash join

- 보통 내가 작성한 쿼리는 where 조건절이 먼저 실행되서 우선 데이터를 거른 다음에 조인을 한다. 	

- left outer join : from 절에 가까운테이블 내용이 다 나오길 원할 때.
- right outer join : from 절에 먼데이블 내용이 다 나오길 원할 때.
- full outer join : 합집합, ansi 표준은 있는데 mysql 없음.
- cross join

*/

SELECT *  FROM  ORDERS LIMIT 10;
SELECT *  FROM  ORDERdetails ORDER BY quantity;
SELECT *  FROM  ORDERdetails ORDER BY OrderID;
SELECT *  FROM  ORDERdetails LIMIT 10;
SELECT *  FROM  shippers LIMIT 10;
SELECT *  FROM  suppliers LIMIT 10;
SELECT *  FROM  customers LIMIT 10;


-- cross join (쉽다)
SELECT A.customerID, B.orderID
FROM customers A, orders B;


-- self join : 자기 테이블에서 join
-- (emp 테이블의 mgr 필드가 자기 상사의 사원번호임) 
-- 동일 테이블을 조인한다고 해서 self join 을 많이 쓴다. 코드테이블 만들 
USE mydb;

SELECT * FROM emp;

-- emp A    mgr   /   emp B   empno     이 2개가 서로 일치해야
SELECT A.ename, A.mgr, B.ename
FROM emp A
LEFT OUTER JOIN emp B ON A.mgr = B.empno;      -- 근데 LEFT OUTER JOIN을 



-- ===================================================
-- 다른 예제 보기 
USE w3schools;

SELECT A.OrderID, B.CustomerName
FROM Orders A
INNER JOIN Customers B ON A.CustomerID = B.CustomerID; 

-- w3schoos 에서 가져온 예
-- SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
-- FROM ((Orders
-- INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
-- INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID); 

-- 서브쿼리와 병합한 형태이지만, 이렇게 쓰는 것보다 join으로만 구성하는 것이 빠르다.
-- SELECT A.OrderID, A.CustomerName, C.ShipperName
-- FROM 
-- ( 
-- 			SELECT 
-- ) A
-- INNER JOIN Customers B ON A.CustomerID = B.CustomerID
-- INNER JOIN Shippers C ON A.ShipperID = C.ShipperID;

-- 결론
SELECT A.orderId, B.CustomerName, C.shippername
FROM orders A, Customers B, Shippers C
WHERE A.customerID = B.customerID
						AND A.shipperID = C.shipperID;
-- join만 쓰는 것이 일반적으로 서브쿼리보다 빠르다.


-- ========================================================
/*
< 문제풀어보기 >

- employees 테이블에 firstname 이 king 임
where E.firstname = 'king'

- 이 사람이 판매한 내역을 확인하고 싶다.

- 주문번호, 고객이름, 배달업자, 제품

*/
SELECT *  FROM employees LIMIT 10;
SELECT *  FROM  ORDERS WHERE EmployeeID = 7;
SELECT *  FROM  customers LIMIT 10;
SELECT *  FROM  shippers LIMIT 10;
SELECT *  FROM  ORDERDETAILS;
SELECT *  FROM  products LIMIT 10;

SELECT A.EmployeeID, A.Lastname
FROM employees A
WHERE A.Lastname = 'king';

-- 잘 풀었습니다. 하나하나씩 완성해나아가는 방식으로 해보았습니다.
SELECT 
-- 					A.EmployeeID, A.Lastname, 
-- 					B.EmployeeID, 
-- 					B.orderid, C.customerName, D.shipperName,
-- 					E.orderID, E.OrderDetailID, F.productID, F.ProductName
-- 					A.Lastname, 
					B.orderid, C.customerName, D.shipperName, F.ProductName
FROM employees A
INNER JOIN ORDERS B ON A.EMPLOYEEID = B.EMPLOYEEID
INNER JOIN customers C ON B.customerID = C.customerID
INNER JOIN shippers D  ON  B.shipperID = D.shipperID
INNER JOIN ORDERDETAILS E ON B.orderID = E.orderID
INNER JOIN products F ON E.productID = F.productID
WHERE A.Lastname like 'King%';  -- 이거 틀렸었습니다.


-- 같이 풀어보기 (위와 결과는 동일)
SELECT A.orderID, C.customername, F.shippername, E.productname
FROM orders A
INNER JOIN employees B ON A.EMPLOYEEID = B.EMPLOYEEID
INNER JOIN customers C ON A.customerID = C.customerID
INNER JOIN ORDERDETAILS D ON A.orderID = D.orderID
INNER JOIN products E ON D.productID = E.productID
INNER JOIN shippers F ON A.shipperID = F.shipperID
WHERE B.Lastname like 'King%';

