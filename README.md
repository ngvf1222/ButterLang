`python index.py <code> [입력 파일(선택사항)]`

숫자에 대한 표현식은 ?와 !,그리고 변수명으로 구성됩니다.
| 표현 | 의미 |
|--|--|
|!|+1|
|?|-1|

또한 변수명으로 변수 값을 참조할떄는 단독으로 앞에 띄어쓰기가 붙게 됩니다.

이떄 변수 앞에는 띄어쓰기가 필요합니다.
(추후 변수 연산 추가할 예정)

출력에 경우에는 처음에는 문자 출력이며 추후 숫자출력과 전환가능합니다.

| 명령어                                                                                         | 의미                                            | 현재 상태              |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------- |
| 마, 맛있는 거요? 뭔데요? 고구마? 빵? 고기? (변수명)?                                           | chr 타입 input                                  | <ul><li>[x] </li></ul> |
| (변수명) 못 참으면 뭐?                                                                         | int 타입 input                                  | <ul><li>[x] </li></ul> |
| (변수명) 버터 바보야...?                                                                       | bool 타입 input                                 | <ul><li>[x] </li></ul> |
| 따지고 보면 다 너 떄문이야!                                                                    | 문자출력<->숫자출력 전환                        | <ul><li>[x] </li></ul> |
| (표현식)이 또 되도않는 헛소리를 뱉고 있잖아(표현식)                                            | 표현식의 값을 n번으로 출력(stdin,stdout,stderr) | <ul><li>[x] </li></ul> |
| 이제부터 ~는 ~ 채로 영원히 사는 거야                                                           | 상수 선언                                       | <ul><li>[x] </li></ul> |
| 분위기 파악 개 못하네                                                                          | 함수 정의 시작                                  | <ul><li>[x] </li></ul> |
| 이러니까 (함수명)나 차리고 앉아 있어요~                                                        | 함수 정의 끝                                    | <ul><li>[x] </li></ul> |
| 나는 이만 간다                                                                                 | ret                                             | <ul><li>[x] </li></ul> |
| 트릭컬을 서비스 종료                                                                           | exit 함수 **객체**                              | <ul><li>[x] </li></ul> |
| ~시킬 것이다!                                                                                  | 함수 호출                                       | <ul><li>[x] </li></ul> |
| (변수명) 푼수 요정/유령/마녀/엘프/정령/수인/용족이에용                                         | 변수 정의                                       | <ul><li>[x] </li></ul> |
| (변수명)은/는 친구 아니야!                                                                     | 변수 할당 해제                                  | <ul><li>[x] </li></ul> |
| (변수명)을/를 한 방에 다 정리해버리고                                                          | 변수를 0으로 초기화                             | <ul><li>[x] </li></ul> |
| (변수명) 닥쳐(표현식)                                                                          | 변수를 n으로 설정                               | <ul><li>[x] </li></ul> |
| (변수명) 후우...(표현식)                                                                       | 변수에n을 더합니다.                             | <ul><li>[x] </li></ul> |
| (표현식)도록                                                                                   | n이 0이라면(if) 시작                            | <ul><li>[x] </li></ul> |
| 이게 진짜!                                                                                     | if문 끝                                         | <ul><li>[x] </li></ul> |
| 큭큭                                                                                           | 타 언어의 //                                    | <ul><li>[x] </li></ul> |
| 이제 모두 반성의 시간을 가질테니 얌전히 있도록(표현식)                                         | n ms만큼 sleep                                  | <ul><li>[x] </li></ul> |
| 버터는 친구들이 웃는게 좋아! 나도 웃는게 좋아! 같이 산책하는 것도 좋아! 밥먹는 것도 좋아, 헤헤 | flag: error시 로그에 기록+정지                  | <ul><li>[x] </li></ul> |
| 버터는 친구들을 돕는게 좋아! 그냥 하면 돼!                                                     | flag: error시 로그에만 기록                     | <ul><li>[x] </li></ul> |

---

<details>
<summary>추가할지 고민되는거</summary>

바보 바부 하지마요!

야, 나와

나오라고..

아~ 여기 다 모여있었네.

여기 있는 나약한 녀석들

버터는 엘리아스 최강자가 될 거야.

버터! 두 번쨰 섭종은 진짜 위험하다고!

씨끄러워! 맞아야 정신을 차리겠어?

(표현식)번 남았다

감히 이 버터님을 ~겠다?

~면서 말이지-> ~~비동기?~~

으윽... 머리가...

</details>
