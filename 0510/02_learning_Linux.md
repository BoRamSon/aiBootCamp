## 🟢 관리자 권한으로 실행

- ls

- cat /etc/shells

- su
  - 비밀번호 입력...

안되면

- sudo passwd root

  - 비밀번호 변경 = qhfkal0513
    (이거는 단순 터미널의 명령어)

- su
  - 암호입력 : qhfkal0513

<br><br>

## 🟢 디렉토리 확인하기

- pwd (현재 폴더 관련 내용 확인)

- ls -l (디렉토리 내의 파일 목록보기, -l 은 자세히 보기)
- ls -al (.으로 숨겨진 것까지 볼 수 있습니다.)

- cd / (home 디렉토리로, 언제나 root(/)위치로 이동)
- cd /home
- cd softcream/ (softcream 디렉토리로 들어가기)

- cd .. (이전 디렉토리로 돌아가기, 상위 디렉토리로 나가기)
- cd ~ (내 홈으로 / 나의 계정명까지 간다.)

<br><br>

## 🟢 권한 관련 설명

### drwxr-xr-x

- d (디렉토리)
- rwx (소유권자 권한)
- r-x (그룹 권한)
- r-x (그룹 외 사람들)

<br><br>

## 🟢 디렉토리 만들기

- mkdir 디렉토리명

- su 내이름(softcream) (다시 root계정에서 나의 계정으로 돌아옴)

- cd ~ (여기 오면 나의 홈디렉토리라고 함.)

- mkdir test

- cd test/

- 한번에 여러개의 폴더 만들기

  - mkdir program ming/python/source
    - (이렇게 만들 수 없음 오류남)

- 원래는 하나씩 폴더를 만들어야 합니다.

  - mkdir programming
  - cd programming
  - mkdir python
  - cd python
  - mkdir source
  - cd source

- 한번에 여러개의 폴더 test 폴더에 만들기 / option 사용 ( -p)

  - mkdir -p program ming/python/source
  - ls (이걸 통해 만들어진 폴더를 확인 가능)

- 디렉토리에서 파일들 확인해보기

  - ls -am
  - la -al
  - 파란색은 폴더 디렉토리

<br><br>

## 🟢 스크립트에 대한 설명

- cat .bashrc (사용자 환경변수 설정하는 파일)

- 스크립트: 독자적인 번역기가 없는 언어를 스크립트라고 합니다.
  - 가장 유명한 자바스크립트로 번역기가 browser입니다.
  - 크롬을 만들다가 v8 엔진을 만들다가 괜찮아서 밖으로 뺍니다. 독립적인 언어가 된 것은 node.js 입니다.
  - 확장자가 .bat인 파일이 바로 스크립트 입니다.
    - 자주 사용하는 명령어들을 모아놓은 것.

<br><br>

## 🟢 디렉토리(폴더) 삭제해보기

- rmdir 디렉토리명 (디렉토리 안에 아무것도 없어야 삭제가 된다.)
- rmdir test
- rmdir programming (비어있는 디렉토리가 아니라서 삭제 불가)

- rm -r programming

  - r : recursive (전체 경로를 뒤지면서 삭제한다.)

- rm -ri program ming

  - i: 삭제 전에 하나하나 확인하고 삭제할지 물어봅니다.

- rm -rf programming
  - 파일 및 폴더 삭제
  - r : recursive (전체 경로를 뒤지면서 삭제한다.)
  - f : force (강제로)

<br><br>

## 🟢 born 쉘 사용해보기

- /bin/sh (born 쉘 실행 경로 안나오고, 히스토리도 안됨)

- whoami (나 누구임?)

- id (1000부터 시작합니다.)

- exit (이걸로 본쉘에서 나올 수 있음)

<br><br>

## 🟢 계정을 하나 만들어보자

- sudo useradd -m testuser (계정 생성은 관리자만 가능)
  - m : /home/user02 폴더를 만들어라

(비번 입력하라고해서 했는데... 왜 이렇게 비번이 각각 달라)

- cd /home
  - ls
    - 이렇게 만들어진 계정 폴더를 볼 수 있다.

(비번이 도대체 뭔데?)

- sudo passwd testuser

  - 신규 비밀번호 : qwer1234

- su testuser (이걸로 들어가면 본쉘이 기본으로 켜짐)

- passwd (비밀번호를 변경할 수 있다.)
  - 신규 비밀번호 : rewq4321
- date (날짜와 시간이 출력되는 것을 볼 수 있다.)

<br><br>

## 🟢 명령어를 알아볼 때

- man ls

- man cd

<br><br>

## 🟢 다시 또 파일 하나 만들기

- su softcream (나의 본계정에 돌아온다.)

- cd ~ (홈디렉토리로 온다.)

- mkdir test
- cd test
- touch linux.txt
- ls
- cat linux.txt
