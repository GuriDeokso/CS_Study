# HTTP Method

# 한 문장 정리‼️

HTTP 요청 데이터에 **특정 동작을 수행**하도록 하기 위한 방법.

---

# 0. HTTP(Hyper Text Transfer Protocol)?

**인터넷**에서 **데이터**를 주고 받을 수 있는 프로토콜

**요청**과 **응답**을 통해 데이터를 주고 받음.

- stateless 프로토콜
    - **이전** 데이터 요청과 **다음** 데이터 요청이 서로 관련이 없음.
    - 서버는 세션과 같은 별도의 추가 정보를 관리하지 않아도 됨.
    - 다수의 요청 처리 및 서버의 부하를 줄일 수 있음.
- TCP/IP 통신 위에서 동작하며 기본 포트는 80번.

### HTTP Request

클라이언트가 HTTP Request 를 하는 쪽이며, 웹 브라우저가 그 역할을 함.
![Untitled](https://user-images.githubusercontent.com/42290273/116803749-5d405880-ab55-11eb-8e9d-26cb68aeaff3.png)

### HTTP Response

서버가 HTTP Response를 하는 쪽이며, 데이터를 보내주는 원격지의 컴퓨터가 그 역할을 함.

![Untitled 3](https://user-images.githubusercontent.com/42290273/116803752-616c7600-ab55-11eb-888b-86205cd887af.png)

### URL (Uniform Resource Locators)

서버에 자원을 요청하기 위해 입력하는 영문 주소.

숫자로 되어 있는 IP 주소보다 가독성이 좋아 사용.

![Untitled 2](https://user-images.githubusercontent.com/42290273/116803757-63ced000-ab55-11eb-9402-d98bff02f0c9.png)

url 구성 :

프로토콜 + 호스트 + 포트 + resource path + query

# 1. HTTP Method

URL을 이용하면 서버에 특정 데이터를 요청할 수 있음.

여기서 요청 데이터에 특정 동작을 수행하도록 하기 위해 HTTP Method를 사용함.

- **GET** : 존재하는 자원에 대한 **요청**
- **POST** : 새로운 자원을 **생성**
- **PUT** : 존재하는 자원에 대한 **변경**
- **DELETE** : 존재하는 자원에 대한 **삭제**

이와 같이 데이터의 CRUD를 HTTP Method로 정의할 수 있음.

기타 HTTP Method는 다음과 같음.

- **HEAD** : **서버 헤더 정보**를 획득. GET과 비슷하나 **Response Body를 반환하지 않음**
- **OPTIONS** : **서버 옵션들을 확인**하기 위한 요청. → CORS에서 사용

---

### HTTP Post와 Put 의 차이

**POST:  INSERT**

**PUT: UPDATE**

- POST는 멱등하지 않고 PUT은 멱등함.
    - 동일한 자원을 여러번 POST 하면 서버자원에는 변화가 생기지만, 여러번 PUT하는 경우는 변화가 생기지 않음.
    - POST의 경우 클라이언트가 리소스의 위치를 지정하지 않는 경우 사용됨. (/user)
    - 따라서, 아래와 같은 요청이 여러번 수행되는 경우 매번 새로운 user가 생성되어 user/3, user/4 등 매번 새로운 자원이 생성됨. → 멱등하지 않음.

### HTTP PUT과 PATCH의 차이

**PUT: 해당 자원의 전체를 교체**하는 의미

**PATCH: 일부를 변경한다는 의미**

최근 update 이벤트에서 PUT보다 더 의미적으로 적합하다고 평가받음. 

또한 PUT의 경우는 멱등하지만, PATCH의 경우는 멱등하지 않음.

- PUT은 전체 자원을 업데이트 하기 때문에 동일 자원에 대해서 동일하게 PUT을 처리하는 경우 **멱등하게 처리**
- 반면 PATCH로 처리되는 경우 자원의 일부가 변경되기 때문에 멱등성을 보장할 수 없다.
    - 만족하지 않는 케이스

        ```
        PATCH users/1
        {
            $increase: 'age',
            value: 1,
        }
        ```

### HTTP 멱등성

![Untitled 1](https://user-images.githubusercontent.com/42290273/116803758-64676680-ab55-11eb-94b9-d3d7222c596a.png)


멱등(idempotent)의 의미:  같은 작업을 계속 반복해도 같은 결과가 나오는 경우를 의미

- 동일한 자원에 대한 GET요청이라면 클라이언트에 반환되는 모든 응답은 동일해야 함.
- 특정 자원에 대한 DELETE의 경우도 자원은 더 이상 이용할 수 없어야 하며,
- DELETE요청을 다시 호출한 경우도 자원은 여전히 사용할 수 없는 상태여야 함.