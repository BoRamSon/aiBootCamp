USE mydb2;

SHOW tables;

/*
player - 선수들
schedule - 스케줄
stadium - 경기장 정보
team - 팀정보 
*/

DESC team;

-- 단순 몇개의 팀이 있는지 확인 
SELECT count(*) FROM team;
SELECT * FROM team;

-- =======================================================
-- 문제 1
-- teamId 가 K01인 선수들의 명단을 확인하고 싶다.
SELECT count(*) FROM player;
SELECT * FROM player;

SELECT *  
FROM player
WHERE team_id = 'k01';

-- =======================================================
-- 문제 2
-- K01 팀의 정보 백번호로 불러와서 입단 연도 오름차순, 이름 오름차순해서 보여주기 (player_name, join_yyyy, posit)
-- (이 문제를 통해 중복된 정렬을 알 수 있음 )
SELECT * FROM player;

SELECT player_name, join_yyyy, posit, back_no
FROM player
WHERE team_id = 'k01'
ORDER BY join_yyyy, player_name;   -- null 값은 판단불가라서 맨 처음에 나옵니다. 

-- 한쪽만 내림차순으로 만들어 보았다.  
SELECT player_name, join_yyyy, posit
FROM player
WHERE team_id = 'k01'
ORDER BY join_yyyy desc, player_name;   -- null 값은 판단불가라서 맨 처음에 나옵니다. 

-- null 값 처리하기 
SELECT player_name, ifnull(join_yyyy, 2025) join_yyyy, posit
FROM player
WHERE team_id = 'k01'
ORDER BY join_yyyy, player_name; 

-- 서브쿼리 FROM절로 사용해보기 
SELECT *  
FROM (
		SELECT player_name, ifnull(join_yyyy, 2025) join_yyyy, posit
		FROM player
		WHERE team_id = 'k01'
) AS AA
ORDER BY join_yyyy, player_name; 

-- [다른 예시] null이 아닌 것들만 불어오겠다.
SELECT player_name, join_yyyy, posit  
FROM player
WHERE team_id = 'k01' AND join_yyyy IS NOT NULL
ORDER BY join_yyyy, player_name

-- [응용] UNION을 의도치않게 써보았다. (잘된다.)
SELECT player_name, join_yyyy, posit
FROM player
WHERE team_id = 'k01' AND join_yyyy IS NULL
UNION ALL
SELECT player_name, join_yyyy, posit  
FROM player
WHERE team_id = 'k01' AND join_yyyy IS NOT NULL
ORDER BY join_yyyy, player_name

-- [응용] (안됨) 서브쿼리를 써먹어보기 (order by가 먹히지 않는 문제 )
-- ANY, ALL, UNION 등 행의 순서를 보장하지 않는다.
-- 전체 결과 집합의 정렬 순서는 ORDER BY가 최종 쿼리 바깥에 있어야 적용됩니다.
SELECT AA.* 
FROM(
			SELECT player_name, join_yyyy, posit  
			FROM player
			WHERE team_id = 'k01' AND join_yyyy IS NOT NULL
			ORDER BY join_yyyy, player_name     -- 정렬이 안 먹는 문제가 있습니다.
) AS AA
UNION ALL
SELECT player_name, join_yyyy, posit
FROM player
WHERE team_id = 'k01' AND join_yyyy IS NULL;


SELECT *  
FROM (
		SELECT player_name, ifnull(join_yyyy, 5000) join_yyyy, posit
		FROM player
		WHERE team_id = 'k01'
) AS AA
ORDER BY join_yyyy, player_name;


-- null을 뒤로 정렬 시켜버리는 방법입니다.
SELECT player_name, join_yyyy, posit  
FROM player
WHERE team_id = 'k01'
ORDER BY join_yyyy IS NULL asc, join_yyyy asc, player_name
-- asc : 오름차순을 의미하며, default이기 때문에 제외해도 무방하다.
-- join_yyyy IS NULL asc    :    null을 뒤로 정렬 시켜버리는 방법입니다.


-- =======================================================
-- 문제 3
-- 울산 지역에 있는 모든 팀과 각 팀에 속한 선수이름과 우편번호 주소를 출력하자. 
-- 예시 결과 : 울산현대   |  곽기훈   |  울산   |  682-060   |  울산광역시 동구 서부동 산137-1   |   현대스포츠클럽하우스 
SELECT * FROM team;
SELECT * FROM player;

SELECT 
			T.Team_name, 
			P.player_name, 
			T.REGION_NAME, 
			concat(T.zip_code1, '-', T.zip_code2),
			T.address
FROM team T
INNER JOIN player P ON T.team_ID = P. team_ID
WHERE REGION_NAME = '울산'


--  team_id가 K01 이거나  K03 인 선수의 팀이름, 선수이름, 팀주소 
SELECT 
			T.Team_name, 
			P.player_name, 
			T.address
FROM team T
INNER JOIN player P ON T.team_ID = P. team_ID
WHERE T.team_id IN ('k01', 'k03');


-- !!! 서브쿼리 practice
-- select 절에서 사용하는 서브쿼리는 스칼라 서브쿼리만 됩니다.
-- 스칼라 -> 쿼리 실행결과가 달랑 값 하나인 것이 스칼라이다.
SELECT team_naem FROM team WHERE team_id = 'k01'

SELECT 
			P.player_name,
			(SELECT team_name FROM team T WHERE team_id = T.team_id) team_name   -- 스칼라 SELECT 서브쿼리 
FROM player P
WHERE P.team_id IN ('k01', 'k03');

-- 서브쿼리 추가  
SELECT 
			P.player_name,
			(SELECT team_name FROM team T WHERE team_id = T.team_id) team_name,
			(SELECT address FROM team T WHERE team_id = T.team_id) address,
			(SELECT concat(zip_code1, "-", zip_code2)
								FROM team WHERE team_id = A.team_id) zipcode
FROM player P
WHERE P.team_id IN ('k01', 'k03');


-- =======================================================
-- 문제 4
-- player 이름, 팀이름, 경기장 이름, K05, K07, K12 구단
-- 팀이름으로 정렬, 백넘버로 정렬 
SELECT * FROM team;
SELECT * FROM player;
SELECT * FROM stadium;

SELECT 
			P.player_name, 
			T.Team_name,
			S.stadium_name
-- 			P.back_no
FROM team T
INNER JOIN player P ON T.team_ID = P. team_ID
INNER JOIN stadium S ON T.stadium_id = S.stadium_id
WHERE T.team_id IN ('k05', 'k07', 'k12')
-- ORDER BY P.back_no;
-- ORDER BY T.Team_name, P.back_no IS NULL,  P.back_no;
ORDER BY T.Team_name, P.back_no;
