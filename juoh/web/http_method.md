# HTTP METHOD

### 한문장 정리

HTTP 메소드(HTTP Method)를 이용해 클라이언트가 서버에 데이터를 전송하고, 반대로 서버에서 클라이언트로 데이터를 회신할 수 있다.

### 안전한 메서드

- HTTP 요청의 결과로 서버에 어떤 작용도 하지 않는다( 리소스를 변경 x)
- GET, HEAD, OPTIONS,
- 디버깅용 메서드 TRACE는 해당 X

### 멱등성

- 멱등성 : 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질을 뜻합니다.
- 메소드는 "오류 또는 만료 문제를 제외하고 동일한 요청의 부작용이 단일 요청의 부작용과 동일하다는 점에서 멱등 속성을 가질 수 있습니다

### 캐시 가능성

- 향후 재사용을 위해 이에 대한 응답을 저장할 수 있음을 나타낼 수 있다
- GET, HEAD, POST, patch
- 실제로는 get, head 정도만 캐시 사용
- post, patch의 경우 캐시 key 고려

![http_method_01](./juoh/image/http_method-01.jpg)

### 메서드 종류

get

- 요청받은 url의 정보를 찾아 응답, read

HEAD

- 리소스의 헤더 취득

post

- 요청 자원을 생성, create

put

- 요천 자원을 수정, update

patch

- 요청 자원을 일부 수정

delete

- 요청 자원을 삭제

options

- 웹서버에서 지원되는 메소드의 종류를 확인할 경우 사용.

connect

- 동적으로 터널 모드를 교환, 프락시 기능을 요청시 사용.

trace

- 원격지 서버에 루프백 메시지 호출하기 위해 테스트용으로 사용.

### HTTP STATUS

- 200 (해당 요청 수행 성공)
- 201 Created (PUT 메소드에 의해 서버에 파일 생성됨)
- 203 Non-authoritative information (서버가 클라이언트 요구 중 일부만 전송)
- 204 No content (성공은 했지만 전송할 데이터가 없는 경우)
- 400 Bad Request (사용자의 잘못된 요청을 처리할 수 없음)
- 401 Unauthorized (인증이 필요한 페이지를 요청한 경우)

- 403 Forbidden (접근 금지, 디렉터리 리스팅 요청 및 관리자 페이지 접근 등을 차단)
- 404 Not found, (요청한 페이지 보일수 없음)
- 500 Internal server error (내부 서버 오류)
- 503 Service unnailable (서비스 불가)
- 504 Gateway timeout (게이트웨이 시간초과)