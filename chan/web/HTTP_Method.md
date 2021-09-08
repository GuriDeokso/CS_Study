# HTTP Method

주어진 리소스에 대하여 수행하길 원하는 행동을 나타낸다.

## **GET**

서버에게 Resource를 보내도록 요청하는데 사용 (**서버의 Resource를 읽음**)

![https://miro.medium.com/max/521/1*8L6ByXBQAAcafj2dAk_z0Q.jpeg](https://miro.medium.com/max/521/1*8L6ByXBQAAcafj2dAk_z0Q.jpeg)

GET example

## **HEAD**

GET과 동일하지만 **서버에서 Body를 Return 하지 않음**

- Resource를 받지 않고 오직 찾기만 원할때
- object가 존재할 경우 응답의 상태 코드를 확인할때
- 서버의 응답 헤더를 봄으로써 Resource가 수정 되었는지 확인

![https://miro.medium.com/max/523/1*-R9pF0Hf13WUFVfFIMz8YA.jpeg](https://miro.medium.com/max/523/1*-R9pF0Hf13WUFVfFIMz8YA.jpeg)

HEAD example

## **PUT**

**서버에 문서를 쓸때 사용** (GET과 반대)

- PUT 메소드는 서버가 **Client 요청의 Body를 확인**한다.
- 요청된 URL에 정의된 새로운 Resource를 생성하기 위함
- 요청된 URL이 존재할 경우 대체하여 사용

![https://miro.medium.com/max/601/1*J5gbefuo4GJNaOGefscDAA.jpeg](https://miro.medium.com/max/601/1*J5gbefuo4GJNaOGefscDAA.jpeg)

PUT example

## **POST**

**Server에 Input Data를 보내기 위함** (HTML form에 많이 사용)

- PUT vs. POST

— PUT은 서버의 Resource에 Data를 저장하기 위한 용도

— POST는 서버에 DATA를 보내기 위한 용도

![https://miro.medium.com/max/455/1*Z_GYZfNkE7ow_u-HNC-q2A.jpeg](https://miro.medium.com/max/455/1*Z_GYZfNkE7ow_u-HNC-q2A.jpeg)

Method usage

![https://miro.medium.com/max/603/1*Rkb0kk5Ox1AOpGZH16fTKA.jpeg](https://miro.medium.com/max/603/1*Rkb0kk5Ox1AOpGZH16fTKA.jpeg)

POST example

## **TRACE**

Client로 부터 Request Packet이 방화벽, Proxy Server, Gateway등을 거치면서 packet의 변조가 일어날 수 있는데, 이 때 **Server에 도달 했을 때의 최종 Packet의 Request Packet을 볼수 있다**.

- 즉, **Original Data와 서버에 도달했을 때의 비교본 Data를 서버의 응답 Body를 통해 확인 할 수 있다.**
- 요청의 최종 수신자는 반드시 **송신자에게 200(OK) 응답의 내용(Body)로 수신한 메세지를 반송**해야 한다.
- **최초 Client의 요청에는 Body가 포함될수 없다.**

![https://miro.medium.com/max/601/1*jK-6lUNXucZN7hoZiXFZZw.jpeg](https://miro.medium.com/max/601/1*jK-6lUNXucZN7hoZiXFZZw.jpeg)

TRACE example

## **OPTION**

- Target Server의 지원 가능한 method*(ex> GET, POST …)*를 알아보기 위함

![https://miro.medium.com/max/580/1*ZwlnGLJiamd-7cOafCO9CA.jpeg](https://miro.medium.com/max/580/1*ZwlnGLJiamd-7cOafCO9CA.jpeg)

OPTION example

## **DELETE**

- **요청 Resource를 삭제**하도록 요청
- 그러나!! HTTP 규격에는 Client의 요청에도 서버가 무효화 시킬수 있도록 정의되어 있음
- DELETE Method는 항상 보장되지 않는다.

![https://miro.medium.com/max/589/1*ByBNzONHDPxiTg8saVbnEQ.jpeg](https://miro.medium.com/max/589/1*ByBNzONHDPxiTg8saVbnEQ.jpeg)

DELETE example

[간단정리]

**`[GET](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/GET):**GET` 메서드는 특정 리소스의 표시를 요청합니다. `GET`을 사용하는 요청은 오직 데이터를 받기만 합니다.

**`[HEAD](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/HEAD):**HEAD` 메서드는 `GET` 메서드의 요청과 동일한 응답을 요구하지만, 응답 본문을 포함하지 않습니다.

**`[POST](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/POST):**POST` 메서드는 특정 리소스에 엔티티를 제출할 때 쓰입니다. 이는 종종 서버의 상태의 변화나 부작용을 일으킵니다.

**`[PUT](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/PUT):**PUT` 메서드는 목적 리소스 모든 현재 표시를 요청 payload로 바꿉니다.

**`[DELETE](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/DELETE):**DELETE` 메서드는 특정 리소스를 삭제합니다.

**`[CONNECT](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/CONNECT):**CONNECT` 메서드는 목적 리소스로 식별되는 서버로의 터널을 맺습니다.

**`[OPTIONS](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/OPTIONS):**OPTIONS` 메서드는 목적 리소스의 통신을 설정하는 데 쓰입니다.

**[TRACE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/TRACE) :** `TRACE` 메서드는 목적 리소스의 경로를 따라 메시지 loop-back 테스트를 합니다.

**`[PATCH](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/PATCH):**PATCH` 메서드는 리소스의 부분만을 수정하는 데 쓰입니다.
