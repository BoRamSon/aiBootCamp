
-- =========================================
-- 문제  1
-- 각 팀별로 키가 180 이상인 선수의 숫자를 출력한다.
-- team_name, 인원수
use mydb2;
SELECT * FROM team;
SELECT * FROM player;

-- < 먼저 count만 해보기 > 
SELECT HEIGHT, count(*)
FROM player
GROUP BY HEIGHT;

-- < 일단 하나 만들어보기 >
-- SELECT 
-- 			T.Team_name,
-- 			P.player_name,
-- 			P.HEIGHT
-- FROM team T
-- INNER JOIN player P ON T.team_ID = P. team_ID
-- WHERE P.HEIGHT > 180;

-- < 직접 시도해보기 >  = 실패  
-- SELECT 
-- 			T.Team_name,
-- 			P.player_name,
-- -- 			P.HEIGHT
-- 			(
-- 				SELECT count(*)
-- 				FROM 
-- 				GROUP BY Team_name
-- 			) AS what
-- FROM team T
-- INNER JOIN player P ON T.team_ID = P. team_ID
-- WHERE P.HEIGHT > 180
-- ORDER BY T.Team_name;

-- < 같이 풀어보기 1 >
-- 서브쿼리로 해결 
select team_id, count(*) cnt, 
(select team_name from team where team_id =player.team_id) team_name
from player 
where height>=180
group by team_id;

-- < 같이 풀어보기 2 >
select team_name, cnt
from (
	select team_id, count(*) cnt 
	from player 
	where height>=180
	group by team_id
) as A 
join team B on A.team_id=B.team_id;

-- < 같이 풀어보기 3 >
select team_name, cnt
from team A
join (
	select team_id, count(*) cnt 
	from player 
	where height>=180
	group by team_id
) as B  on A.team_id=B.team_id;



-- =========================================
-- 문제 2    (전반적으로 문제에 대한 이해를 못했었음.)
-- FC서울에 전체 일정을 출력하기 (홈일정, away일정까지 )
-- Hint : union 쓰게 만드는 문
SELECT * FROM team;
SELECT * FROM player; 
SELECT * FROM schedule;

-- 먼저  FC 서울 의 stadium_id를 알아와야 한다.
-- Hometeam_id, Awayteam_id 로 찾아봐야 한다. 여기에 들어간 id 값이 바로 team_id 값입니다.
-- 어느 팀으로 어떻게 경기를 하게 되는 것인지 스케줄상에 분류가 된 것입니다. 이 점을 알고 들어가야합니다.
SELECT Hometeam_id, Awayteam_id FROM schedule;

-- < 직접 시도해보기 > = 실패   
-- 일단 홈경기라고 하나 만들어봤는데 이게 아닌 것 같습니다. 
-- SELECT 
-- 				T.Team_id,
-- 				SCD.Hometeam_id 
-- -- 				SCD.Awayteam_id,
-- -- 				SCD.SCHE_DATE
-- FROM team T
-- INNER JOIN player P ON T.team_id = P.team_id
-- INNER JOIN Stadium ST ON T.Stadium_id = ST.Stadium_id 
-- INNER JOIN schedule SCD ON T.Stadium_id = SCD.Stadium_id 
-- WHERE T.team_name = 'FC서울';


-- < 같이 풀어보기 > 
SELECT SCD.sche_date, T.team_id, T.team_name, 'home' AS home
FROM schedule SCD
JOIN Team T ON SCD.hometeam_id = T.team_id
WHERE T.team_name = 'FC서울'
UNION ALL
SELECT SCD.sche_date, T.team_id, T.team_name,	'away' AS home
FROM schedule SCD
JOIN Team T ON SCD.awayteam_id = T.team_id
WHERE T.team_name = 'FC서울';


-- =========================================
-- 문제  3 
-- 2012년 10월 19일날 C06스타티움과C05스타디움에서 경기하는 선수들 이름과 팀명을 출력하시오.
SELECT * FROM team;
SELECT player_id, Team_id, height FROM player;
SELECT * FROM stadium; 
SELECT * FROM schedule SCD WHERE SCD.SCHE_DATE = '20121019';

SELECT 
				SCD.SCHE_DATE,
				ST.stadium_name,
				T.Team_name,
				P.player_name				
FROM team T
INNER JOIN player P ON T.team_id = P.team_id
INNER JOIN Stadium ST ON T.Stadium_id = ST.Stadium_id 
-- INNER JOIN schedule SCD ON T.Stadium_id = SCD.Stadium_id   -- 틀림
INNER JOIN schedule SCD ON SCD.hometeam_id = T.team_id OR SCD.awayteam_id = T.team_id
WHERE SCD.stadium_id IN ('C06', 'C05') AND SCD.SCHE_DATE = '20121019'
ORDER BY T.team_id;



-- =========================================
-- 문제 4  -  같이 풀어보는 문제 (이렇게 풀 수 있는 문제도 있다.)
USE mydb2;
SELECT * FROM schedule;
-- 스타디움, 스케줄      |      ( 홈팀이김, 어웨이팀 이김, 무승부 )    3개 중에 답이 나오도록 

SELECT * FROM schedule;

-- 첫번째 단계
SELECT 
    stadium_id, SCHE_DATE,
    CASE
        WHEN  HOME_SCORE < AWAY_SCORE THEN 'Away 팀 이김 '
        WHEN  HOME_SCORE > AWAY_SCORE THEN 'Home팀 이김 '
        ELSE '무승부'
    END AS winner
FROM schedule;

-- 두번째 단계
SELECT 
    stadium_id, SCHE_DATE,
    CASE
        WHEN  HOME_SCORE < AWAY_SCORE THEN 'Away 팀 이김 '
        WHEN  HOME_SCORE > AWAY_SCORE THEN 'Home팀 이김 '
        ELSE '무승부'
    END AS winner,
    CASE
        WHEN  HOME_SCORE < AWAY_SCORE THEN awayteam_id
        WHEN  HOME_SCORE > AWAY_SCORE THEN hometeam_id
        ELSE 'none'
    END AS winner_team
FROM schedule;











