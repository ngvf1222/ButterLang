def NumberToBlang(num:int):
    if num>=0:
        return "!"*num
    else:
        return "?"*(-num)
def toNumber(expe: str, vars: dict):
    # print(expe, vars)
    expe_strip=expe.strip()
    result=1
    for i in vars:
        expe_strip=expe_strip.replace(i,NumberToBlang(vars[i]))
    for i in expe_strip.split(' '):
        result*=i.count("!")- expe.count("?")
    return result
v={"a":1,"b":2}
while True:
    inp=input()
    print(toNumber(inp,v))