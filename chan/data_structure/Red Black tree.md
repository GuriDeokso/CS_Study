# Red Black tree

![Untitled](Red%20Black%20tree%20b5464a3eb6ae401d878722108465e0bf/Untitled.png)

RB tree는 균형 이진 탐색 트리를 생성하는 알고리즘 중 한가지이다.

이진 탐색 트리는 모든 서브트리에 대해서 다음과 같은 특징을 가진다.

- Root 보다 작은 값 = Left child
- Root보다 큰 값 = Right child

만약 순차적으로 주어지는 데이터에 대해 트리를 만들경우

위 그림과 같이 이상적인 순서 ( 35, 11, 51 .. )로 데이터가 주어진 경우엔 균형 이진 트리를 생성할 수 있다.

 

### 하지만 데이터 값이 극단적인 경우로 주어진다면?

예를 들어 첫번째 입력값이 최소값인 1 또는 최댓값 56으로 주어진다면 

그 이후에 들어오는 데이터들은 전부 트리의 좌측 또는 우측으로만 child가 붙는 

편향 이진 트리 (Skewed binary tree) 구조가 될 가능성이 있다.

### 효율적인 균형 이진 탐색 트리 생성 알고리즘 : Red Black tree

### 생성조건

1. Root property : 루트노드의 색깔은 검정이다
2. External property : 모든 external node는 검정이다
3. Internal property : 빨강노드의 자식은 검정이다.
4. Depth property : 모든 리프노드에서 Black depth는 같다 (= 어떤 루트노드에서 그에 속한 리프노드에 도달하는 동안 만나는 블랙 노드의 개수는 일정하다)

RB tree를 형성할때 추가되는 노드는 모두 Red block으로 가정한다.

계속해서 노드를 추가한다면 빨강노드의 자식으로 새로운 빨강 노드가 들어오는 경우가 생긴다.

이때 생성조건중 Internal property를 위반하게 되는 경우가 필연적으로 생기는데 

이를 해결하기 위한 **두가지 해결책**을 제시한다.

![Untitled](Red%20Black%20tree%20b5464a3eb6ae401d878722108465e0bf/Untitled%201.png)

### Restructuring

현재 삽입된 노드(z) 기준으로 부모(v)의 형제 노드(w)가 **검정노드**일때

### Recoloring

현재 삽입된 노드(z) 기준으로 부모(v)의 형제 노드(w)가 **빨강노드**일때

## Restructuring :

현재 삽입된 노드(z) 기준으로 부모(v)의 형제 노드(w)가 **검정노드**일때

![Untitled](Red%20Black%20tree%20b5464a3eb6ae401d878722108465e0bf/Untitled%202.png)

1. 나(z), 부모(v), 부모의 부모(v') 이 세가지 노드를 가지고 새로 이진 탐색트리를 만든다.
2. 그 이후 Root노드는 검정노드로
3. 두 child node는 빨강노드로 정한다.

![Untitled](Red%20Black%20tree%20b5464a3eb6ae401d878722108465e0bf/Untitled%203.png)

Restructuring된 서브트리 완성후 기존 노드를 다시 추가한다.

![Untitled](Red%20Black%20tree%20b5464a3eb6ae401d878722108465e0bf/Untitled%204.png)

Restructuring 과정속에서 z, v, v' 세 노드를 가지고 

서브트리를 만드는 과정은 O(1)의 시간복잡도를 가진다.

단 이진 탐색 트리의 특성상 맨처음 z 노드가 삽입되는 위치를 탐색하기 위한 O(logn)의 시간 복잡도까지 고려하여 총 수행시간은 O(logn)이다.

## Recoloring

현재 삽입된 노드(z) 기준으로 부모(v)의 형제 노드(w)가 **빨강노드**일때

![Untitled](Red%20Black%20tree%20b5464a3eb6ae401d878722108465e0bf/Untitled%205.png)

1. 현재 삽입된 노드(z)의 부모와 형제(v, w)를 검정노드로 하고, 부모의 부모(v')을 빨강노드로 한다.
2. 부모의 부모노드(v')가 Root node인 경우
RB tree의 생성조건 Root property로 인해 검정노드로 한다.
3. 부모의 부모노드(v')가 Root node가 아닌경우 v'의 부모노드가 존재할경우
v''의 색에 따라 Recoloring이 한번에 끝나지 않을 수 있다.
- v''이 검정노드일 경우 : Recoloring 종료
- v''이 빨강노드일 경우 : v'', v' 모두 빨강노드로 Double red발생, 
이때 v' 의 uncle node(w')의 색에 따라 
다시한번 Restructuring or Recoloring 진행