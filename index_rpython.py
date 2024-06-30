# -*- coding: utf-8 -*-
import sys
import time
import os


def NumberToBlang(num):
    if num>=0:
        return "!"*num
    else:
        return "?"*(-num)
def toNumber(expe, vars):
    # print(expe, vars)
    expe_strip=expe.strip(' \t')
    result=1
    for i in vars:
        expe_strip=expe_strip.replace(i,NumberToBlang(vars[i]))
    for i in expe_strip.split(' '):
        result*=i.count("!")- expe.count("?")
    return result


def error_handeler(error_code, is_stop_when_error):
    os.write(1,error_code)
    sys.exit()


def is_vaild_var_name(name, is_stop_when_error):
    for i in [u"?", u"!", u"도록", u"후우", u"는", u"채"]:
        if i in name:
            return False
    return True
def uni_isdigit(x):
    for i,j in enumerate(x):
        if j not in u'0123456789' and (i!=0 or j!=u'-'):
            return False
    return True

def main(
    program,
    variables={},
    consts={},
    is_stop_when_error=True,
    numebr_print_mode=False,
    string_input=None
):
    #print(program)
    #print(type(program))
    if_depth = 0
    def_depth = 0
    is_finding_def = False
    is_finding_else = False
    func_started_line = -1
    ret_adress = []
    is_tail_recursion_dict={}
    is_tail_recursion=False
    is_recursion=False
    i = -1
    codes = program.split("\n")
    # codes = map(
    #     lambda x: (x[: x.find(u"큭큭")] if u"큭큭" in x else x), codes
    # )  # 주석 제거
    codes_=codes
    codes=[]
    for j in codes_:
        v=(j[: abs(j.find(u"큭큭"))] if u"큭큭" in j else j)
        if v!=u'':
            codes.append(v)
    # codes = filter(lambda x: x != "", codes)  # 빈행 제거
    codes = list(codes)
    variables[u"트릭컬을 서비스 종료"] = len(codes)#exit함수
    while i < len(codes) - 1:
        i += 1
        code = codes[i]
        code = code.strip(' \t')
        #print(code)
        #print(variables)
        if is_finding_else:
            if code.endswith(u"도록"):
                if_depth += 1
            if code == u"이게 진짜!":
                if_depth -= 1
                if if_depth == 0:
                    is_finding_else = False
            continue
        if is_finding_def:
            if code == u"분위기 파악 개 못하네":
                def_depth += 1
            if code.endswith(u"나 차리고 앉아 있어요~") and code[:5] == u"이러니까 ":
                def_depth -= 1
                if def_depth == 0:
                    is_finding_def = False
                    variables[code[5:abs(len(code)-13)]] = func_started_line
                    is_tail_recursion_dict[func_started_line]=is_tail_recursion and is_recursion
                    is_tail_recursion=False
                    is_recursion=False
            if code.endswith(u"시킬 것이다!"):
                is_recursion=True
                if not codes[i+1].endswith(u"나 차리고 앉아 있어요~") or not codes[i+1][:5] == u"이러니까 ":#마지막 줄전에 호출->꼬리재귀x
                    is_tail_recursion=False
            continue

        if code.endswith(u"도록"):
            if_numebr = toNumber(code[:abs(len(code)-2)], variables)
            if if_numebr == 0:
                pass
            else:
                is_finding_else = True
                if_depth += 1
        if code == u"이게 진짜!":
            pass
        if code == u"분위기 파악 개 못하네":
            is_finding_def = True
            def_depth = 1
            is_tail_recursion=True
            func_started_line = i
        if (
            code.endswith(u"나 차리고 앉아 있어요~")
            and code[:5] == u"이러니까 "
            or code == u"나는 이만 간다"
        ):
            i = ret_adress.pop()
        if code.endswith(u"시킬 것이다!"):
            adress = toNumber(code[:abs(len(code)-7)], variables)
            if not is_tail_recursion_dict[adress]:
                ret_adress.append(i)
            i = adress
            continue
        if (
            code.startswith(u"마, 맛있는 거요? 뭔데요? 고구마? 빵? 고기? ")
            and code[abs(len(code)-1)] == u"?"
        ):
            var_name = code[28:abs(len(code)-1)]
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            if var_name in consts:
                error_handeler("can't edit constant", is_stop_when_error)
                continue
            if string_input:
                ch=string_input[0]
                string_input=string_input[1:]
            else:
                ch=(os.read(0,1)[0])
                if ord(ch)>127:
                    ch+=os.read(0,2)
                ch=ch.decode('utf-8')
                if ch!=u'\n':
                    os.read(0,1)
            if not ch or len(ch)>1 :
                continue
            variables[var_name]=\
                       ord(
                           ch[0]
                           )
            
        if (
            code.endswith(u" 푼수 요정이에용")
            or code.endswith(u" 푼수 수인이에용")
            or code.endswith(u" 푼수 마녀이에용")
            or code.endswith(u" 푼수 용족이에용")
            or code.endswith(u" 푼수 정령이에용")
            or code.endswith(u" 푼수 유령이에용")
            or code.endswith(u" 푼수 엘프이에용")
        ):
            var_name = code[:abs(len(code)-9)]
            if (
                is_vaild_var_name(var_name, is_stop_when_error)
                and var_name not in variables
            ):
                variables[var_name] = 0
            else:
                error_handeler("non_vaild_var_name", is_stop_when_error)
        if code.endswith(u" 못 참으면 뭐?"):
            var_name = code[:abs(len(code)-9)]
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            if var_name in consts:
                error_handeler("can't edit constant", is_stop_when_error)
                continue
            if string_input:
                inp=string_input.split(' ')[0]
                string_input=' '.join(string_input.split(' ')[1:])
            else:
                inp = os.read(0,4096)[0:].strip()
                inp=inp.decode('utf-8')
            if uni_isdigit(inp):
                variables[var_name] = int(inp)
            else:
                error_handeler("not_intger", is_stop_when_error)
        if code.endswith(u" 버터 바보야...?"):
            var_name = code[:abs(len(code)-11)]
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            if var_name in consts:
                error_handeler("can't edit constant", is_stop_when_error)
                continue
            if string_input:
                inp=string_input[0]
                string_input=string_input[1:]
            else:
                os.write(1,'(y|n)')
                inp = os.read(0,4096)[0]
            if inp in "YNyn":
                variables[var_name] = int(inp in "Yy")
            else:
                error_handeler("not_bool", is_stop_when_error)
        if code.startswith(u"이제 모두 반성의 시간을 가질테니 얌전히 있도록"):
            wait_time = toNumber(code[26:])
            time.sleep(wait_time)

        if code.endswith(u"을 한 방에 다 정리해버리고") or code.endswith(
            u"를 한 방에 다 정리해버리고"
        ):
            var_name = code[:abs(len(code)-15)]
            if var_name in variables and var_name not in consts:
                variables[var_name] = 0
            else:
                error_handeler("not_exist_var", is_stop_when_error)
        if code.endswith(u"은 친구 아니야!") or code.endswith(u"는 친구 아니야!"):
            var_name = code[:abs(len(code)-9)]
            if var_name in variables:
                del variables[var_name]
                if var_name in consts:
                    consts.remove(var_name)
            else:
                error_handeler("not_exist_var", is_stop_when_error)
        if code == u"따지고 보면 다 너 떄문이야!":
            numebr_print_mode = not numebr_print_mode
        if code == u"버터는 친구들을 돕는게 좋아! 그냥 하면 돼!":
            is_stop_when_error = False
        if (
            code
            == u"버터는 친구들이 웃는게 좋아! 나도 웃는게 좋아! 같이 산책하는 것도 좋아! 밥먹는 것도 좋아, 헤헤"
        ):
            is_stop_when_error = True

        if (
            code.startswith(u"이제부터 ")
            and code.endswith(u" 채로 영원히 사는 거야")
            and code.count(u"는 ") == 1
        ):
            # A변수명B값C 형태
            B = code.find(u"는 ")
            var_name = code[4:B]
            var_value = code[B + 2 : abs(len(code)-13)]
            if (
                is_vaild_var_name(var_name, is_stop_when_error)
                and var_name not in variables
            ):
                variables[var_name] = 0
                consts.append(var_name)
            else:
                error_handeler("non_vaild_var_name", is_stop_when_error)
        if code.count(u" 후우...") == 1:
            k = code.find(u" 후우...")
            var_name = code[:k]
            var_value = toNumber(code[k + 6 :], variables)
            if var_name not in variables and var_name not in consts:
                error_handeler(u"not_exist_var", is_stop_when_error)
                continue
            variables[var_name] += var_value
        if code.count(u" 닥쳐") == 1:
            k = code.find(u" 닥쳐")
            var_name = code[:k]
            var_value = toNumber(code[k + 3 :], variables)
            if var_name not in variables and var_name not in consts:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            variables[var_name] = var_value
        if code.count(u"이 또 되도않는 헛소리를 뱉고 있잖아") == 1:
            k = code.find(u"이 또 되도않는 헛소리를 뱉고 있잖아")
            value = toNumber(code[:k], variables)
            std_number = toNumber(code[k + 20 :], variables)
            if std_number == 0:
                error_handeler("not_writeable_stdin", is_stop_when_error)
                continue
            if std_number > 2 or std_number<0:
                error_handeler("not_exist_std_number", is_stop_when_error)
                continue
            if numebr_print_mode:
                os.write(std_number,str(value))
            else:
                os.write(std_number,
                         unichr(value).encode('utf8')
                         )


def run(argv):
    try:
        filename = argv[1]
        code=""
        fp=os.open(filename, os.O_RDONLY, 0777)
        while True:
            read = os.read(fp, 4096)
            if len(read) == 0:
                break
            code += read
        os.close(fp)
        code=code.decode('utf-8')
        if len(argv)==3:
            inp=""
            fp=os.open(argv[2], os.O_RDONLY, 0777)
            while True:
                read = os.read(fp, 4096)
                if len(read) == 0:
                    break
                inp += read
            os.close(fp)
            inp=inp.decode('utf-8')
            main(code,string_input=inp)
        else:
            main(code)
    except IndexError:
        error_handeler("file_missing",True)
        return 1
    return 0


def target(*args):
    return run, None


if __name__ == "__main__":
    run(sys.argv)
    #     hello_world = """에르핀 푼수 요정이에용
    # 에슈르도 푼수 요정이에용
    # 에슈르도 닥쳐!!!!!!!!!!
    # 따지고 보면 다 너 떄문이야!
    # 마, 맛있는 거요? 뭔데요? 고구마? 빵? 고기? 에르핀?
    # 에르핀이 또 되도않는 헛소리를 뱉고 있잖아!
    # 따지고 보면 다 너 떄문이야!
    # 에슈르도 이 또 되도않는 헛소리를 뱉고 있잖아!
    # 따지고 보면 다 너 떄문이야!
    # !!!!시킬 것이다!"""
#     hello_world = """분위기 파악 개 못하네
# 따지고 보면 다 너 떄문이야!
# !이 또 되도않는 헛소리를 뱉고 있잖아!!
# 따지고 보면 다 너 떄문이야!
# 분위기 파악 개 못하네
# 따지고 보면 다 너 떄문이야!
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# !이 또 되도않는 헛소리를 뱉고 있잖아!!
# 따지고 보면 다 너 떄문이야!
# 이러니까 모나티엄나 차리고 앉아 있어요~
# 모나티엄시킬 것이다!
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 이러니까 빵집나 차리고 앉아 있어요~
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 큭큭
# 빵집시킬 것이다!
# 따지고 보면 다 너 떄문이야!
# 빵집이 또 되도않는 헛소리를 뱉고 있잖아!!"""
#     main(hello_world)
