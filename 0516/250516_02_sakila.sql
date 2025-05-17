use sakila;

-- [기초 조회]
-- 1. 모든 배우(Actor)의 이름과 성을 조회하시오.
desc actor;
select count(*) from actor; -- 습관적으로 먼제 db 갯수가 뭔지 확인 후 *를 사용해야합니다.
select * from actor;
select * from actor limit 10, 10; -- limit 옵셋(시작), (시작부터)개수
SELECT first_name, last_name FROM actor;

-- 2. 배우 테이블에서 성(last_name)이 ‘DAVIS’인 사람을 모두 찾으시오.
-- SELECT first_name FROM actor where 
select * from actor where first_name = 'davis';

-- 3. 고객(Customer)의 이메일 목록을 알파벳 순서로 조회하시오.
select * from customer order by email;

-- 4. 영화(film)의 제목과 대여 요금(rental_rate)을 조회하시오.
select title, rental_rate from film; 

-- 5. 고객(Customer)의 이름, 성, 이메일을 각각 출력하시오.
select last_name, first_name, email from customer;

-- 6. 카테고리(category)별 이름과 ID를 출력하시오.
select name, category_id from category;



-- [조건과 정렬]
-- 7. 길이가 180분 이상인 영화 제목을 조회하시오.
select * from film where length >= 180;

-- 8. ‘Comedy’ 카테고리에 속한 영화 제목을 모두 조회하시오. (join)
select * from category where name = 'comedy';
-- 최소한 2개 이상의 테이블을 join 해야합니다.

-- 9. 🔥🔥🔥🔥🔥 [정렬] 대여 요금이 4.99 이상인 영화 중에서 제목(title)과 요금(rental_rate)을 내림차순 정렬하시오.
select title, rental_rate 
from film 
where retal_rate >= 4.99 
order by rental_rate desc;

-- 10. 대여(rental) 중 2005년에 이루어진 기록만 조회하시오.
desc rental;
select * from rental
where rental_date >= '2005-01-01'
and rental_date >= '2005-12-31'

-- 🔥🔥🔥🔥🔥 문자열을 자르는 함수 substring
-- pthon이나 java 0부터 시작된다.  디비는 1번부터!!
-- substring(시작위치, 개수) 1번부터
select rental_date, substring(rental_date, 1, 4)
from rental;

select * from rental
where substring(rental_date, 1, 4) = '2005';

-- 11. 🔥🔥🔥🔥🔥 고객 중 이름이 'S'로 시작하는 고객의 이름을 조회하시오.
select * from customer
where last_naem like 'S%';

select * from actor
where length(last_name) = 5;

-- 12. 배우(actor) 테이블에서 이름이 5글자인 배우만 찾으시오.






