# final

# 한 문장 정리‼️

### final

변수를 선언할 때 초기값이 저장되면 최종적인 값으로 판단하고 프로그램 실행 도중에 수정할 수 없게 하는 키워드입니다.

---

# 0. final 이란?

final의 의미는 **최종적이란** 뜻을 가지고 있음.

final 필드는 초기값이 저장되면 **최종적인 값**이 되어 프로그램 실행 도중에 수정을 할 수 없음.

# 1. final 사용법

### final 필드

`final int number = 1; //final 타입 필드 [= 초기값];`

final 필드는 위와 같이 선언하며 final 필드의 초기값을 줄 수 있는 방법은 딱 두가지 방법밖에 없음. 

1. 필드 선언시 초기 값 설정.
    - 단순 값이라면 이 방법이 제일 간단함.
2. 생성자를 통해서 초기 값 설정.
    - 복잡한 초기화 코드가 필요하거나 객체 생성 시에 외부 데이터로 초기화를 시켜야한다면 생성자를 통해서 초기값을 부여하는 방법을 써야 함
    - 생성자는 final 필드의 최종 초기화를 마쳐야 하는데 만약 초기화가 되지 않은 final 필드가 있다면 컴파일 에러가 발생.

### final 객체

```java
class Company{
    String name = "회사명";

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

public class Final_ex {
    public static void main(String[] args) {
    	final Company company = new Company();
    	//company = new Company(); //객체를 한번 생성했다면 재생성 불가능
    	company.setName("ex회사"); //클래스의 필드는 변경가능
    }
}
```

객체 변수에 final로 선언하면 그 변수에 다른 참조 값을 지정할 수 없음!!

- 즉 한번 생성된 final 객체는 같은 타입으로 재생성이 불가능합니다.

객체자체는 변경이 불가능하지만 **객체 내부 변수는 변경 가능**!

- 단, 내부 변수가 final이 아닐 경우 ㅋ

### final 클래스

```java
//final 클래스
final class Company{
    String name = "회사명";
}

//상속 불가능
class A_Company extends Company{
	
}
```

클래스에 final을 사용하게되면 그 클래스는 최종상태가 되어 더이상 **상속이 불가능**함. final 클래스여도 필드는 **Setter함수를 통하여 변경은 가능.**

### final 메서드

```java
class Company{
	
    String name = "회사명";

    public final void print() {
        System.out.println("회사 이름은 :"+name+" 입니다.");
    }
}

class A_Company extends Company{
	
    String name = "a회사";
	
    //메서드 오버라이드 불가능
    public void print() {
		
    }
}
```

메서드에 final을 사용하게되면 상속받은 클래스에서 부모의 **final 메서드를 재정의 할 수 없음.**

자신이 만든 메서드를 변경할 수 없게끔 하고싶을때 사용되며 **시스템의 코어부분에서 변경을 원치 않는 메서드에 많이 구현**되어 있음.

### 메서드의 인자값에 final을 사용하는 경우

```java
class Company{
    String name = "회사명";

    public void setName(final String name) {
    	//name = "ex회사2"; //인자값으로 받은 final변수는 변경 불가능
        this.name = name;
    }
}

public class Final_ex {
    public static void main(String[] args) {
    	final Company company = new Company();
    	company.setName("ex회사");
    }
}
```

잘 사용하지는 않지만 코딩을 좀 더 명확하게 하고 싶은 경우 메서드의 인자값에 final을 사용하시는 분들이 종종 있음. 

final 필드와 마찬가지로 인자값에 final을 사용하는 경우 final 인자값의 변경이 불가능함.

# 2. 왜 자바에서 final 멤버 변수는 관례적으로 static 을 붙일까?

### 왜 final 변수는 꼭 static 인가

흔히 클래스의 멤버 변수를 상수(final)로 만들고자 할 땐, 클래스 상수(static fianl)로 만들어 주곤함. 왜?!

### final 키워드

final 키워드는 프로그래밍 언어에서 ‘constant’, ‘상수’와 같은 단어와 비교되는 단어

- final은 해당 entity가 오로지 한 번 할당될 수 있음을 의미!

### final의 쓰임새

- final 변수
    - 해당 변수가 생성자나 대입연산자를 통해 한 번만 초기화 가능함을 의미함.
    - 상수를 만들 때 응용함.
- final 메소드
    - 해당 메소드를 오버라이드하거나 숨길 수 없음을 의미함.
- final 클래스
    - 해당 클래스는 상속할 수 없음을 의미함.
    - 문자 그대로 상속 계층 구조에서 ‘마지막’ 클래스!!
    - 보안과 효율성을 얻기 위해 자바 표준 라이브러리 클래스에서 사용할 수 있는데, 대표적으로 `java.lang.System`, `java.lang.String` 등이 있음.

### 세부 분석

**1. final 멤버 변수가 반드시 상수는 아니다.**

왜냐면 final의 정의가 ‘상수이다’가 아니라 ‘한 번만 초기화 가능하다’이기 때문이다.

어느 클래스의 멤버 변수가 final일때 , 어떤 객체로 생성하냐에 따라 해당 final 변수에 다른 값들이 들어올 수 있음.

**2. private 메소드와 final 클래스의 모든 메소드는 명시하지 않아도 final 처럼 동작한다.**

왜냐면 오버라이드가 불가능하기 때문임.

- 참고: [jls-8.4.3.3](http://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.4.3.3)

하지만 private 메소드에 여전히 `final` 명시는 가능함. 

- private: 자식 클래스에서 안 보임. (오버라이드도 물론 금지)
- final: 자식 클래스에서 보이지만, 오버라이드가 금지.

### static 키워드

static 키워드는 프로그래밍 언어에서 ‘전역’, ‘정적’의 의미로 통용됨.

static은 해당 데이터의 메모리 할당을 **컴파일 시간에 할 것임을 의미함.**

- 이에 static 데이터는 **런타임 중에 필요할 때마다 동적으로 할당 및 해제되는 동적 데이터와는 기능과 역할이 구분됨**
- 동적 데이터와 달리, static 데이터는 프로그램 실행 직후부터 끝날 때까지 메모리 수명이 유지

### static 쓰임새

- static 멤버 변수
    - 클래스 변수라고 불림
    - 모든 해당 클래스는 같은 메모리를 공유
    - 특정한 인스턴스에 종속되지 않음.
    - 인스턴스를 만들지 않고 사용 가능함.
- static 메소드
    - 클래스 메소드라고도 부름.
    - 오버라이드 불가.
    - 상속 클래스에서 보이지 않음.
- static 블록
    - 클래스 내부에 만들 수 있는 초기화 블록.
    - 클래스가 초기화될 때 실행되고, `main()` 보다 먼저 수행됨.
- static 클래스
    - 일반적인 클래스, 즉 top-level 클래스에 적용하면 문법 오류.
        - 그러나 이것이 top-level 클래스가 `static`하지 않다는 뜻이 아님.
        - **뭔말이지**
    - 중첩 클래스(nested class)에만 사용할 수 있음.
        - static nested class: `static`으로 정의된 nested class
        - inner class: `static`으로 정의되지 않은(non-static) nested class
    - 부모 클래스의 멤버 필드 중에는 `static` 필드에만 접근할 수 있음.
    - 사실상 일반적인 top-level 클래스와 동일하게 동작하지만, 그 위치가 하나의 top-level 클래스 안에 들어있는 것.
        - 이것은 유사한 클래스 집합을 하나로 묶고, 클래스 패키징 구조를 편리하게 정리하는 테크닉으로 사용될 수 있음.
- static import
    - 다른 클래스에 존재하는 static 멤버들을 불러올 때 사용함.
    - 멤버 메소드를 곧바로 사용할 수 있음.

### 그래서 왜 static final을 쓸까?

==**클래스 멤버 변수를 final로 지정하는 의도의 확인**

그것은 클래스에서 사용할 해당 멤버 변수의 데이터와 그 의미, 용도를 고정시키겠다는 뜻.

해당 클래스를 쓸 때 변하지 않고 계속 일관된 값으로 쓸 것을 멤버 상수로 지정할 것임.

예

- 기독교 클래스에서 멤버변수 신의 이름은 하나님.
- 중학교 성적 클래스에서 과목 최대 점수 멤버변수는 항상 100

```java
public static final String NAME_OF_GOD = "하나님";
public static final int MAX_SUBJECT_SCORE = 100;
```

### final 멤버 변수에 static을 사용하지 않는 경우는?

각 인스턴스마다 서로 다른 final 멤버 변수를 생성자에서 초기화시키는 식으로 사용하는 경우에는 static을 사용하지 않음.

즉, 인스턴스를 생성할 때 

- 한번만 초기화 하고
- 쭉 변화 없이 사용할 경우.

**DI(Dependency Injection) 기법**을 사용해 클래스 내부에 **외부 클래스 의존성**을 집어넣는 경우가 그것.

대표적으로 **Spring** Framework가 있음.

```java
public class MovieRecommender {

    private final CustomerPreferenceDao customerPreferenceDao;

    @Autowired
    public MovieRecommender(CustomerPreferenceDao customerPreferenceDao) {
        this.customerPreferenceDao = customerPreferenceDao;
    }

    // ...
}
```

### static 멤버 변수에 final을 사용하지 않는 경우는?

이 역시 기술적으로 충분히 가능

명확한 목적이 있는 경우는 사용할 수 있음.

하지만 보통의 경우엔 좋은 코딩 관례(practice)로 보기 어려울 듯.

- static 필드는 클래스 스코프(범위)의 전역 변수라 볼 수 있음.
- final을 쓰지 않았다면 값이 얼마든지 바뀔 수 있는 상태이므로, 이를 mutable 하다고 말함.
- 이는 모든 클래스 인스턴스에서 접근하여 그 값을 변경할 수 있음을 의미하므로, 값을 추론하거나 테스트하기 어렵게 만들 것임.
- 또한 동시성 프로그래밍을 어렵게 만드는 요인이 됨.

---

### 참고 사이트

[](https://coding-factory.tistory.com/525)

[자바의 final 는 언제 사용할까?](https://blog.lulab.net/programming-java/java-final-when-should-i-use-it/)

[왜 자바에서 final 멤버 변수는 관례적으로 static을 붙일까?](https://djkeh.github.io/articles/Why-should-final-member-variables-be-conventionally-static-in-Java-kor/)