
-- ======================================
-- EXISTS
/*
EXISTS

- 장점
	- 서브쿼리의 모든 수행을 기다리지 않고, 뭔가 하나 찾으면 바로 끝남..
	- 서브쿼리의 수행 결과셋 존재 유무만 파악  

*/

USE w3schools;

-- alias 활용하는 습관을 들입니다. 찾 것이 좀 빨라집니다.
SELECT A.SupplierName
FROM Suppliers A
WHERE EXISTS (
					SELECT ProductName 
					FROM Products B
					WHERE B.SupplierID = A.supplierID AND Price < 20
); 







