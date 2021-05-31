# TCP 3 way handshake & 4 way handshake

# 한 문장 정리‼️

TCP의 **연결성 서비스, 신뢰성 보장**을 위한 수단으로써, **세션을 성립**하고, **세션을 종료**하기 위한 절차이다.

---

# 0. TCP(Transmission Control Protocol)?

전송을 제어하는 프로토콜?!

**인터넷상에서** 데이터를 **메세지**의 형태로 보내기 위해 **IP**와 함께 사용하는 프로토콜

# 1. TCP 특징

- 연결형 서비스로 **가상 회선 방식**을 제공함.
    - TCP가 가상 회선 방식을 제공한다는 것 ==  발신지와 수신지를 연결하여 패킷을 전송하기 위한 논리적 경로를 배정한다.
- **3-way handshaking**과정을 통해 **연결을 설정**하고, **4-way handshaking**을 통해 **연결을 해제.**
    - 3-way handshaking과정은 목적지와 수신지를 확실히 하여 **정확한 전송을 보장**하기 위해서 **세션을 수립하는 과정**을 의미.
- 흐름 제어 및 혼잡 제어.
- 높은 신뢰성을 보장
    - TCP는 **연결형 서비스**로 신뢰성을 보장
    - 3-way handshaking의 과정이 신뢰성을 높임.
    - 신뢰성이 필요한 경우. 예를 들어 **파일 전송**시 주로 사용.
- UDP보다 속도가 느림.
    - 흐름 제어 및 혼잡 제어 → CPU 사용
- 전이중(Full-Duplex), 점대점(Point to Point) 방식.

# 2. TCP 3 way handshake

장치들 사이에서 논리적인 접속을 성립(establish)하기 위한 방법.

TCP/IP프로토콜을 이용해서 통신을 하는 **응용프로그램**이 **데이터를 전송하기 전에**

먼저 **정확한 전송을 보장**하기 위해 **상대방 컴퓨터와 사전에 세션을 수립하는 과정**을 의미.

→ TCP 연결을 초기화 

1. **Client > Server : TCP SYN  :** 너랑 ****연결한다~
2. **Server > Client : TCP SYN+ACK :** 알겟어 연결해~확인!
3. **Client > Server : TCP ACK :** 오케이 확인했다~!

SYN : **SYN**chronize sequence numbers

ACK : **ACK**nowledgement

![Untitled](https://user-images.githubusercontent.com/42290273/116803761-65989380-ab55-11eb-956e-86e715252c5b.png)

# 3. TCP 4 way handshake

TCP 4 way handshake는 세션을 종료하기 위한 절차임.

1. **Client > Server : FIN**  : 클라이언트 연결 종료한다~
2. **Server > Client : ACK** : 오케이 확인~ 일단 기달려봐 
3. **Server > Client : FIN** : 오케이 통신 종료~
4. **Client > Server : ACK** : 알겠다 확인~!

![Untitled 1](https://user-images.githubusercontent.com/42290273/116803760-64fffd00-ab55-11eb-9bfe-837d9fec6727.png)


### Server에서 FIN을 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN패킷보다 늦게 도착하는 상황이 발생한다면?

Client에서 세션을 종료시킨 후 뒤늦게 도착하는 패킷이 있다면 이 **패킷**은 **Drop되고 데이터는 유실**됨.

이러한 현상에 대비하여 **Client**는 Server로부터 FIN을 수신하더라도 **일정시간(디폴트 240초) 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정**을 거치게 되는데 이 과정을 **TIME_WAIT이라고 함.**
