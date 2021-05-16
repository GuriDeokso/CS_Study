# LinkedList

# 1. LinkedList

### List란?

배열이 가지고 있는 인덱스라는 장점을 버리고 **빈틈없이 데이터를 적재**라는 장점을 취한 자료 구조.

리스트의 핵심은 엘리먼트간의 **순서**이다. 그래서 리스트는 다른 말로 시퀀스(Sequence)라고도 불리기도 함.

즉, 순서가 있는 데이터의 모임을 리스트라고 함.

### List의 특징

- 리스트에서 인덱스란 **몇 번째 데이터 인가?**를 지칭하기 위한 도구로 사용됨.
- 빈 엘리먼트는 허용하지 않음.
- 순차성을 보장하지 않음!
    - 공간 지역성(spacial Locality)를 보장하지 않으므로, cache hit 률이 낮음.
    - 임의의 노드에 바로 접근할 수 없음!
- 데이터의 삭제와 삽입이 용이함.
    - 연결을 끊고 다시 이어주면 됨.
- 길이를 동적으로 조절 가능
    - 다음 노드의 위치를 조절하기 위해서 추가 저장 공간이 필요함
- 기능이 있음!
    - 처음, 끝, 중간에 엘리먼트를 **삭제/추가**하는 기능
    - 리스트에 데이터가 있는지 체크하는 기능
    - 리스트에 모든 데이터에 접근할 수 있는 기능

### Double Linked List

- 보통 단순 연결리스트는 next 포인터를 통해 다음 노드를 가리킴
    - 반대 방향의 탐색이 불가.
- 이중 연결 리스트는 next, prev 두 개의 포인터를 갖고, 앞 뒤 노드를 연결함
    - 반대 방향의 탐색이 가능함.
        - 마지막 노드와 가까운 노드를 탐색하려고 할때, tail 노드부터 탐색을 할 수 있으므로 단순 연결리스트보다 효율적임.

### Java 에서의 리스트

- ArrayList
- LinkedList

java에서는 리스트 자료구조를 ArrayList, LinkedList 두 개로 제공한다. 두 데이터 타입 모두 삽입, 삭제에 대한 기능을 제공하지만, ArrayList는 삽입, 삭제가 느리고 조회가 빠른 반면, LinkedList 는 삽입, 삭제가 빠르고 조회가 느리다. 그래서 **지금 하고 있는 작업이 조회가 빈번하면 ArrayList, 삽입&삭제가 빈번하면 LinkedList를 사용하는 선택이 중요하다.**

- ArrayList에서 삽입, 삭제가 왜 느리나요!
    - 그 이유는 삽입, 삭제를 제공하지만 내부적으로 Array(배열) 형태이기 때문이다. 삽입을 하면 그만큼 뒤에 있는 엘리먼트를 뒤로 땡겨줘야하고, 삭제를 하면 그만큼 뒤에 있는 엘리먼트를 앞으로 땡겨줘야 하기 때문이다.
- ArrayList에서 조회는 그럼 왜 빠를까요?
    - 그 이유는 마찬가지로 내부적으로 배열 형태이기 때문에 메모리 참조 시 연속적인 공간에서 정확한 메모리 주소를 이용하여 참조하기 때문이다.

### why index starts with 0?

- 메모리 주소가 0부터 시작함.
- 인덱스는 시작 위치 (0)으로 부터 떨어진 거리를 의미.
    - 그래서 컴퓨터가 계산하기 더 쉬우라고
- 구간 컨벤션 중 하나인 **Half-open Interval** 를 사용하는 것이 프로그래밍에 용이함.
    - Half-open Interval : [a,b) , (a,b] 표현 방식 이중 [a,b)를 설명하면
        - 시작위치는 포함하고 마지막 위치를 제외함.
            - 그러면 a는 0, 그리고 배열의 크기인 N을 b로 표현할 수 있음.