# Access Modifier(접근 제어자)

# 한줄 정리‼️

---

**접근 제어자** 

접근 제어자는 **객체**에 대한 **외부의 접근을 제한**하는 역할을 합니다. 

# 0. 접근제어자(Access Modifier)이란?

---

개발자가 의도한 방식대로 프로그램이 작동되게 하기 위해선 **내부 동작을 외부에서 건드는 일을 최소화**해야한다. 

이 것을 위해 **객체지향 프로그래밍(OOP)**에서는 **캡슐화**(Encapsulation)이라는 개념이 적용되었는데 캡슐화를 위해 Java에서는 **접근제어자**(Access Modifier)을 사용한다. (제어자인데 왜 Controller라고 하지 않았을까..? 개인적인 생각이지만 "수정에 대한 접근"이 더 근접한 의미이기 때문인 것 같다ㅋㅋ)

**접근 제어자**는 클래스 멤버(필드, 메서드) 혹은 클래스에 사용되며 객체로의 외부에서의 접근을 제한하는 역할을 합니다. 

# 1. 접근제어자의 역할

---

접근제어자는 생략가능하며 생략했을 때는 자동으로 `default` 접근제어자로 설정됩니다. → 이말인 즉슨, default일 땐 접근제어자를 지정할 필요가 없다는 뜻.

📍**[CF] package 접근제어자와 동일하다!** 

**접근 제어자가 사용될 수 있는 곳**

---

- Class
- Member Field
- Member Method
- Constructor

**접근 제어자의 접근 범위** 

---

- 1) `private` : 같은 클래스 내에서만 접근 가능.
- 2) `default` : (같은 패키지) + 같은 패키지 클래스 내에서만 접근 가능
- 3) `protected` : (같은 클래스) + (같은 패키지) + 자신을 상속받은 자손 클래스에서만 접근 가능
- 4) `public` : 자유롭게 접근 가능

[접근 제어자 접근 범위](https://www.notion.so/1feed1b52d434adb84d3b13024df3ccd)

- 접근 범위 : private < default < protected < public 순으로 많은 접근을 허용합니다.

대상에 따라 **사용가능한 접근 제어자  && 키워드** 

---

- **Class** : public , (default), final, abstract
- **Method** : public, protected, (default), private, final, abstract, static
- **Variable** :  public, protected, (default), private, final, static
- **local Variable** : static

**제어자 조합에서 사용할 때 주의할 사항**

---

1) 메서드에 `**static**` 과 `**abstract**` 을 함께 사용할 수 없다.

: `**static**` 메서드는 구현이 있는 메서드에서만 사용할 수 있기 때문이다.

2) 클래스에 `**abstract**` 와 `**final**`을 동시에 사용할 수 없다.

: 클래스에 사용되는 `**final**`은 클래스를 확장할 수 없다는 의미, `**abstract**` 는 상속을 통해서 완성되어야 한다는 의미므로 서로 모순적인 개념입니다. 

3) `**abstract**` 메서드의 접근 제어자가 `**private**` 일 수는 없다.

: `**abstract**` 메서드의 구현부를 자손 클래스에서 구현하기 위해선 접근해야 하기 때문입니다.

4) 메서드에 **`private`**와 **`final`**을 같이 사용할 필요는 없다.

: 접근제어자가 `**private**` 인 메서드는 오버라이딩 될 수 없기 때문입니다. 이 둘 중 하나만 사용해도 의미가 충분합니다. 

# 참고자료

---

[[JAVA] 접근제어자 (Access Modifier)](https://88240.tistory.com/448)

[객체의 캡슐화(Encapsulation), 접근제어자](https://siyoon210.tistory.com/33)

[JAVA 기본 접근제어자 - default 이란? / 접근 권한 / 예제](https://gocoder.tistory.com/1841)