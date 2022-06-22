#<문제> 곱하기 혹은 더하기

data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

#자바 풀이

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        //첫 번째 문자를 숫자로 변경한 값을 대입
        long result = str.charAt(0) - '0';
        for(int i = 1; i < str.length(); i++) {
            //두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기가 수행
            int num = str.charAt(i) - '0';
            if(num <= 1 || result <=1) {
                result += num;
            } else {
                result *= num;
            }
        }
        System.out.println(result); 
    }
}