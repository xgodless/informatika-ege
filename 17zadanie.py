f = open('17.txt') # Шаблон
a = [] # Шаблон
for s in f: # Шаблон
    a.append(int(s)) # Шаблон
sum_pari = []   # Шаблон
for i in range(len(a)-1):# Шаблон
    if (a[i]%3==0 or a[i+1]%3==0):
        sum_pari.append(a[i]+a[i+1])

print(len(sum_pari), max(sum_pari))
