

-- ==================================


/*
 
 create table 테이블명 
( 
   id int primary key auto_increment,
   title varchar(20)

);

*/  


/*
CREATE TABLE `tb_member` (
  `member_id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `member_name` varchar(45) NOT NULL,
  `member_phone` varchar(45) NOT NULL,
  `member_email` varchar(45) NOT NULL,
  `member_ip` varchar(45) DEFAULT NULL,
  `regdate` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 
COLLATE=utf8mb4_0900_ai_ci;
*/
/*INSERT INTO `mydb2`.`tb_member`
(`member_id`,
`user_id`,
`password`,
`member_name`,
`member_phone`,
`member_email`,
`member_ip`,
`regdate`)
VALUES
(<{member_id: }>,
<{user_id: }>,
<{password: }>,
<{member_name: }>,
<{member_phone: }>,
<{member_email: }>,
<{member_ip: }>,
<{regdate: }>);
' - 어포스트로피 
` - 틸트  
*/

-- insert 명령어를 통해서 데이터 추가시 
-- auto_increment 는 빼고 넣자
-- Not Null 조건 필드는 다 넣자  
insert into tb_member( user_id, password, member_name, 
   member_phone, member_email, regdate) 
   values('user01', '1234', '홍길동', '010-0000-0001', 
          'hong@gmail.com', now());
-- 등록시 디비 서버의 날짜와 시간 을 알려준다 
  





-- ==================================
-- 테이블을 GUI로 만들어보자!
/*
- insert 명령어를 통해서 데이터 추가 시
  - auto-increment 는 빼고 넣자
  - not null 조건 필드는 다 넣자
*/

USE mydb2;

-- 에러해결을 위한 코드
-- member_id를 AUTO_INCREMENT로 변경
-- ALTER TABLE tb_member
-- MODIFY COLUMN member_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

SHOW CREATE TABLE tb_member;

CREATE TABLE `tb_member` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `password` varchar(225) NOT NULL,
  `member_name` varchar(45) NOT NULL,
  `member_phone` varchar(45) NOT NULL,
  `member_email` varchar(45) NOT NULL,
  `member_ip` varchar(45) DEFAULT NULL,
  `regdate` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

SHOW CREATE TABLE tb_member;

-- 
INSERT INTO  tb_member(user_id, password, member_name,
				member_phone, member_email, regdate)
values('user01', '1234', '홍길동', '010-0000-0001', 
								'hong@gmail.com', now());

DESC tb_member;

SELECT * FROM tb_member;
-- 확인완료 



-- ==================================
-- tb_guestbook  |  2번째 테이블 만들기
-- 실직적인 테이블을 직접 쿼리로 생성해보자!
CREATE TABLE tb_guestbook
(
			-- mysql에서 auto_increment 속성은 테이블에 하나의 필드만 반드시 primary key여야 한다.
			id bigint AUTO_INCREMENT,
			title varchar(1000) NOT NULL,
			contents text,
			writer bigint,   -- tb_member와 FOREIGN key로 묶음
			regdate datetime
);
-- SQL Error [1064] [42000]: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'regdate datetime)' at line 9

SHOW tables;  -- 확인 

-- 삭제
DROP TABLE tb_guestbook;

-- 다시 테이블 생성  
CREATE TABLE tb_guestbook
(
			id bigint AUTO_INCREMENT PRIMARY KEY,
			title varchar(1000) NOT NULL,
			contents text,
			writer int,          -- tb_member와 FOREIGN key로 묶음
			regdate datetime
);

-- 만들어졌는지 확인해봅시다
SHOW tables;


-- !!! FOREIGN KEY 추가하기     
-- tb_gestbook이 tb_member를 참조하는 구조이다.
ALTER TABLE tb_guestbook                             -- 테이블 'tb_guestbook'에 아래 내용을 추가하겠다
ADD CONSTRAINT fk_guestbook_member  -- 외래 키 제약 조건의 이름을 'fk_guestbook_member'라고 지정한다
FOREIGN KEY (writer)                                   -- 외래 키로 지정할 컬럼은 'writter'이다 (tb_guestbook 테이블 안의 컬럼)
REFERENCES tb_member(member_id);   -- 이 외래 키는 'tb_member' 테이블의 'member_id' 컬럼을 참조한다



-- ===================================
-- !!!!! 추가한 외래키 존재 여부 확인하는 방법 
-- information_schema, mysql, performance_schema
-- 시스템 데이터베이스 : 시스템이 운영한다.
USE information_schema;

SHOW tables;

SELECT * FROM tables;

SELECT TABLE_name FROM  information_schema.tables WHERE table_schema='sakila';

SELECT TABLE_name FROM  information_schema.tables WHERE table_schema='mydb2';

-- foreign key : key_column_usage
SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE table_schema = 'mydb2';

-- 추가 여부 확인하기   
SELECT 
    CONSTRAINT_NAME, 
    TABLE_NAME, 
    COLUMN_NAME, 
    REFERENCED_TABLE_NAME, 
    REFERENCED_COLUMN_NAME
FROM 
    information_schema.KEY_COLUMN_USAGE
WHERE 
    TABLE_SCHEMA = 'mydb2' 
    AND TABLE_NAME = 'tb_guestbook'
--     AND REFERENCED_TABLE_NAME IS NOT NULL;

-- 엔티티관계도(다이어그램)에도 변경내용이 반영됩니다.

-- ===================================
-- 키에 대해서 건드려보기 

use mydb2;

-- !!! FOREIGN KEY 삭제하기  
alter table tb_guestbook 
drop foreign key fk_guestbook_member;

-- 삭제 여부 확인하기  
SELECT 
    CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM 
    information_schema.KEY_COLUMN_USAGE
WHERE 
    TABLE_SCHEMA = 'mydb2' 
    AND TABLE_NAME = 'tb_guestbook'
--     AND REFERENCED_TABLE_NAME IS NOT NULL;

    -- or 다양한 확인 방식 
select CONSTRAINT_NAME from information_schema.key_column_usage 
where table_schema='mydb2'
										AND TABLE_NAME = 'tb_guestbook';
   
 -- FOREIGN KEY 또 다시 추가해보기 
alter table tb_guestbook 
add constraint fk_guestbook_member 
foreign key (writer) 
references tb_member(member_id);


-- 
select * from tb_member;     -- 여기는 1번 값이 있는상태 
select * from tb_guestbook;   -- 여기는 현재 값이 없는 상태 

-- tb_guestbook 테이블에  insert
insert into tb_guestbook (title, writer, contents, regdate)
values('제목1', 1, '내용1', now()); 

select * from tb_member;
select * from tb_guestbook;  -- 추가된 값 확인 가

-- foreign key로 인해 에러발생 
insert into tb_guestbook (title, writer, contents, regdate)
values('제목2', 2, '내용2', now());

select * from tb_member;











