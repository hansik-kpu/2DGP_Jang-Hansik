#### # 1. 게임의 소개
 - 제목 : Cross the Street
 - Copy 게임 : 길건너 친구들
 
   <img src="https://t1.daumcdn.net/cfile/tistory/2249FE3454E3777401" width="200" height="200">

 - 목적 : 지나다니는 차량을 피해 길을 건너는 게임
 - 방법 : 방향키를 이용해 상하좌우로 이동하며, 지나다니는 차량을 피해 움직인다.

#### # 2. GameState (Scen)의 이름 및 설명
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

##### - Play State
- 설명 : 도로에 자동차가 좌우로 이동하며, 캐릭터를 이동해 자동차를 피해 목표지점으로 이동하는 State
- 화면에 표시할 객체들의 목록 : 캐릭터, 자동차, 게임_배경화면
- 처리할 키/마우스 등 이벤트 : 키보드 입력
- 다른 State로 이동하는 조건 및 방법 : 캐릭터가 차량과 충돌 시 Gameover State로 이동


##### - Gameover State
- 설명 : 게임화면 위에 메뉴가 출력되어 재시도, 나가기 버튼이 나오는 State
- 화면에 표시할 객체들의 목록 : 캐릭터, 자동차, 게임_배경화면
- 처리할 키/마우스 등 이벤트 : 키보드 입력 
- 다른 State로 이동하는 조건 및 방법 : 

      a. 재시작 버튼 선택 시 : Play State 재시작
      b. 나가기 버튼 선택 시 : 게임 종료
      
    
<img src="https://postfiles.pstatic.net/MjAyMDA5MjVfMjA3/MDAxNjAxMDE5ODQzNDQ3.ADAoGMF3rplZVZVY8w6CQ8085AqxA70t9mVAm0uEQjwg.tll8WpYrfXWfWgX2kfsQ4Iyilmhm52hUHngIYZmQdTAg.PNG.hansik0806/Dier.png?type=w773" >


 #### - 필요한 기술
 - 이 과목에서 배울 것으로 기대되는 기술 : 게임 중 일시 정지
 - 수업 에 다루어 달라고 요청할 기술 :
 Gameover State에서 필요한 부분인데 메뉴가 출력될 때 메뉴 화면 뒤에 출력되고 있는 Play State를 흐리게 혹은 색상을 조정해 흐리게 보이는 기술
