# 2DGP - 01  //  2012180039 장한식


### # 1. 게임의 소개


 - 제목 : Cross the Road
 - Copy 게임 : 길건너 친구들
 
   <img src="https://t1.daumcdn.net/cfile/tistory/2249FE3454E3777401" width="200" height="200">

 - 컨셉 : 기존의 ‘길건너 친구들’ 게임을 2D로 카피하며, 방향키를 이용해 상하좌우로 이동하여 좌우로 지나다니는 차량을 피해 길을 건너는 게임
 - 방법 : 방향키를 이용해 상하좌우로 이동하며, 지나다니는 차량을 피해 움직인다.


### # 2. 게임화면 예시

 <img src="https://postfiles.pstatic.net/MjAyMDEwMTJfMzMg/MDAxNjAyNDcxOTI5NTc3.DHtyYppF3wESoDkp0tJDnDnxRWCrP19eEy8HNij57I0g.piPql_wG50mkhD4cBcPA4il3Ly7JbJOiHPvhD-QCxi8g.PNG.hansik0806/image.png?type=w773">

### # 3. GameState (Scen)의 이름 및 설명
#####  - Loading State
 - 설명 : 게임 실행 시, 자동으로 재생되는 State
 - 화면에 표시할 객체들의 목록 : 로딩 이미지 or 영상
 - 처리할 키/마우스 등 이벤트 : 키보드 입력
 - 다른 State로 이동하는 조건 및 방법 : 


      a. 일정 시간 이후 자동으로 Menu State로 이동
      b. 키 입력 시 : Loading State 스킵 후 Menu State로 이동
  
##### - Menu State
- 설명 : 게임 실행, 나가기 버튼이 있는 State
- 화면에 표시할 객체들의 목록 : 게임 실행 버튼, 나가기 버튼, 메뉴_배경화면
- 처리할 키/마우스 등 이벤트 : 키보드 입력
- 다른 State로 이동하는 조건 및 방법 : 

      a. 게임 실행 버튼 선택 시 : Play State로 이동
      b. 나가기 버튼 선택 시 : 게임 종료

#### - Play State
- 설명 : 도로에 자동차가 좌우로 이동하며, 캐릭터를 이동해 자동차를 피해 목표지점으로 이동하는 State
- 화면에 표시할 객체들의 목록 : 캐릭터, 자동차, 게임_배경화면
- 처리할 키/마우스 등 이벤트 : 키보드 입력
- 다른 State로 이동하는 조건 및 방법 : 캐릭터가 차량과 충돌 시 Gameover State로 이동


#### - Gameover State
- 설명 : 게임화면 위에 메뉴가 출력되어 재시도, 나가기 버튼이 나오는 State
- 화면에 표시할 객체들의 목록 : 캐릭터, 자동차, 게임_배경화면
- 처리할 키/마우스 등 이벤트 : 키보드 입력 
- 다른 State로 이동하는 조건 및 방법 : 

      a. 재시작 버튼 선택 시 : Play State 재시작
      b. 나가기 버튼 선택 시 : 게임 종료
      

#### - 전체 State 다이어 그램
<img src="https://postfiles.pstatic.net/MjAyMDA5MjVfMjA3/MDAxNjAxMDE5ODQzNDQ3.ADAoGMF3rplZVZVY8w6CQ8085AqxA70t9mVAm0uEQjwg.tll8WpYrfXWfWgX2kfsQ4Iyilmhm52hUHngIYZmQdTAg.PNG.hansik0806/Dier.png?type=w773" width="50%" height="50%">


### # 4. 개발범위
|내용|최소 범위|추가범위|
|:-----------:|:---:|:---|
|캐릭터 컨트롤|키보드 방향키로 4방향 이동||
|맵|여러 개의 안전 구역과 도로 디자인, 화면에 안전 구역과 도로가 랜덤하게 출력|철도, 일정 점수마다 안전구역의 색 변경|
|차량|자동차의 종류와 크기, 랜덤한 차량의 속도, 도로마다 랜덤하게 차량의 방향이 지정됨|기차, 일정 점수마다 차량들의 속도 증가|
|게임기능|충돌 시 게임 종료, 앞으로 전진 시 점수 상승|맵에 철도가 랜덤으로 출력, 일시정지|
|애니메이션|캐릭터 이동, 차량 이동, 충돌 시 이펙트|
|사운드|캐릭터 이동 소리, 차량 이동 소리, 차량 경적, 배경음악 등|


### # 5. 개발일정
| 주차 |내용|상세내용|
|:------:|:---:|:---:|
|1주차|수집, 디자인|리소스 수집 / 안전구역, 도로 디자인|
|2주차|디자인, 출력, 좌표처리| 안전 구역, 도로 디자인 / 안전구역, 도로, 차량, 캐릭터의 크기 및 좌표 규정 / 캔버스 위에 캐릭터, 맵 출력|
|3주차|캐릭터 이동| 키보드 입력에 따른 캐릭터 이동 / ↑ 입력 : 맵 이동 / ←, → 입력 : 캐릭터가 좌우로 이동 / ↓ 입력 : 캐릭터 아래로 이동, 맵은 고정|
|4주차|랜덤 맵 생성 및 중간 점검| 캐릭터와 맵 끝의 거리를 계산해, 일정 거리 이하일 시 상단에 랜덤으로 맵 생성 / 중간 점검 / 1~4주차 간 부족한 점 보완|
|5,6 주차|차량 오브젝트, 충돌| 도로마다 랜덤하게 차량의 방향, 속도를 램덤하게 설정하여 이동 / 캐릭터와의 충돌 체크 결과에 따른 메뉴 출력|
|7주차|점수 시스템, 시작과 종료 처리, 밸런스| 캐릭터가 앞으로 전진할 시 점수 상승 / 실제적인 게임의 시작과 종료 처리, 스코어 화면 / 밸런스 조절|
|8주차|마무리|최종 점검 및 릴리즈|


### # 6. 출처
길건너친구들 화면 : https://gamejay.net/650
자동차 일러스트 : https://littledeep.com/car-illustration-free-download/
트럭 일러스트 : https://littledeep.com/%ed%8a%b8%eb%9f%ad-%ec%9d%bc%eb%9f%ac%ec%8a%a4%ed%8a%b8-png-ai-%eb%ac%b4%eb%a3%8c-%eb%8b%a4%ec%9a%b4%eb%a1%9c%eb%93%9c/
버스 일러스트 : https://www.pngwing.com/ko/free-png-basol


### # 7. 필요한 기술
 - 이 과목에서 배울 것으로 기대되는 기술 : 게임 중 일시 정지
 - 수업 에 다루어 달라고 요청할 기술 :
 Gameover State에서 필요한 부분인데 메뉴가 출력될 때 메뉴 화면 뒤에 출력되고 있는 Play State를 흐리게 혹은 색상을 조정해 흐리게 보이는 기술
