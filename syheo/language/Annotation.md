# Annotation

# 한 문장 정리‼️

### Annotation

메타 데이터 역할을 하는 기능. 

---

# 0. Annotation이란?

JEE5(Java Platform, Enterprise Edition 5)부터 새롭게 추가된 요소.

- 가장 큰 역할은 **메타 데이터**의 역할을 한다는 것!
    - 메타-테이터(Meta-Data) : 데이터를 위한 데이터를 의미하며, 풀어 이야기하면 한 데이터에 대한 설명을 의미하는 데이터. (자신의 정보를 담고 있는 데이터)
- AOP(Aspect Oriented Programing; 관심 지향 프로그래밍)을 편리하게 구성할 수 있음.

# 1. Annotation 의 특징

- 컴파일러에게 코드 문법 에러를 체크하도록 정보를 제공
- 소프트웨어 개발 툴이 빌드나 배치 시 코드를 자동으로 생성할 수 있도록 정보를 제공
- 어노테이션을 만들 때 용도를 분명하게 해야 함.
    - 소스상에서만 유지해야 할지
    - 컴파일된 클래스에도 유지해야 할지
    - 런타임 시에도 유지해야 할지

# 2. Built-in Annotation

Java에서 기본적으로 제공하는 어노테이션의 종류는 다음과 같음.

1. **@Override**
    - 선언한 메서드가 오버라이드 되었다는 것을 나타냄.
    - 만약 상위(부모) 클래스(또는 인터페이스)에서 해당 메서드를 찾을 수 없다면 컴파일 에러를 발생 시킴.
2. **@Deprecated**
    - 해당 메서드가 더 이상 사용되지 않음을 표시함.
    - 만약 사용할 경우 컴파일 경고를 발생시킴.
3. **@SuppressWarnings**
    - 선언한 곳의 컴파일 경고를 무시함.
4. **@SafeVarargs**
    - Java7 부터 지원하며, 제너릭 같은 가변인자의 매개변수를 사용할 때의 경고를 무시함.
5. **@FunctionalInterface**
    - Java8 부터 지원하며, 함수형 인터페이스를 지정하는 어노테이션
    - 만약 메서드가 존재하지 않거나, 1개 이상의 메서드(default 메서드 제외)가 존재할 경우 컴파일 오류를 발생 시킴.

# 3. Meta Annotations

Meta Annotation을 활용해서 Custom Annotation을 만들 수 있음.

1. **@Retention**
    - 자바 컴파일러가 어노테이션을 다루는 방법을 기술하며, **특정 시점까지 영향**을 미치는지를 **결정**함.
        - **RetentionPolicy.SOURCE** : 컴파일 전까지만 유효. (컴파일 이후에는 사라짐)
            - Compile 이후로 삭제되는 형태
        - **RetentionPolicy.CLASS** : 컴파일러가 **클래스를 참조할 때까지** 유효.
            - 바이트 코드 파일까지 어노테이션 정보를 유지
            - 하지만 리플렉션을 이용해서 어노테이션 정보를 얻을 수는 없음.
        - **RetentionPolicy.RUNTIME** : 컴파일 이후에도 **JVM에 의해 계속 참조**가 가능. (리플렉션 사용)
            - 바이트 코드 파일까지 어노테이션 정보를 유지하면서 리플렉션을 이용해서 런타임시에 어노테이션 정보를 얻을 수 있음.
2. **@Target**
    - 어노테이션이 적용할 위치를 선택.
        - **ElementType.PACKAGE** : 패키지 선언
        - **ElementType.TYPE** : 타입 선언
        - **ElementType.ANNOTATION_TYPE** : 어노테이션 타입 선언
        - **ElementType.CONSTRUCTOR** : 생성자 선언
        - **ElementType.FIELD** : 멤버 변수 선언
        - **ElementType.LOCAL_VARIABLE** : 지역 변수 선언
        - **ElementType.METHOD** : 메서드 선언
        - **ElementType.PARAMETER** : 전달인자 선언
        - **ElementType.TYPE_PARAMETER** : 전달인자 타입 선언
        - **ElementType.TYPE_USE** : 타입 선언
3. **@Documented**
    - 해당 어노테이션을 Javadoc에 포함시킴.
4. **@Inherited**
    - 어노테이션의 상속을 가능하게 함.
    - 자식클래스가 어노테이션을 상속 받을 수 있음.
5. **@Repeatable**
    - Java8 부터 지원하며, 연속적으로 어노테이션을 선언할 수 있게 해줌.

# 4. Annotation 구조

```java
@Inherited // 상속
@Documented // 문서에 정보가 표현
@Retention(RetentionPolicy.RUNTIME) // 컴파일 이후에도 JVM에 의해서 참조가 가능합니다
@Retention(RetentionPolicy.CLASS)   // Compiler가 클래스를 참조할 때까지 유효합니다
@Retention(RetentionPolicy.SOURCE)  // 컴파일 이후 사라집니다
@Target({
		ElementType.PACKAGE, // 패키지 선언시
		ElementType.TYPE, // 타입 선언시
		ElementType.CONSTRUCTOR, // 생성자 선언시
		ElementType.FIELD, // 멤버 변수 선언시
		ElementType.METHOD, // 메소드 선언시
		ElementType.ANNOTATION_TYPE, // 어노테이션 타입 선언시
		ElementType.LOCAL_VARIABLE, // 지역 변수 선언시
		ElementType.PARAMETER, // 매개 변수 선언시
		ElementType.TYPE_PARAMETER, // 매개 변수 타입 선언시
		ElementType.TYPE_USE // 타입 사용시
})
public @interface CustomAnnotation{
	/* enum 타입을 선언할 수 있습니다. */
	public enum Quality {
		BAD, GOOD, VERYGOOD
	}

	/* String은 기본 자료형은 아니지만 사용 가능합니다. */
	String value() default "CustomAnnotation : Default String Value";

	/* 배열 형태로도 사용할 수 있습니다. */
	int[] values();

	/* enum 형태를 사용하는 방법입니다. */
	Quality quality() default Quality.GOOD;
}
```

---

### 참고 사이트

[Java에서 어노테이션(Annotation)이란?](https://elfinlas.github.io/2017/12/14/java-annotation/)

[Java Annotation이란?](https://nesoy.github.io/articles/2018-04/Java-Annotation)