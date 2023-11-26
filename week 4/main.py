import random
rand_list=[]
n=5
for i in range(n):
  rand_list.append(random.randint(1, 20))
print(*rand_list)
total = 0
for ele in range(0, len(rand_list)):
  total = total + rand_list[ele]
print(total)
