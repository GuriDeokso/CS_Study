# 탬플릿 메소드 패턴

# 한 문장 정리‼️

### 템플릿 메소드 패턴

특정 작업을 처리하는 일부분을 **서브 클래스로 캡슐화**하여 전체적인 구조는 바꾸지 않으면서 특정 단계에서 수행하는 내용을 바꾸는 패턴입니다.

---

# 0. 템플릿 메소드 패턴(Template Method Pattern)

템플릿 메소드 패턴이란 특정 작업을 처리하는 일부분을 서브 클래스로 캡슐화하여 전체적인 구조는 바꾸지 않으면서 특정 단계에서 수행하는 내용을 바꾸는 패턴

- 디자인 패턴이라고 하기도 뭐할정도로 객체지향 언어로 개발을 하다보면 무의식적으로 사용하는 패턴
- 주로 개발을 하다보면 구체적인 구현은 다르지만 기본적인 기능은 비슷한 경우가 종종 있음
- 예를 들면 HTTP와 SMTP Client 프로그램의 경우, 주고받는 메시지의 내용이 서로 다를 뿐 둘 다 인터넷 프로토콜을 이용하여 서버에게 요청을 전달하고 결과를 수신한다는 점에서 동일
- 이처럼 두개 이상의 프로그램이 기본적으로 동일한 골격 하에서 동작할때 기본 골격에 해당하는 알고리즘은 일괄적으로 관리하면서 각 프로그램마다 달라지는 부분들에 대해서는 따로 만들고 싶을때 템플릿 메소드 패턴을 사용하면 좋음.

![template_method_pattern](./image/template_method_pattern.png)

- 템플릿 메소드 패턴은 알고리즘의 구조를 메소드에 정의하고, 하위 클래스에서 알고리즘 구조의 변경없이 알고리즘을 재정의함.
- 알고리즘이 단계별로 나누어지거나, 같은 역할을 하는 메소드이지만 여러곳에서 다른 형태로 사용이 필요한 경우 유용하며 상속을 통해 슈퍼 클래스의 기능을 확장이 용이함.
- 변하지 않는 기능은 슈퍼 클래스에 만들어두고 자주 변경하며 확장할 기능은 서브 클래스에서 만들도록 함.

# 1. 템플릿 메소드 패턴 장단점

### 장점

**1.** 중복코드를 줄일 수 있다.

**2.** 자식 클래스의 역할을 줄여 핵심 로직의 관리가 용이하다.

**3.** 좀더 코드를 객체지향적으로 구성할 수 있다.

### 단점

**1.** 추상 메소드가 많아지면서 클래스 관리가 복잡해진다.

**2.** 클래스간의 관계와 코드가 꼬여버릴 염려가 있다.

# 2. 사용 예제

```java
//추상 클래스 선생님
abstract class Teacher{
	
    public void start_class() {
        inside();
        attendance();
        teach();
        outside();
    }
	
    // 공통 메서드
    public void inside() {
        System.out.println("선생님이 강의실로 들어옵니다.");
    }
    
    public void attendance() {
        System.out.println("선생님이 출석을 부릅니다.");
    }
    
    public void outside() {
        System.out.println("선생님이 강의실을 나갑니다.");
    }
    
    // 추상 메서드
    abstract void teach();
}
 
// 국어 선생님
class Korean_Teacher extends Teacher{
    
    @Override
    public void teach() {
        System.out.println("선생님이 국어를 수업합니다.");
    }
}
 
//수학 선생님
class Math_Teacher extends Teacher{

    @Override
    public void teach() {
        System.out.println("선생님이 수학을 수업합니다.");
    }
}

//영어 선생님
class English_Teacher extends Teacher{

    @Override
    public void teach() {
        System.out.println("선생님이 영어를 수업합니다.");
    }
}

public class Main {
    public static void main(String[] args) {
        Korean_Teacher kr = new Korean_Teacher(); //국어
        Math_Teacher mt = new Math_Teacher(); //수학
        English_Teacher en = new English_Teacher(); //영어
        
        kr.start_class();
        System.out.println("----------------------------");
        mt.start_class();
        System.out.println("----------------------------");
        en.start_class();
    }
}
```

---

### 참고 사이트

[[Design Pattern] 템플릿 메소드 패턴(Template Method Pattern)에 대하여](https://coding-factory.tistory.com/712)
