def partion_postive(var_,n):
    if n<6:
        return f"{var_} 닥쳐{'!'*n}"
    for i in range(50,1,-1):
        if n%i==0:
            return f'{partion_postive(var_,int(n/i))}\n{var_} 닥쳐 {var_} {"!"*i}'
    return f'{partion_postive(var_,n-1)}\n{var_} 후우...!'
def partion(var_,n):
    if n<0:
        return f"{partion_postive(var_,-n)}\n{var_} 닥쳐 {var_} ?"
    return partion_postive(var_,n)
if __name__=='__main__':
    inp=int(input())
    print(partion('result',inp))
    