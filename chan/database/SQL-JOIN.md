# SQL-JOIN

둘 이상의 테이블을 연결해서 데이터를 검색하는 방법이다.

연결시에는 테이블들이 적어도 하나의 컬럼을 공유하고 있어야 한다.

이 공유 컬럼값을 PK또는 FK로 사용한다.

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled.png)

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%201.png)

두 가지 테이블 A, B로 예시를 들겠다.

1. INNER JOIN : 교집합, 공통적인 부분만 SELECT 된다.

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%202.png)

1. LEFT JOIN : 조인 기준 왼쪽에 있는것 전부 SELECT 된다. (공통부분 + LEFT 전부)

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%203.png)

2-1. A-B, 조인기준 왼쪽에 있는것만 SELECT 된다.

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%204.png)

1. RIGHT JOIN : 조인 기준 오른쪽에 있는것 전부 SELECT된다. (공통부분 + RIGHT전부)

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%205.png)

3.1 A-B, 조인기준 오른쪽에 있는것만 SELECT 된다.

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%206.png)

1. OUTER JOIN: A테이블, B테이블이 가지고 있는 것 둘다 SELECT

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%207.png)

4.1 오른쪽, 왼쪽에 있는것만 SELECT
FULL OUTER가 가지고 있는 것 중 공통부분을 제외한 값

![Untitled](SQL-JOIN%203d51f25dda5c4f15bf37ac9c526329a9/Untitled%208.png)