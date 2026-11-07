
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_dict = {}
    for coin in coins:
        count = amount // coin
        amount = amount % coin
        if count > 0:
            coin_dict[coin] = count
    return coin_dict

print(find_coins_greedy(113))


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_coin = [0] * (amount + 1)
    
    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x:
                candidate = 1 + min_coins[x - coin]
                if candidate < min_coins[x]:
                    min_coins[x] = candidate
                    last_coin[x] = coin

    result = {}
    x = amount
    while x > 0:
        coin = last_coin[x]
        if coin not in result:
            result[coin] = 0
        result[coin] += 1
        x = x - coin
    return result

print(find_min_coins(113))







#*********************************************TASK2*****************************************************
import random
 
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
 
 
def f(x):
    return x ** 2
 
a = 0 
b = 2  
 

x = np.linspace(-0.5, 2.5, 400)
y = f(x)
 

fig, ax = plt.subplots()
 

ax.plot(x, y, 'r', linewidth=2)
 

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
 

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
 

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
 
 

def monte_carlo(n):
    y_max = f(b)
    inside = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, y_max)
        if y <= f(x):
            inside += 1
    return (b - a) * y_max * inside / n
 
 
# Check with quad
result, error = spi.quad(f, a, b)
print("Інтеграл (quad): ", result, error)
 

print("Інтеграл (аналітично): ", b ** 3 / 3 - a ** 3 / 3)
 

for n in [1000, 10000, 100000]:
    print("Інтеграл (Монте-Карло, n =", n, "): ", monte_carlo(n))