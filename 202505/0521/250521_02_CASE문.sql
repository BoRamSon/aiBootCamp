USE mydb2;

-- CASE 문 

/*
> if 느낌에서 직관적으로 된 느낌으로 볼 수 있습니다.

## 🟢 Simple CASE
- 특정 값(value) 을 기준으로 비교할 때 사용
```sql
CASE 컬럼명
  WHEN 값1 THEN 결과1
  WHEN 값2 THEN 결과2
  ELSE 기본값
END
```
```sql
SELECT 
  player_name,
  team_id,
  CASE team_id
    WHEN 'k01' THEN '기아 타이거즈'
    WHEN 'k02' THEN 'LG 트윈스'
    ELSE '기타 팀'
  END AS team_name
FROM player;
```

## 🟢 Searched CASE
- 조건식(비교식) 을 직접 쓸 수 있음
```sql
CASE
  WHEN 조건1 THEN 결과1
  WHEN 조건2 THEN 결과2
  ELSE 기본값
END
```
```sql
SELECT 
  player_name,
  join_yyyy,
  CASE 
    WHEN join_yyyy < 2020 THEN '베테랑'
    WHEN join_yyyy >= 2020 AND join_yyyy <= 2023 THEN '중견'
    ELSE '신입'
  END AS 경력구분
FROM player;
```
*/
-- -----------------------------------------
-- 문제
SELECT 
    player_name, 
    CASE posit   -- posit가 ~라면 
        WHEN 'GF' THEN '골키퍼'
        WHEN 'DF' THEN '수비수'
        WHEN 'FW' THEN '공격수'
        WHEN 'MF' THEN '미드필더'
        ELSE 'xxx 포지션 없음'
    END AS posit
FROM player
WHERE team_id = 'k01'


-- -----------------------------------------
-- 문제
-- 키가 190 이상 = A
-- 키가 180 넘으면 = B
SELECT * FROM team;
SELECT * FROM player;

SELECT 
    P.player_name, 
    P.HEIGHT,
    CASE
        WHEN  P.HEIGHT >= 190 THEN 'A'
        WHEN  P.HEIGHT >= 180 THEN 'B'
        ELSE 'C'
    END AS grade
FROM player P
WHERE P.team_id = 'k03'

-- -----------------------------------------
-- 문제
-- 부서번호            
-- 10  ->   총무부   |   20   ->    홍보부       |      30   ->   개발 1부    |     40   ->   개발 2
USE mydb;

SELECT * FROM dept;

SELECT 
    deptno,
    CASE deptno
        WHEN  10 THEN '총무'
        WHEN  20 THEN '홍보부'
        WHEN  30 THEN '개발 1부'
        WHEN  40 THEN '개발 2부'
--         ELSE '부서 없음'
    END AS department
FROM dept;

