#그래프 탐색 알고리즘: DFS/BFS

#탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다.
#대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있습니다.
#DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야 합니다.

#스택 자료구조

#먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조 입니다.
#입구와 출구가 동일한 형태로 스택을 시각화할 수 있습니다.

#스택 동작 예시
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
#[5, 2, 3, 1]

stack = []

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력

#[1, 3, 2, 5]
#[5, 2, 3, 1]

#자바 구현
import java.util.*;

public class Main {
    
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        
        //삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();
        
        //스택의 최상단 원소부터 출력
        while(!s.empty()) {
            System.out.print(s.peak() + " ");
            s.pop();
        }
    }
}

#큐 자료구조

#먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조입니다.
#큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

#큐 동작 예시
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
#[3, 7, 1, 4]

from collections import deque

#큐(Queue) 구현을 위해 deque 라이브러리 사용
#list 자료형으로 큐를 구현할 수도 있지만 시간복잡도가 더 높아 비효율적
queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #시간 복잡도는 O(1) 상수시간
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력

#[3, 7, 1, 4]
#[4, 1, 7, 3]

#자바 구현

import java.util.*;

public class Main {
    
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        
        //삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();
        q.offer(1);
        q.offer(4);
        q.poll();
        
        //먼저 들어온 원소부터 추출
        while(!q.empty()) {
            System.out.print(q.poll() + " ");
        }
    }
}