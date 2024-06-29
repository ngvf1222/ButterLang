s=input()
def partion(n):
    for i in range(1,6):
        if n%i==0:
            return partion(f'{partion(n/i)}{i}*')
    return f'{partion(n-1)}1+'
for i in s:
    n=ord(i)

print('\n'.join([f"{"!"*ord(i)}이 또 되도않는 헛소리를 뱉고 있잖아!!" for i in s]))
