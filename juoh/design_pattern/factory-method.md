# 팩토리 메서드

한문장 정리

- 객체를 만드는 부분을 Sub class에 맡기는 패턴.

의도

- 객체를 생성하기 위해 인터페이스를 정의하지만, 어떤 클래스의 인스턴스를 생성할지에 대한 결정은 서브클래스가 내리도록 한다.

동기

- 어떤 클래스가 자신이 생성해야 하는 객체의 클래스를 예측할 수 없을 때
- 생성할 객체를 기술하는 책임을 자신의 서브클래스가 지정했으면 할 때
- 객체 생성의 책임을 몇 개의 보조 서브클래스 가운데 하나에게 위임하고, 어떤 서브클래스가 위임자인지에 대한 정보를 국소화시키고 싶을 때

구조

- Product: 팩토리 메서드가 생성하는 객체의 인터페이스 정의
- ConcreteProduct: Product 클래스에 정의된 인터페이스를 실제로 구현
- Creator
    - Product 타입의 객체를 반환하는 팩토리 메서드를 선언
    - 팩토리 메서드를 기본적으로 구현, ConcreteProduct 객체를 반환
    - Product 객체의 생성을 위해 팩티로 메서드를 호출
- ConcreteCreator: 팩토리 메서드를 재정의하여 ConcreteProduct의 인스턴스를 반환

![image_1](./factory-method/factory-method_1.png)

방법

- Creator는 자신의 서브클래스를 통해 실제 필요한 팩토리 메서드를 정의하여 적절한 ConcreteProduct의 인스턴스를 반환할 수 있게 한다.

구현

- 팩토리 메소드 페턴의 구현 방법은 크게 두 가지가 있다.
    1. Creator를 추상 클래스로 정의하고, 팩토리 메소드는 abstract로 선언하는 방법.
    2. Creator가 구체 클래스이고, 팩토리 메소드의 기본 구현을 제공하는 방법.
- 팩토리 메소드의 매개변수를 통해 다양한 종류의 Product를 생성하게 한다.
    - 팩토리 메소드에 잘못된 인자가 들어올 경우의 런타임 에러 처리에 대해 고민할 것.
    - Enum 등을 사용하는 것도 고려할 필요가 있다.
- 프로그래밍 언어별로 구현 방법에 차이가 있을 수 있다.

결과

- 팩토리 메서드 패턴은 응용프로그램에 국한된 클래스가 코드에 종속되지 않도록 해준다
- 응용프로그램은 Product 클래스에 정의된 인터페이스와만 동작하도록 코드가 만들어지기 때문에, 사용자가 정의한 어떤 ConcreteProduct 클래스가 와도 동작할 수 있다.

eample1) 방법 1

```java
// Product
abstract class Key {
    public abstract void use();
}
```

```java
// concreteProduct
class CardKey extends Key {
    @Override
    public void use() {
        System.out.println(owner + "의 카드를 사용합니다.");
    }
}

class IronKey extends Key {
    @Override
    public void use() {
        System.out.println(owner + "의 카드를 사용합니다.");
    }

}
```

```java
// Creator
abstract class Factory {
    public final Product create() {
        Product p = createProduct();
        return p;
    }
		// factory method
    protected abstract Product createProduct();
}
```

```java
// ConcreteCreator
class CardKeyFactory extends Factory {

    @Override
    protected Product createProduct() {
        return new CardKey();
    }
}

// ConcreteCreator
class IronKeyFactory extends Factory {

    @Override
    protected Product createProduct() {
        return new IronKey();
    }
}

Factory cardKeyFactory = new CardKeyFactory();
Factory ironKeyFactory = new IronKeyFactory();
Product key1 = cardKeyFactory.create();
Product key2 = ironKeyFactory.create();
Product key33 = ironKeyFactory.create();
```

example2) 팩토리 메소드를 매개변수화

```java
class CardKeyFactory extends Factory {

    @Override
    protected Product createProduct(String type) {
				switch( type ){
					case "A-Type": return new A-CardKey();
					case "B-Type": return new B-CardKey();
				}
    }
}
```