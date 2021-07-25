# 싱글톤 패턴

한문장 정리

- 오직 한 개의 클래스 인스턴스만을 갖도록 보장하고, 이에 대한 전역적인 접근점을 제공

의도

- 오직 한 개의 클래스 인스턴스만을 갖도록 보장하고, 이에 대한 전역적인 접근점을 제공

동기

- 어떻게 하면 클래스의 인스턴스를 하나만 만들고, 해당 인스턴스에 쉽게 접근할 수 있을까?
    1. 전역 변수를 이용해서 해당 객체에 접근하도록 하면 가능
    2. 더좋은 방법: 클래스 자신이 자기의 유일한 인스턴스로 접근하는 방법을 자체적으로 관리(싱글턴 패턴)

활용성

- 싱글턴 패턴은 다음 상황에서 사용
    1. 클래스의 인스턴스가 오직 하나여야 함을 보장하고, 잘 정의된 접근점으로 모든 사용자가 접근할 수 있도록 해야 할 때
    2. 유일한 인스턴스가 서브클래싱으로 확장되어야 하며, 사용자는 코드의 수정 없이 확장된 서브클래스의 인스턴스를 사용할 수 있어야 할때

자바 구현 예시

- Eager Initialization(이른 초기화, Thread-safe)

```java
public class Singleton {
    // Eager Initialization
    private static Singleton uniqueInstance = new Singleton();

    private Singleton() {}

    public static Singleton getInstance() {
      return uniqueInstance; 
    } 
}
```

- Lazy Initialization with synchronized (동기화 블럭, Thread-safe)
    - synchronized 키워드로 인한 성능 하락

```java
public class Singleton {
    private static Singleton uniqueInstance;

    private Singleton() {}

    // Lazy Initailization
    public static synchronzied Singleton getInstance() {
      if(uniqueInstance == null) {
         uniqueInstance = new Singleton();
      }
      return uniqueInstance;
    }
}
```

- Lazy Initialization + Double-checked Locking
    - cf) volatile : 컴파일러가 특정 변수에 대해 옵티마이져가 캐싱을 적용하지 못하도록 하는 키워드이다.

    ```java
    public class ThreadSafe_Lazy_Initialization{
        private volatile static ThreadSafe_Lazy_Initialization instance;

        private ThreadSafe_Lazy_Initialization(){}

        public static ThreadSafe_Lazy_Initialization getInstance(){
        	if(instance == null) {
            	synchronized (ThreadSafe_Lazy_Initialization.class){
                    if(instance == null){
                        instance = new ThreadSafe_Lazy_Initialization();
                    }
                }
            }
            return instance;
        }
    }
    ```

- Lazy Initailization. Enum(열거 상수 클래스, Thread-safe)
    - enum 외에 다른 클래스 상속 불가
    - Enum 내의 다른 메서드가 있는 경우에 해당 메서드가 Thread-safe 한지는 개발자가 책임져야 한다

    ```java
    public enum Singleton {
        INSTANCE;

    }
    ```

- Lazy Initialization. LazyHolder(게으른 홀더, Thread-safe)
    - 가장 많이 사용하는 방법
    - 개발자가 직접 동기화 문제에 대한 코드를 작성하면서 회피하려고 하면 프로그램 구조가 그만큼 복잡해지고 비용 문제가 발생
    - 또한 코드 자체가 정확하지 못할 때도 많음 따라서 JVM의 클래스 초기화 과정에서 보장되는 원자적 특성을 이용해 싱글톤의 초기화 문제에 대한 책임을 JVM에게 떠넘기는 걸 활용함
    - 싱글턴 클래스에는 InnerInstanceClazz 클래스의 변수가 없기 때문에, static 멤버 클래스더라도, 클래스 로더가 초기화 과정을 진행할때 InnerInstanceClazz 메서드를 초기화 하지 않는다.
    - 따라서 getInstance() 메서드를 호출할때 초기화 됩니다. 즉, 동적바인딩(Dynamic Binding) (런타임시에 성격이 결정) 의 특징을 이용하여 Thread-safe 하면서 성능이 뛰어납니다.

    ```java
    public class Singleton {

        private Singleton() {}

        private static class InnerInstanceClazz() {
            //클래스 로딩 시점에서 생성
            private static final Singleton uniqueInstance = new Singleton();
        }

        public static Singleton getInstance() {
            return InnerInstanceClazz.instance;
        }
        
    }
    ```