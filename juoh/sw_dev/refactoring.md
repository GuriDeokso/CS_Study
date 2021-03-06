# 리팩토링

### 한문장 정리

- 리팩토링이란 외부 동작(기능)은 그대로 둔 채, 내부의 코드를 정리하며 개선하는 것

### 리팩토링이란

- Refactoring은 외부 동작을 바꾸지 않으면서 내부 구조를 개선하는 방법으로, SW 시스템을 변경하는 프로세스이다.
- Refactoring시 중요한 점
    - 소프트웨어를 보다 이해하기 쉽고, 수정하기 쉽도록 만드는 것, 겉으로 보이는 소프트웨어의 기능을 변경하지 않는 것이다.
    - 따라서, Refactoring을 할 때는 기능을 추가해서는 안되고, 단지 코드의 구조에만 신경 써야 한다.
- Refactoring은 가동중인 프로그램을 취해서, 동작을 바꾸는 것이 아니라 우리가 빠른 속도로 개발 할 수 있도록 하는 특성을 좀 더 많이 주어, 프로그램의 가치를 높이는 것이다.

### **Refactoring을 언제 해야 하는가?**

- Refactoring을 위해 별도의 시간을 내는 것은 좋지 않다.
- Refactoring 자체를 목적으로 삼는 것이 아니라, 어떤 다른 것을 하기 위해 Refactoring을 하는 것이고, Refactoring은 그 다른 것을 하는데 도움을 준다.
- 삼진규칙 : 스트라이크 세 개면 Refactoring을 한다.
    - 어떤 것을 처음 할 때는, 그냥 한다.
    - 두번 째로 비슷 어떤 것을 하게 되면, 그냥 중복되도록 한다.
    - 세 번째로 비슷한 것을 하게 되면, 그때 Refactoring을 한다.
- 기능을 추가 할 때 Refactoring을 하라.
    - 수정 해야 할 코드에 대한 이해가 높아진다. 또한 기능 추가가 쉬운 디자인으로 바꿀 수 있다.
    - Two hats
        - 리팩토링을 할 때는 기능을 추가 x, 기능을 추가할 때는 리팩토링을  x

![image_1](./refactoring/refactoring_1.png)

- 버그를 수정해야 할 때 Refactoring을 하라.
- 코드 검토(Code Review)를 할 때 Refactoring을 하라.

### **Refactoring을 할 때의 문제점**

- Database
    - 대부분의 비즈니스 어플리케이션은 데이터베이스 스키마와 밀접하게 결합되어 있다. 데이터베이스 스키마와 객체 모델간의 종속(Dependency)를 최소화 하기 위해 계층 구조로 만들었다 하더라도, 스키마를 변경하려면 데이터를 마이그레이트 해야 하는데, 시간도 오래 걸리고 위험도 큰 작업이다.
- interface 변경
    - 객체의 중요한 점 중 하나로 인터페이스를 변경하지 않고 내부 구현을 바꿀 수 있다는 것이다.
    - 객체를 사용하는 부분을 변경하지 않고도 객체의 내부 구조를 안전하게 바꿀 수 있지만, 인터페이스를 변경하면 어떤 일이 발생할지 모르기 때문에 인터페이스를 유지하는 것은 중요하다. 하지만, 많은 Refactoring이 인터페이스를 변경 시킨다.
    - 그렇다면 언제 Refactoring을 하지 말아야 하는가?
        - 코드를 처음부터 다시 작성해야 할 때
            - 기존 코드가 너무 엉망이라 처음부터 다시 시작하는 것이 더 쉬운 경우가 있다. 하지만 이런 결정은 쉽게 내릴 수 없도 가이드라인도 없다.
        - 마감일이 가까울 때
            - Refactoring으로 얻는 생산성 향상은 마감일이 지난 다음에야 나타날 것이다.

### **어떤 것을 Refactoring 해야 하는가?**

- 중복된 코드 (Duplicated Code)
- 긴 메소드 (Long Method)
- 거대한 클래스 (Large Class)
- 긴 파라미터 리스트 (Long Parameter List)
- 확산적 변경 (Divergent Change)
- 산탄총 수술 (Shotgun Surgery)
- 기능에 대한 욕심 (Feature Envy)
- 데이터 덩어리 (Data Clump)
- 기본 타입에 대한 강박관념 (Primitive Obsession)
- Switch 문 (Switch Statements)
- 평행 상속 구조 (Parallel Inheritance Hierarchies)
- 게으른 클래스 (Lazy Class)
- 추측성 일반화 (Speculative Generality)
- 임시 필드 (Temporary Field)
- 메시지 체인 (Message Chains)
- 미들 맨(Middle Man)
- 부적절한 친밀 (Inappropriate Intimacy)
- 다른 인터페이스를 가진 대체 클래스 (Alternative Classes with Different Interface)
- 불완전한 라이브러리 클래스 (Imcomplete Library Class)
- 데이터 클래스 (Data Class)
- 거부된 유산 (Refused Bequest)
- 주석 (Comments)

### 클린코드와 리팩토링 차이

- 리팩토링이 좀 더 넓은 의미
- 클린 코드 : 가독성
- 리팩토링 : 클린 코드 기반 + 유지보수