money = 1000
count = 0 # 잔돈의 개수

coins = [500, 100, 50, 10, 5, 1] # 동전 종류

pay_money = int(input()) # 지불할 돈
remain_money = money - pay_money # 거스름 돈

for coin in coins:
    if remain_money >= coin:
        count += remain_money // coin # 동전의 개수
        remain_money %= coin # 남은 돈
print(count)