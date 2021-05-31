# SQL - JOIN

# 한 문장 정리‼️

둘 이상의 테이블을 결합하여 데이터를 검색하는 방법! 공유하고 있는 컬럼을 PK나 FK로 사용하는 릴레이션을 만듬.

---

# 0. Join 이란?

둘 이상의 테이블을 연결해서 데이터를 검색하는 방법임.

- 연결하려면 적어도 하나의 컬럼을 공유해야 함.
- 공유하고 있는 컬럼을 PK 또는 FK로 사용

# 1. SQL Join 종류

![Untitled](https://user-images.githubusercontent.com/42290273/116813629-91386f80-ab8f-11eb-95d8-c556a06052bf.png)

### 1. Inner Join : 내부 조인 → 교집합

### 2. Left/Right Join : → 부분집합

### 3. Outer Join : 외부 조인 → 합집합

- 오라클에서는 Outer Join이 있지만, MySQL에서는 없어서 Left+Right Join으로 대체

# 2. Join SQL문

### 1. Inner Join

![Untitled 1](https://user-images.githubusercontent.com/42290273/116813628-909fd900-ab8f-11eb-83d6-bde82fdfdd22.png)

- 교집합
- 공통적인 부분만 SELECT 됨.

```sql
select A.ID, A.ENAME, A.KNAME FROM A INNER JOIN B ON A.ID = B.ID;
```

### 2. Left Join

**1) <조인(JOIN) 기준> 왼쪽에 있는 데이터 전부 다 조회 (공통적인 부분 포함)**

![Untitled 2](https://user-images.githubusercontent.com/42290273/116813627-909fd900-ab8f-11eb-8cca-6a833daf8061.png)

- LEFT OUTER JOIN

```sql
select A.ID, A.ENAME, A.KNAME FROM A LEFT OUTER JOIN B ON A.ID = B.ID;
```

**2) <조인(JOIN) 기준> 왼쪽에 있는 데이터만 조회 (공통적인 부분 제외)**

![Untitled 3](https://user-images.githubusercontent.com/42290273/116813626-90074280-ab8f-11eb-9705-aaa79c6d81fa.png)

- LEFT JOIN 값에서 B의 속성값이 NULL인 값을 WHERE 절을 통해 조회

```sql
select A.ID, A.ENAME, A.KNAME FROM A LEFT OUTER JOIN B ON A.ID = B.ID 
WHERE B.ID is NULL
```

### 3. Right Join

**1) <조인(JOIN) 기준> 오른쪽에 있는 데이터 전부 다 조회 (공통적인 부분 포함)**

![Untitled 4](https://user-images.githubusercontent.com/42290273/116813624-8f6eac00-ab8f-11eb-8713-45d7bb07127e.png)

- RIGHT OUTER JOIN

```sql
select A.ID, A.ENAME, A.KNAME FROM A RIGHT OUTER JOIN B ON A.ID = B.ID;
```

**2) <조인(JOIN) 기준> 오른쪽에 있는 데이터만 조회 (공통적인 부분 제외)**

![Untitled 5](https://user-images.githubusercontent.com/42290273/116813623-8ed61580-ab8f-11eb-9c14-f3834870bac4.png)

- RIGHT JOIN 값에서 A의 속성 값이 NULL 인 것을 WHERE 절을 통해서 조회.

```sql
select A.ID, A.ENAME, A.KNAME FROM A RIGHT OUTER JOIN B ON A.ID = B.ID 
WHERE A.ID is NULL ; 
```

### 3. Outer Join

**1) 왼쪽,오른쪽에 있는 데이터 전부 다 조회 (공통적인 부분 포함)**

![Untitled 6](https://user-images.githubusercontent.com/42290273/116813620-8e3d7f00-ab8f-11eb-9994-dbad0f58c1c8.png)

- FULL OUTER JOIN

```sql
select A.ID, A.ENAME, A.KNAME FROM A FULL OUTER JOIN B ON A.ID = B.ID;

```

**1) 왼쪽,오른쪽에 있는 데이터만 조회 (공통적인 부분 제외)**

![Untitled 7](https://user-images.githubusercontent.com/42290273/116813618-8b428e80-ab8f-11eb-896c-901075a0c511.png)

- Where 절을 통해 A나 B의 속성값이 NULL인 값을 조회.

```sql
select A.ID, A.ENAME, A.KNAME FROM A FULL OUTER JOIN B ON A.ID = B.ID 
WHERE A.ID is NULL OR B.ID is NULL; 
```