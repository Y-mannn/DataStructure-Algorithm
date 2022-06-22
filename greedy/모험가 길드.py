#<문제> 모험가 길드

n = int(input()
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인하며
    count +=1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화
        
print(result) #총 그룹의 수 출력

#자바 풀이

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        int n = sc.nextInt();
        
        for(int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }
        Collections.sort(list);
        
        int result = 0; #총 그룹의 수
        int count = 0; #현재 그룹에 포함된 모험가의 수
        for(int i = 0; i < n; i++) {
            count += 1; #현재 그룹에 해당 모험가를 포함시키기
            if(count >= list.get(i)) { #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
                result += 1; #총 그룹의 수 증가시키기
                count = 0 #현재 그룹에 포함된 모험가의 수 초기화
            }
        }
        System.out.println(result);
    }

}
    

    
    
