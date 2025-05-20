USE w3schools;

-- ===================================
-- < 자주 쓰는 함수 모음 >

-- now
SELECT now()
SELECT now() FROM customers;    -- customers 테이블 개수만큼 호출된다.

-- like
SELECT * FROM customers WHERE customername LIKE '%Around%';

-- concat
SELECT concat('Tom ', "is", ' a student') AS sentence;

SELECT CONCAT(Address, " ", PostalCode, " ", City) Address   -- as가 생략되어도 무관하다.
FROM Customers; 


-- TRIM
SELECT TRIM('    SQL Tutorial    ') AS TrimmedString; 
-- LTRIM
SELECT LTRIM("     SQL Tutorial") AS LeftTrimmedString; 
SELECT LTRIM("     SQL Tutorial       ") AS LeftTrimmedString; 
-- RTRIM
SELECT RTRIM("SQL Tutorial     ") AS RightTrimmedString; 
SELECT RTRIM("      SQL Tutorial     ") AS RightTrimmedString; 


-- SUBSTR
-- 대부분의 DBMS가 문자열인덱스를 1부터 시작한다.
SELECT SUBSTR("SQL Tutorial", 5, 3) AS ExtractString; 
-- 해석 : 5번째 자리부터 3개를 가져온다.

-- 이런식으로도 활용할 수 있습니다.
SELECT substr('2025-05-20', 1, 4) YEAR,
        substr('2025-05-20', 6, 2) MONTH,
        substr('2025-05-20', 9, 2) day;



-- ===================================
-- < 수학함수 >
-- ceil : 올림함수     -- 데이터 개수가 231개  ->  23.1
-- floor : 내림함수 



-- ===================================
-- < 날짜 함수 >

-- ADDDATE
SELECT ADDDATE("2017-06-15", INTERVAL 10 DAY); 
-- interval = '간격'을 의미 
-- 해석: 2017-06-15에 10일을 더한다.

SELECT ADDDATE("2017-12-29", INTERVAL 10 DAY); 
-- 이런 것들을 자동으로 계산해주는 함수로 인해 편하다. 

-- DATADIFF
SELECT DATEDIFF("2017-06-25", "2017-06-15"); 

-- ------------------------------
-- < 날짜 함수 예제 >

-- 주문날짜가 '1996-07-01' ~ '1996-09-30' 일까지의 주문아이디와 고객이름
SELECT * FROM orders;

SELECT A.orderDate, A.orderID, B.customerName
FROM orders A
INNER JOIN customers B ON A.customerID = B.customerID
WHERE  YEAR(orderDate) = '1996' and  month(orderDate) IN ('07', '08', '09');


SELECT A.orderDate, A.orderID, B.customerName
FROM orders A
INNER JOIN customers B ON A.customerID = B.customerID
WHERE A.orderDate >= '1996-07-01' AND A.orderDate <= '1996-09-30';

-- 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기 
SELECT A.orderDate, A.orderID, B.customerName
FROM orders A
INNER JOIN customers B ON A.customerID = B.customerID
WHERE  YEAR(orderDate) = '1996' and  month(orderDate) IN ('07', '08', '09')
ORDER BY B.customerName DESC;




