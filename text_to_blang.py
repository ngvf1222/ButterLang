from num_to_blang import partion
s=input()
for i in s:
    n=ord(i)
    print(f"{partion('_',n)}\n_이 또 되도않는 헛소리를 뱉고 있잖아!!")

#print('\n'.join([f"{"!"*ord(i)}이 또 되도않는 헛소리를 뱉고 있잖아!!" for i in s]))
