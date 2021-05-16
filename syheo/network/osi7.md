# OSI 7 계층

# 한 문장 정리‼️

OSI 7 계층은 네트워크 통신 접속~완료까지의 과정을 7단계로 표현한 것입니다.

송신 측에서는 캡슐화를, 수신 측에서는 디캡슐레이션을 진행합니다.

---

# 0. OSI 7 계층이란?

OSI (Open System Interconnection) 7계층은 국제 표준화 기구(ISO)에서 개발한 모델로서, **네트워크 프로토콜 디자인**과 **통신**을 계층으로 나눠서 설명한 것.

네트워크 통신 접속에서 완료까지의 과정을 7단계로 정의한 것.

→ **송신** 측에서는 헤더를 붙이는 **캡슐화**를 하여 진행되고, **수신** 측에서는 헤더를 떼는 **디캡슐레이션**을 진행.

![Untitled 1](https://user-images.githubusercontent.com/42290273/116803765-6af5de00-ab55-11eb-9e71-80738529756d.png)

![Untitled](https://user-images.githubusercontent.com/42290273/116803791-70532880-ab55-11eb-851a-7aa29332f0de.png)

# 1. OSI 7 계층 구조

### 1. 물리계층

전송하는데 필요한 기능을 제공함. 

→ 통신 케이블을 통해 전기 신호를 이용하여 비트 스트림을 전송함.

장비 : 통신 케이블, 허브

### 2. 데이터 링크 계층

송/수신을 확인. MAC Address를 가지고 통신함.

→ 데이터 전송 오류 감지, 재전송 기능 

장비 : 브릿지, 스위치

### 3. 네트워크 계층

패킷을 네트워크 간의 IP를 통하여 데이터를 전달함.

→ 전송 데이터를 목적지까지의 경로를 찾아 전송함.

→ 주소(IP)를 정하고, 경로(Route)를 선택하고, 패킷을 전달하는 것이 제일 핵심.

→ 네트워크 라우팅 기능

장비 : 라우터

### 4. 전송 계층

두 호스트 시스템으로부터 발생하는 데이터의 흐름을 제공함.

→ 보통 TCP 프로토콜을 자주 사용함.

→ 헤더에 송,수신지 포트번호를 포함하여 전달하는 계층.

→ 데이터의 전송단위.

→ TCP : 세그먼트 , UDP : Datagram

### 5. 세션 계층

통신 시스템 사용자간의 연결을 유지 및 설정함.

→ 세션을 만들고 유지, 세션 종료, 전송 중단 시 복구 기능이 있음.

→ 여기서 TCP/IP 세션을 만들고 없앰. 

→ 통신 연결은 포트 기반으로 구성. **OS가 세션 계층에 속함.**

→ OS(운영체제)가 세션 확립, 유지, 중단 기능을 해줌.

### 6. 표현 계층

세션 계층 간의 주고받는 인터페이스를 일관성 있게 제공함.

→ 응용계층으로부터 전달받거나 전송하는 데이터의 인코딩 및 디코딩이 이루어짐.

→ 응용 프로그램이 Data를 이해할 수 있게 응용 프로그램에 맞춰 변환. ex) JPEG,MPEG,GIF, TIFF 

### 7. 응용 계층

사용자가 네트워크에 접근할 수 있도록 서비스를 제공함.

→ 사용자에게 보이는 유일한 계층