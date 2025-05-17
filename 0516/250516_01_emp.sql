-- emp 테이블의 내용을 다 보여줌 - 14건
select * from emp;

-- 데이터 전체 몇건인가??? 
select count(*) from emp; 

-- * : 아스테리스크 모든 필드
select empno, enamem, job from emp

--  aliasing - 별명지정하여 테이블을 수정해서 부를 수 있다.
select empno, enamem, job 
from emp as e;

-- 이렇게 aliasing을 통해서 만들면 빨라집니다!!!
-- information_schema 디비에 사용자가 만드는 테이블 정보가 저장된다. 
-- aliasing 안쓰면 저 디비 다 검색해서 정보를 읽어오고, aliasing을 하면 임시로 후다닥 읽어옵니다(cashing)
-- 디비정보를 메리에 붙러놓고 작업 속도가 유리하다
select e.empno, e.enamem, e.job 
from emp as e;

-- as 생략 가능 / count(필드명) 대부분의 dbms는 null값이 있을 경우 카운트 안함
-- 있을 경우, 카운트 안함
-- count(*) - 필드중에 null 값이 아예 없는 필드를 기준으로 제일 많은 데이터 카운트를 가져와라
select count(e.comm) from emp e;

/*
	< null 값 >
    알 수 없음, 빈값이 아님. 
    파이썬의 경우는 None. 
    수학적으로 무한대의 의미를 갖는다. 
    null + 1  =>  null (무한대)
    null + 1  =>  null (무한대)
    
	(수학연산 다 가능 (+, -0, *, /, sin, cosin, tan, round .........)
    
    null값에 연산을 하면 결과는 null
    파이썬의 if문, 함수를 써서 처리가능
    DBMS의 쿼리는 AWSI 표준이 있어서 비슷한데 함수는 각자 다르다
	
    IFNULL(필드명, 기본값) 만일 필드명에서 값이 NULL이 아닌 값이 오면 그 값을 주고 NULL이면 기본값을 부여한다.	
*/

-- select empno, sal+comm from emp; 대문자로 해봅시다
-- SELECT EMPNO, sal, comm, SAL+COMM FROM EMP;


-- 연산을 통해서 새로운 컬럼을 만들었음, 수식이 필드명으로 나옴
-- 필드명도 aliasing을 통해서 다시 부여할 수 있음. 
select empno, sal, comm, sal+IFNULL(comm, 0) as totla_sal
from emp;



-- ==================================================
-- ==================================================
-- [ 문자 합치기 ]
-- 홍길동의 급여는 얼마입니다.
-- concat을 통해서 문자열을 합칠 수 있습니다.
select concat(ename, "님의 급여는", sal, "입니다.") as desc
from emp;



-- ==================================================
-- ==================================================
-- [ 조건절 ]
/*
select 필드들
from 테이블명
where 조건절   해당조건에 만족하는 데이터
		- 비교연산자 : =   !=   >    <    >=   <=  
		- 논리연산자 : and, or, not
        
*/

select * from emp;
-- 사람 이름이 ALLEN 사람
select * from emp where ename='allen';
select * from emp where ename = 'allen' or ename = 'WARD';
-- 대소문자 구분이 없다는 것을 알 수 있습니다. 



-- ==================================================
-- =================================================
-- <문제풀기>
-- 급여가 3000이상인 사원의 이름과 급여를 조회하시오
select * from emp;
select * from emp where sal >= 3000;

-- 직무가 MANGER 인 사람의 정보를 조회하시오
select * from emp where job = 'MANAGER';

-- 급여가 2000 이상 5000이하인 사원을 조회하시오
select * from emp where sal >= 2000 and 5000 >= sal;
-- between : oracle, mysql에서만 지원
select * from emp where sal between 2000 and 5000;

-- 커미션이 NULL이 아닌 사원을 조회하시오
-- null은 관계연산자가 아니라, is, is not 을 사용해야합니다.
select * from emp where comm is null; 
select * from emp where comm is not null; 

-- A로 시작하는 이름을 가진 사원을 조회하시오.
-- select * from emp where ename = 'A*';  이거 아닙니다.
-- ~ 로 시작하는 와일드카드와 like 연사자 _(한글자) %(여러글자) 를 사용해야합니다.
select * from emp where ename like 'A%';  -- A로 시작하는
select * from emp where ename like '%A';  -- A로 끝나는
select * from emp where ename like '%O%';  -- 이름 중간에 O가 들어가는 
select * from emp where ename like '_O%';  -- 두번째 O가 들어가는


-- 부서번호가 10, 20, 30 에 해당하는 사원을 조회하시오.
select * from emp where deptno = 10 or deptno = 20 or deptno = 30;
select * from emp where deptno in (10, 20, 30);
-- in으로 통해서 할 수 있습니다.
-- 오라클의 경우 500개 가능


-- in 연산자의 유용성
select empno from emp;
-- 7521, 7565, 7903, 7934
select empni
from emp
where empo in (7521, 7565, 7903, 7934);



-- 급여가 1000 미만이거나 커미션이 500초과인 사원을 조회하시오
select * from emp where sal < 1000 or comm > 500;

-- 관리자가 없는 사원을 mgr이 null을 조회하시오
select * from emp where mgr is null;

-- 직무가 CLERK 이면서 부서번호가 20인 사원을 조회하시오
select * from emp where job = 'CLERK' and deptno = '20';

-- 입사일이 1982년 이전인 사원을 조회하시오
select * from emp where hiredate <'1982-01-01';



-- ==================================================
-- ==================================================
-- 정렬
select *
from emp
-- where;
order by ename;  -- 이름으로 오름차순
-- order by 필드명 acs 또는 desc   이게 단순 내림차순 정렬


select *
from emp
order by ename desc;  -- 내림차순 정렬








