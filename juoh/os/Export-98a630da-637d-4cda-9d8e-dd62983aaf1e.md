# 운영체제란

## 한문장 정리

- 일반적으로 `하드웨어를 관리하고, 응용 프로그램과 하드웨어 사이에서 인터페이스 역할을 하며 시스템의 동작을 제어하는 시스템 소프트웨어`
- 컴퓨터와 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트 계층
- 운영체제는 컴퓨터의 성능을 높이고(performance), 사용자에게 편의성 제공(Convenience)을 목적으로 하는 컴퓨터 하드웨어 관리하는 프로그램이다.

## 운영체제란

- the one program running at all times on the computer
- usually called the kernel.

![image_1](./Export-98a630da-637d-4cda-9d8e-dd62983aaf1e/Export-98a630da-637d-4cda-9d8e-dd62983aaf1e_1.png)

## 운영체제의 역할

- User interface
- Program execution
- I/O operation
- File-system manipulation
- Communications
- Error detection
- Resource allocation
- Logging
- Protection and security

## 멀티프로세싱

- 멀티 프로세싱은 다수의 프로세서가 서로 협력적으로 일을 처리하는 것을 의미한다.

## 멀티프로그래밍

- 특정 프로세스 A에 대해서 프로세서가 작업을 처리할때 낭비되는 시간동안 다른 프로세스를 처리하도록 하는 것
- runs more than one program at a time
- keeps several processes in memory simultaneously.
- to increase CPU utilization.

## 멀티태스킹(시분할)

- a logical extension of multiprogramming.
    - in which CPU switches jobs so frequently that
    - users can interact with each job while it is running.
- CPU scheduling
    - If several processes are ready to run at the same time,
    - the system must choose which process will run next
- 멀티프로그래밍과의 차이
    - 멀티프로그래밍은 프로세서의 자원이 낭비되는 것을 최소화하기 위한 것
    - 멀티테스킹은 일정하게 정해진 시간동안 번갈아가면서 각각의 Task를 처리하는 것

멀티쓰레딩

- 하나의 프로세스를 다수의 실행 단위로 구분하여 자원을 공유하고 자원의 생성과 관리의 중복성을 최소화하여 수행 능력을 향상 시키는 것