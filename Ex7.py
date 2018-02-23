# from cyberuniversity

print ('Now i will count my fruits')

mangoes = 6 + 12 + 99

apples = 9 / 3 + 1

peaches = 4 * 3 - 2

print ('mangoes', mangoes)
print('apples', apples)
print('peaches', peaches)

print('How many fruits have i eaten')
mangoes_left = int(input("How many mangoes are left? "))
apples_left = int(input("How many apples are left? "))
peaches_left = int(input("How many peaches are left? "))

# Now lets calculate
mangoes_eaten = mangoes - mangoes_left
apples_eaten = apples - apples_left
peaches_eaten = peaches - peaches_left

print ('You have eaten ', mangoes_eaten, 'mangoes',
       apples_eaten, 'apples', peaches_eaten, 'peaches')
