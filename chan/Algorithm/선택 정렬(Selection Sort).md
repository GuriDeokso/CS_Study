# 선택 정렬(Selection Sort)

1. 주어진 리스트 중에 최소값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체한다.
3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.

![Selection-Sort-Animation.gif](%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%A7%E1%86%AF(Selection%20Sort)%200981152ba02041f68f5dadbd12cdff73/Selection-Sort-Animation.gif)

```
void selectionSort(int *list,const int n)
{
    int i, j, indexMin, temp;

for (i = 0; i < n - 1; i++)
    {
        indexMin = i;
for (j = i + 1; j < n; j++)
        {
if (list[j] < list[indexMin])
            {
                indexMin = j;
            }
        }
        temp = list[indexMin];
        list[indexMin] = list[i];
        list[i] = temp;
    }
}
```

- 매번 가장 작은 값을 찾아서 맨앞에서 부터 차례로 자리를 정한다 (오름차순의 경우)
- 자료의 정렬 형태가 어떻게 되어있든 언제나 O(n^2)의 시간복잡도를 가진다
- Bubble sort와 유사한 듯 하지만 swap이 매번 비교시마다 일어나는 것이 아닌 마지막 변수까지 확인을 한 후에 한번씩만 이루어지기 때문에 더 효율적이다.