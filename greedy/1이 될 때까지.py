#<문제> 1이 될 때까지

#첫 번째 풀이
n, k = map(int, input().split())
result = 0

while n >= k:
    #N이 K로 나누어 떨어지면 K로 나누기
    if n % k == 0:
        #K로 나누기
        n //= k
        result += 1
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    else:
        n -= 1
        result += 1
        
result += (n - 1)

print(result)

#두 번째 풀이
n, k = map(int, input().split())
result = 0

while True:
    #나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    #N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    #K로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

#자바 풀이
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        //N, K를 공백을 기준으로 구분하여 입력 받기
        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;
        
        while(true) {
            //N이 K로 나누어 떨어지는 수가 될 때까지 빼기
            int target = (n / k) * k;
            result += (n - target)
            n = target
            //N이 K값 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
            if(n < k)
                break;
            //K로 나누기
            result += 1;
            n /= k;
        }
        //마지막으로 남은 수에 대하여 1씩 빼기
        result += (n - 1);
        System.out.println(result);
    }
}
    
