from itertools import product 
alphabet = '12345'
count=0
for i in product(alphabet, repeat=5):    
    if i.count('1') == 3:
        count += 1
print(count)
