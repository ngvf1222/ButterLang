import sys
def toNumber(expe:str,vars:dict):
    return (vars[expe.strip()] if expe.strip() in vars else 0)+expe.count('!')-expe.count('?')
def error_handeler(error_code,is_stop_when_error):
    print(error_code)
    sys.exit()
def is_vaild_var_name(name:str,is_stop_when_error):
    if name in '!?도록후우...' or ' ' in name:
        return False
    return True
def main(program:str):
    variables:dict[str]={}
    is_stop_when_error=True
    numebr_print_mode=False
    codes=program.split('\n')
    codes=map(lambda x: (x[:x.find('큭큭')] if '큭큭' in x else x),codes)#주석 제거
    codes:list[str]=filter(lambda x:x!='',codes)#빈행 제거
    #print(list(codes))
    for i in codes:
        #print(i)
        if i.endswith(' 푼수 요정이에용'):
            var_name=i[:-9]
            if is_vaild_var_name(var_name,is_stop_when_error):
                variables[var_name]=0
            else:
                error_handeler('non_vaild_var_name',is_stop_when_error)
        if i.endswith(' 못 참으면 뭐?'):
            var_name=i[:-9]
            if var_name in variables:
                variables[var_name]=int(input())
            else:
                error_handeler('not_exist_var',is_stop_when_error)
        if i=='따지고 보면 다 너 떄문이야!':
            numebr_print_mode=not numebr_print_mode
        if i.count(' 후우...')==1:
            k=i.find(' 후우...')
            var_name=i[:k]
            var_value=toNumber(i[k+6:],variables)
            if var_name not in variables:
                error_handeler('not_exist_var',is_stop_when_error)
                continue
            variables[var_name]+=var_value
        if i.count('이 또 되도않는 헛소리를 뱉고 있잖아')==1:
            k=i.find('이 또 되도않는 헛소리를 뱉고 있잖아')
            var_name=i[:k]
            std_number=toNumber(i[k+5:],variables)
            if var_name not in variables:
                error_handeler('not_exist_var',is_stop_when_error)
                continue
            if std_number==0:
                error_handeler('not_writeable_stdin',is_stop_when_error)
                continue
            if std_number>2:
                error_handeler('not_exist_std_number',is_stop_when_error)
                continue
            if std_number==1:
                stream=sys.stdout
            else:
                stream=sys.stderr
            if numebr_print_mode:
                stream.write(str(variables[var_name]))
            else:
                stream.write(chr(variables[var_name]))
if __name__=='__main__':
    hello_world="""a 푼수 요정이에용
b 푼수 요정이에용
result 푼수 요정이에용
a 못 참으면 뭐?
b 못 참으면 뭐?
따지고 보면 다 너 떄문이야!
result 후우... a
result 후우... b
result이 또 되도않는 헛소리를 뱉고 있잖아!"""
    main(hello_world)
    