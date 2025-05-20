
-- =======================================
-- < join practice >
-- actor_id, first_name, last_name
USE sakila;

SELECT * FROM actor LIMIT 10;
SELECT * FROM film LIMIT 10;
-- 배우가 누군지 알 수가 없다... 

-- 어떤 배우가 어떤 영화에 출연했는지 알고 싶다...
SELECT * FROM film_actor LIMIT 10;

-- 영화 필름 기준으로 join 
SELECT title, description, B.actor_id,
concat(C.last_name, '', C.first_name) actor_name
FROM film A
LEFT OUTER JOIN film_actor B ON A.film_id = B.film_id
LEFT OUTER JOIN actor C ON B.actor_id = C.actor_id



-- ============================================
-- 문제 1
-- category가 conmedy인 영화 목록만
-- film, category, film_category

SELECT * FROM category LIMIT 20;  -- 5
SELECT * FROM film_category LIMIT 20;
SELECT * FROM film LIMIT 20;

-- 시도 1
SELECT A.category_id, B.category_id 
FROM category A
LEFT OUTER JOIN film_category B ON A.category_id = B.category_id;
-- LEFT OUTER JOIN actor C ON B.actor_id = C.actor_id

-- 시도2
SELECT A.category_id, B.category_id 
FROM category A
LEFT OUTER JOIN film_category B ON A.category_id = B.category_id
LEFT OUTER JOIN film C ON B.category_id = C.film_id
WHERE A.name = 'Comedy';

-- 같이 풀어보기 
SELECT title 
FROM film A
LEFT OUTER JOIN film_category B ON A.film_id = B.film_id
LEFT OUTER JOIN category C ON B.category_id = C.category_id
WHERE C.name = 'Comedy';



-- ============================================
-- 문제 2
-- 고객의 이름과 고객이 대여 한 영화 제목을 모두 출력하자 
-- customer, rental, invetory, film
-- inventory_id, store_id, film_id

-- !!!! 방법을 알아냈습니다. 이런 규칙을 왜 안알려주는지 모르겠지만....
SELECT * FROM customer LIMIT 20;     -- 1. 먼저 구할 값을 정한다.
		-- 2. 관련 있는 데이터들의 공통점을 파악한다. 그래서 다 가져온다. (like rental, inventory, film)
SELECT * FROM rental LIMIT 20;     -- 3. 
SELECT * FROM inventory LIMIT 20;
SELECT * FROM film LIMIT 20;

 -- 내가 직접 풀어보기! (성공)
SELECT A.first_name, A.last_name, B.rental_date, D.title
FROM customer A
LEFT OUTER JOIN rental B ON A.customer_id = B.customer_id
LEFT OUTER JOIN inventory C ON B.inventory_id = C.inventory_id
LEFT OUTER JOIN film D ON C.film_id = D.film_id
LIMIT 10;

-- 같이 풀어보기 (concat을 추가하고 테이블 명치까지변경하는 방법을 알게 되었습니다.)
SELECT concat(A.first_name, "  ", A.last_name) name, B.rental_date, D.title
FROM customer A
LEFT OUTER JOIN rental B ON A.customer_id = B.customer_id
LEFT OUTER JOIN inventory C ON B.inventory_id = C.inventory_id
LEFT OUTER JOIN film D ON C.film_id = D.film_id
LIMIT 10;



-- ========================================================
-- 문제 3 : NICK WAHLBERG 라는 배우가 출연한 영화의 제목 조회하기

SELECT * FROM actor LIMIT 20;
SELECT * FROM film_actor LIMIT 20;
SELECT * FROM film LIMIT 20;

SELECT concat(A.first_name, "  ", A.last_name) name, C.title
FROM actor A
LEFT OUTER JOIN film_actor B ON A.actor_id = B.actor_id
LEFT OUTER JOIN film C ON B.film_id = C.film_id
WHERE A.first_name = 'NICK' AND A.last_name = 'WAHLBERG'
LIMIT 10;

-- 같이 풀어보기 ( inner join으로도 할 줄 알아야 합니다.)
SELECT CONCAT(A.first_name, ' ', A.last_name) AS name, C.title
FROM actor A
INNER JOIN film_actor B ON A.actor_id = B.actor_id
INNER JOIN film C ON B.film_id = C.film_id
WHERE A.first_name = 'NICK' AND A.last_name = 'WAHLBERG'
LIMIT 10;



-- ========================================================
-- 문제 4 : London 도시의 고객 이름만 출력 

SELECT * FROM customer LIMIT 20;
SELECT * FROM address LIMIT 20;
SELECT * FROM city LIMIT 20;

SELECT concat(A.first_name, "  ", A.last_name) name, C.city
FROM customer A
LEFT OUTER JOIN address B ON A.address_id = B.address_id
LEFT OUTER JOIN city C ON B.city_id = C.city_id
WHERE C.city = 'London'

-- 같이 풀어보기
SELECT concat(A.first_name, "  ", A.last_name) name, C.city
FROM customer A 
JOIN address B ON A.address_id = B.address_id
JOIN city C ON B.city_id = C.city_id
WHERE C.city = 'London'



