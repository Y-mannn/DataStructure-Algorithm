#<문제> 큰 수의 법칙

#첫 번째 풀이

#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0] #가장 큰 수
second = data[1] #두 번째로 큰 수

result = 0
count = 0

while m != 0: #m이 0이라면 반복문 탈출
    if count != k: #가장 큰 수를 K번 더하기
        result += first
        count += 1 
        m -= 1 #더할 때마다 1씩 빼기
    else: #두 번째로 큰 수를 한 번 더하기
        count = 0
        result += second
        m -= 1 #더할 때마다 1씩 빼기
        
print(result) #최종 답안 출력

#두 번째 풀이

#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0] #가장 큰 수
second = data[1] #두 번째로 큰 수

result = 0
count = 0

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first #가장 큰 수 더하기
result += (m - count) * second #두 번째로 큰 수 더하기

print(result) #최종 답안 출력

