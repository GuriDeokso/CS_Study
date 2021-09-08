# 거품 정렬(Bubble Sort)

```jsx
def bubble_sort(arr):
	for i in range(len(arr)-1):       
		for j in range(len(arr)-i-1): 
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
```

리스트의 처음부터 마지막 바로 전 원소까지 

바로 다음 원소와 크기를 비교하여 크기가 크다면 뒤로 보낸다.

첫번째 for문을 한번 돌 때마다 1번째로 큰수, 2번째로 큰수, 3번째로 큰수... 가 배열의 맨 마지막부터 차례대로 정렬이 된다.