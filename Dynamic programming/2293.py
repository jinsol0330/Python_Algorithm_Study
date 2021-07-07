'''
동전 1

n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
'''

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp_table = [0] * (k+1)

'''
인덱스 0은 동전을 1개만 쓸 때를 고려하기 위함
예) x원짜리 동전 하나만으로 x원을 만드는 방법은 1개
'''
dp_table[0] = 1

for c in coins:
    for i in range(c,k+1):
        dp_table[i] += dp_table[i-c]

print(dp_table[k])    


'''
예) 
1,3원으로 6원을 만드는 방법은, 3원을 사용하는 방법과 3원을 사용하지 않는 방법 두가지로 나누어 생각할 수 있음
따라서 k원을 만들기 위한 점화식은 
f(k) += f(k-(리스트 안 coin))
'''