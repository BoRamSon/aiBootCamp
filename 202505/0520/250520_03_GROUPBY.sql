
-- ================================
-- GROUP BY 
-- 나라별로 몇명의 고객이 있는가??
-- 그룹함수 중에 null값 처리부분이 조금씩 다르다.
-- count(필드명) 에 null 값이 존재하면 카운트 하지 않는다. count(*)

SELECT * FROM customers;

SELECT count(*)  -- 전체 고객수
FROM customers ;


SELECT country, count(*)
FROM customers
GROUP BY country;


SELECT country, count(*)
FROM customers
GROUP BY country
ORDER BY count(*) desc;


SELECT A.ORDERID, B.shipperID
FROM ORDERS A
JOIN shippers B ON A.shipperID = B.shipperID;

-- [어렵다]  join 해서 group by 사용 
SELECT B.shippername, count(*)
FROM ORDERS A
JOIN shippers B ON A.shipperID = B.shipperID
GROUP BY shippername;

-- 위에꺼는 쉬운데 여기서 더 데이터가 들어가야 한다면....
-- ex) 주문번호, 배달업체, 배달업체 카운트를 도출하고 싶
SELECT B.shippername, count(*)
FROM ORDERS A
JOIN shippers B ON A.shipperID = B.shipperID
GROUP BY shippername;

-- 자! 직접 해보세요!!!
USE w3schools;

SELECT * FROM ORDERS;
SELECT * FROM shippers;

-- 내가 직접 시도해
SELECT A.orderID, B.shipperName, (
				SELECT F.shippername, count(*)
				FROM ORDERS E
				JOIN shippers F ON E.shipperID = F.shipperID
				GROUP BY shippername;
)
FROM ORDERS A
JOIN shippers B ON A.shipperID = B.shipperID;




-- 도저히 모르겠어서 ChatGPT에 물어
-- super example
SELECT 
		A.orderID, 
		B.shipperName, 
		(
		    SELECT COUNT(*) 
		    FROM orders E 
		    WHERE E.shipperID = A.shipperID     -- 이렇게 상관쿼리를 통해서 할 수 있구나... 마치 셀프조인 같이 생김 
  	) AS shipper_order_count
FROM ORDERS A
JOIN shippers B ON A.shipperID = B.shipperID;

-- 뭔가 self join도 될 것 같은데... 
SELECT 
		A.orderID, 
		B.shipperName, 
		(
		    SELECT COUNT(*) 
		    FROM orders E 
		    WHERE E.shipperID = A.shipperID  
  	) AS shipper_order_count
FROM ORDERS A
JOIN shippers B ON A.shipperID = B.shipperID;

SELECT .ename, A.mgr, B.ename
FROM shippers X
LEFT OUTER JOIN emp B ON A.mgr = B.empno;


-- 같이 풀어보기  
-- 생각을 정말 달리 해야하는구나... count 자체를 기준으로 해버리는게 
SELECT AA.*
FROM 
(
				SELECT F.shippername, count(*) cnt, E.shipperID
				FROM ORDERS E
				JOIN shippers F ON E.shipperID = F.shipperID
				GROUP BY shipperID
) AA
INNER JOIN orders Z ON Z.shipperID = AA.shipperID;


-- 카운터가 정렬해서 3개만  =>  분석함수(윈도우 함수)  -  oracle
SELECT E.shipperID, count(*) cnt
FROM ORDERS E
JOIN shippers F ON E.shipperID = F.shipperID
GROUP BY shipperID
ORDER BY cnt DESC
LIMIT 2;


-- 주문번호, 배송업체번호, 카운트
SELECT A.orderID, B.shipperID, cnt
FROM orders A 
INNER JOIN  (
					SELECT E.shipperID, count(*) cnt
					FROM ORDERS E
					JOIN shippers F ON E.shipperID = F.shipperID
					GROUP BY shipperID
					ORDER BY cnt DESC
					LIMIT 2
) B ON A.shipperID = B.shipperID


-- 서브쿼리 써서 
SELECT orderID, shipperID, (
			SELECT count(*) 
			FROM orders B 
			WHERE A. shipperID = B.shipperID
) AS cnt
FROM orders A;


-- 초보자가 코딩하는 순서
-- 디비접속 
-- select * from orders;       -- 쿼리 실행 
-- slect 
-- SELECT * FROM orders;    -- 쿼리 실행

-- FOR ORDER IN orders
-- 				SELECT count(*) FROM orders WHERE shipperID = order








