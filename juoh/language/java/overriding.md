# Overriding vs Overloading

### 오버로딩

- 한 클래스 내에 같은 이름의 메서드를 여러 개 정의하는 것을 오버로딩이라 한다.
    - 메서드 이름이 같아야 한다
    - 매개변수의 개수 또는 타입이 달라야 한다.
    - 반환 타입은 영향 x

        ```java
        // 오버로딩 x,
        int add(int a, int b) {}
        long add(int x, int y) {}

        // 어떤 메서드가 호출된 것인지 결정할 수 없다
        add(5,3)
        ```

    - 매개변수의 타입과 개수가 같고 매개변수의 이름만 다르다면 동일한 메서드로 간주

        ```java
        // 오버로딩 x
        int add(int a, int b) {}
        int add(int x, int y) {}

        ```

- 장점
    - 하나의 이름으로 정의 가능 → 같은 기능으로 쉽게 예측가능(다형성?)
    - 메서드의 이름 절약 가능

### 가변인자와 오버로딩

- 가변인자는 내부적으로 배열을 이용하여 메서드 호출할 때마다 배열이 새로 생성된다(비효율 알아두기)

```java
String concatenate(String... str) {
}

System.out.println(concatenate());                         // 인자 없음
System.out.println(concatenate("a"));                      // 인자 하나
System.out.println(concatenate("a", "b"));                 // 인자 둘
System.out.println(concatenate(new String[] {"A", "B"}));  // 배열도 가능
```

- 매개변수의 타입을 배열로 하는 것과 가변 인자와 어떤 차이?
    - 매개변수 타입을 배열로 하면 반드시 인자를 지정해 줘야하기 때문에 인자 생략 X

```java
String concatenate(String[] str) {}

System.out.println(concatenate(new String[0]));            // 인자로 길이 0 배열
System.out.println(concatenate(null));                     // 인자로 null
System.out.println(concatenate());                         // 에러, 인자 필요
```

- 가변인자 오버로딩 주의점
    - 가능하면 가변인자를 사용한 메서드는 오버로딩 x

```java
static String concatenate(Stirng delim, String... args) {}
static String concatenate(String... args) {}

// reference to concatenate is ambiguous error
// 두 메서드 구분 x
concatenate("-", "100", "200")

```

### 오버라이딩

- 조상 클래스로부터 상속받은 메서드의 내용을 변경하는 것을 오버라이딩이라고 한다.
- ovveride: ~위에 덮어쓰다
- 조건 - 자손클래스에서 오버라이딩하는 메서드는 조상 클래스의 메서드와
    - 이름이 같아야 한다.
    - 매개변수가 같아야 한다.
    - 반환타입이 같아야 한다.
- 즉 선언부가 서로 일치해야 한다.
- 접근자와 예외는 제한된 조건하에서만 다르게 변경 가능
    1. 접근 제어자는 조상 클래스의 메서드보다 좁은 범위로 변경 할 수 없다.
        - 만약 조상 클래스 메서드의 정의된 접근 제어가 protected라면 이를 오버라이딩하는 자손 클래스의 메서드는 접근 제어자가 protected나 public이어야 한다.
        - 넓은 것에서 좁은 순: public - protected - (default) - private
    2. 조상 클래스의 메서드보다 많은 수의 예외를 선언할 수 없다.

        ```java
        class Parent {
        		void parentMethod() throws IOException, SQLException {}
        }

        // ok
        class Child extends Parent {
        		void parentMethod() throws IOException {} 
        }

        // error
        // Exception은 모든 예외의 최고 조상이므로 가장 많은 개수의 예외를 던진 것
        class Child extends Parent {
        		void parentMethod() throws Exception {} 
        }
        ```

    3. 인스턴스 메서드를 static 메서드로 또는 그 반대로 변경할 수 없다.
        - 만약 조상 클래스에 정의된 static 메서드를 자손 클래스에서 똑같은 이름의 static 메서드로 정의할 수 있나요?
            - okay,
            - 하지만 이것은 각 클래스에 별개의 static 메서드를 정의한 것일 뿐 오버라이딩이 아니다.
            - 각 메서드는 클래스 이름으로 구별될 수 있으며 '클래스이름.메서드이름()'으로 호출하는 것이 바람직
            - static 멤버들은 자신들이 정의된 클래스에 묶여있다고 생각하는 것이 좋음
- 아래의 메서드는 오버라이딩일까??

    ```java
    static Barista makeCoffe(CoffeMachine<Arabica> machine) {
    	String tmp;
    	for(Bean b : machine.getList()) tmp += b + " ";
    	return new Barista(tmp);
    }
    static Barista makeCoffe(CoffeMachine<Robusta> machine) {
    	String tmp;
    	for(Bean b : machine.getList()) tmp += b + " ";
    	return new Barista(tmp);
    }
    ```

### 오버로딩 vs 오버라이딩

- 오버로딩: 기존에 없는 새로운 메서드를 정의하는 것, new
- 오버라이딩: 상속받은 메서드의 내용을 변경하는것, change/modify

```java
class Parent {
		void parentMethod() {}
}

class Child extends Parent {
		void parentMethod() {}       // 오버라이딩
		void parentMethod(int i) {}  // 오버로딩

		void childMethod() {}
		void childMethod(int i) {}   // 오버로딩
		void childMethod() {}        // error, 중복정의
}
```

## 참고 출처

- [https://github.com/castello/javajungsuk3](https://github.com/castello/javajungsuk3)