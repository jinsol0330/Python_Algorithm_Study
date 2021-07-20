'''
안녕

세준이는 성형수술을 한 후에 병원에 너무 오래 입원해 있었다. 
이제 세준이가 병원에 입원한 동안 자기를 생각해준 사람들에게 감사하다고 말할 차례이다.

세준이를 생각해준 사람은 총 N명이 있다. 사람의 번호는 1번부터 N번까지 있다. 
세준이가 i번 사람에게 인사를 하면 L[i]만큼의 체력을 잃고, J[i]만큼의 기쁨을 얻는다. 
세준이는 각각의 사람에게 최대 1번만 말할 수 있다.

세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것이다. 
세준이의 체력은 100이고, 기쁨은 0이다. 
만약 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것이 된다. 
세준이가 얻을 수 있는 최대 기쁨을 출력하는 프로그램을 작성하시오.
'''

n = int(input())
l_list = list(map(int,input().split()))
j_list = list(map(int,input().split()))
l_list = [0] + l_list
j_list = [0] + j_list 
dp_table = [[0 for _ in range(101)] for _ in range(n+1)] 
for i in range(1, n+1): 
    for j in range(1, 101): 
        if l_list[i] <= j: 
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-l_list[i]] + j_list[i]) 
        else: 
            dp_table[i][j] = dp_table[i-1][j] 
print(dp_table[n][99])

