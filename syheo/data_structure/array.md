# Array

# 0. Array

### array란?

보통 하나의 데이터를 위해 저장을 위한 변수를 선언하여 사용한다. 하지만 프로그래밍을 하다보면 여러개의 데이터를 위해 각각의 변수를 따로 선언하여 사용하는 것은 되게 비효율적임. 그래서 **여러 개의 데이터가 같은 성격을 가진 데이터일 경우, 하나의 이름을 갖는 변수로 여러 데이터를 그룹핑해서 관리**하는 것을 array(배열)를 통해서 할 수 있다. 

### array의 특징

- 같은 종류의 데이터를 하나의 이름으로 관리함.
    - 같은 종류란, 같은 데이터 타입(String, int, char, float, etc)을 말함.
- **크기가 정해져 있다**.
- 기능이 없다
- **인덱스**를 가지며 요소의 인덱스는 변경되지 않음.
    - 데이터를 삭제해도 해당 공간이 사라지지않음.
    - 배열 인덱스는 유일무이한 식별자임.
- 조회 시, 인덱스를 활용하여 빠르게 데이터에 접근할 수 있음.
    - 만약 순차탐색(Sequential Search)를 하더라도 배열은 **연속적인 공간**이므로 리스트보다 더욱 빠름.
- cache hit의 가능성이 커져서 성능에 큰 도움이 됨.
    - 운영체제의 cache locality(캐시 지역성)을 활용함.
        - cache locality: 운영체제에서는 물리적으로 근접한 위치의 데이터가 주로 활용되기 때문에 미리 캐시에 넣어둠으로써 CPU의 성능을 향상시킴.
        - cache hit : 캐시 지역성에서 캐시의 메모리에 CPU가 참조하고자 하는 메모리가 있다면 캐시 적중이라고 함.
            - 배열은 연속적인 메모리공간을 갖으므로 캐시 적중률이 높다.

### array의 단점

- 배열은 길이를 변경할 수 없다!
    - 만약 변경을 원한다면 해야하는 절차:
        1. 원하는 길이의 배열을 따로 할당
        2. 기존 배열에서의 데이터의 복사 
        3. 기존 배열의 삭제
- 데이터를 삭제해도 해당 공간이 사라지지 않음.
    - 쓸데없는 메모리 낭비