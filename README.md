# CodingTest

## Programmers

### - Level1

### - Level2

### - Level3

## Baekjoon

### BFS 문제

* 나이트의 이동 - [7562번](https://www.acmicpc.net/problem/7562)
* 미로탈출 - [16953번](https://www.acmicpc.net/problem/16953)
* 벽부수고이동하기2 - [14442번](https://www.acmicpc.net/problem/14442)
* 인구이동 - [16234번](https://www.acmicpc.net/problem/16234)
* 케빈베이컨의법칙 - [16953번](https://www.acmicpc.net/problem/16953)
* 토마토 - [7576번](https://www.acmicpc.net/problem/7576)

### DFS 문제

* 알파벳 - [1987번](https://www.acmicpc.net/problem/1987)
* 상근이의여행 - [9372번](https://www.acmicpc.net/problem/9372)
* 안전영역 - [2468번](https://www.acmicpc.net/problem/2468)
* 음료수 얼려먹기 - [16953번](https://www.acmicpc.net/problem/16953)

### 그리디 문제

* 회의실 배정 - [16953번](https://www.acmicpc.net/problem/16953)
* 설탕 배달 - [16953번](https://www.acmicpc.net/problem/16953)
* 동전 - [11047번](https://www.acmicpc.net/problem/11047)
* ATM - [11399번](https://www.acmicpc.net/problem/11399)
* A → B - [16953번](https://www.acmicpc.net/problem/16953)
* 파일합치기3 - [16953번](https://www.acmicpc.net/problem/16953)
* 카드정렬하기 - [16953번](https://www.acmicpc.net/problem/16953)
* 잃어버린괄호 - [16953번](https://www.acmicpc.net/problem/16953)
* 수묶기 - [16953번](https://www.acmicpc.net/problem/16953)
* 여행가자 - [1976번](https://www.acmicpc.net/problem/1976)
* 신입사원 - [16953번](https://www.acmicpc.net/problem/16953)
* 바이트코인 - [17521번](https://www.acmicpc.net/problem/17521)
* 문서검색 - [16953번](https://www.acmicpc.net/problem/16953)
* 로프 - [2217번](https://www.acmicpc.net/problem/2217)
* 뒤집기 - [16953번](https://www.acmicpc.net/problem/16953)
* 공항 - [10775번](https://www.acmicpc.net/problem/10775)

## 알고리즘

### Greedy

탐욕 알고리즘이라고들 많이 불린다.  
미래를 생각하지 않고 당장에 최선의 선택으로 문제를 해결하는 알고리즘이다.
보통 코딩 테스트에선 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있을 때 출제된다.

### Union-Find

그래프 알고리즘의 일종이다.
역할은 여러 개의 노드가 존재할 때 두 개의 노드를 선택해서, 현재 이 두 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘이다.

### Diijkstra (다익스트라)

최단경로를 찾는 알고리즘 중 하나이다.  
특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알려주는 알고리즘이다.

### Floyd Warshall (플로이드 와샬 알고리즘)

#### Lower bound

## 자료구조

### Heap

완전 이진 트리 자료구조의 일종
힙에서는 항상 루트 노드(Root Node)를 제거

* 시간 복잡도

    * 삽입: O(logN)
    * 삭제: O(logN)

* 최소 힙 (min heap)

    * 루트 노드가 가장 작은 값을 가짐
    * 따라서 값이 작은 데이터가 우선적으로 제거 됨

* 최대 힙 (max heap)

    * 루트 노드가 가장 큰 값을 가짐
    * 따라서 값이 큰 데이터가 우선적으로 제거 됨

* 최소 힙 구성 함수 - Min Heapify
    (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체함

* 힙에서 원소를 제거할 때는 가장 마지막 노드가 루트 노드의 위치에 오도록 한 후 하향식으로 Heapfiy 진행
