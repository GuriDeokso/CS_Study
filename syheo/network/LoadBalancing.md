# 로드 밸런싱(Load Balancing)

# 한 문장 정리‼️

### 로드 밸런싱 (Load balancing)

서버에 가해지는 부하를 분산해주는 기술이나 장치로 증가한 트래픽을 대응하기 위해 Scale up이나 Scale out을 수행함.

---

# 0. 로드 밸런싱이란?

부하분산 또는 로드밸런싱은 컴퓨터 네트워크 기술의 일종으로 **중앙처리장치 혹은 저장장치와 같은 컴퓨터 자원들에게 작업을 나누는 것**을 의미함.

서버에 가해지는 부하(=로드)를 분산(=밸런싱)해주는 장치 또는 기술임.

사업의 규모가 확장되고, 클라이언트의 수가 늘어나게 되면 기존 서버만으로는 정상적인 서비스가 불가능하게 되는데, 이런 **증가한 트래픽에 대처할 수 있는 방법**은 크게 두 가지

- Scale up : **서버 자체의 성능**을 높이는 것
- Scale out : **여러 대의 서버**를 두는 것

Scale-out의 방식은 **여러 대의 서버로 트래픽을 균등하게 분산해주는 로드밸런싱**이 반드시 필요.

### 로드 밸런싱 알고리즘

- **라운드로빈**
    - 서버에 들어온 요청을 순서대로 돌아가며 배정하는 방식
    - 서버와의 연결이 오래 지속되지 않는 경우 적합.
- **가중 라운드로빈 방식**
    - 각 서버에 가중치를 매기고 **가중치가 높은 서버에 요청을 우선적으로 배정**하는 방식
    - 서버의 트래픽 처리 능력이 다른 경우 사용
- **최소 연결 방식**
    - 요청이 들어온 시점에 **가장 적은 연결 상태를 보이는 서버**에 트래픽을 배정하는 방식.
    - 서버에 분배된 트래픽들이 일정하지 않은 경우에 적합
- **IP 해시 방식**
    - 클라이언트의 **IP주소를 특정 서버로 매핑**하여 요청을 처리하는 방식사용자가 항상 동일한 서버로 연결됨.

---

### L4 로드 밸런싱

- **트랜스포트 계층**에서 로드를 분산함.
- TCP, UDP 포트 정보를 바탕으로 함.
- 데이터 안을 보지 않고 **패킷 레벨에서만 로드를 분산**하기 때문에 속도가 빠르고 효율이 높음
- 섬세한 라우팅이 불가능하지만 L7로드 밸런서보다 저렴.

### L7 로드 밸런싱

- **애플리케이션 계층**에서 로드를 분산함.
- HTTP 헤더, 쿠키 등과 같은 **사용자 요청을 기준**으로 특정 서버에 트래픽을 분산하는 것이 가능함.
- 즉, **패킷 내용을 확인**하고 그 내용에 따라 로드를 특정 서버에 분배하는 것이 가능
- 더 **섬세한 라우팅**이 가능하고, 비정상적인 트래픽을 필터링 할 수 있음.
- **패킷의 내용을 복호화 해야하기 때문에** 더 많은 비용이 든다.

[[란] L4 load balancer vs L7 load balancer 란?](https://velog.io/@makeitcloud/%EB%9E%80-L4-load-balancer-vs-L7-load-balancer-%EB%9E%80)

---

### 참고자료

[Load Balancing이란?](https://velog.io/@jisoo1170/Load-Balancing%EC%9D%B4%EB%9E%80)

[https://velog.io/@jisoo1170/Load-Balancing이란](https://velog.io/@jisoo1170/Load-Balancing%EC%9D%B4%EB%9E%80)