
/*
- UNION

	- union, union all 단순 합하기, 데이터 붙이기
	
	- union의 경우 중복 배제.
	- union all - 중복을 배제하지 않음.
	
```sql	
	SELECT COLUMN1, COLUMN2 FROM TABLE1
	UNION ALL
	
	SELECT COLUMN1, COLUMN2 FROM TABLE2
```
	- 필드 개수와 타입만 맞으면 된다.
	
	
	
- 사용 사례
	- 행을 열로 바꿔야 할 때
	- 포털사이트, 국가 기관 검색어로 검색하면 각 테이블로부터 검색한 내용을 전부 union해서 갖고 온다.

*/



USE mydb;

SELECT empno, ename FROM emp
UNION ALL
SELECT deptno, dname FROM dept;



SELECT count(*) FROM emp
UNION ALL
SELECT count(*) FROM dept;



USE w3schools;

SELECT * FROM Customers LIMIT 10;
SELECT * FROM Suppliers LIMIT 10;

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
