import sys
import time


def toNumber(expe: str, vars: dict):
    # print(expe, vars)
    return (
        (vars[expe.strip()] if expe.strip() in vars else 0)
        + expe.count("!")
        - expe.count("?")
    )


def error_handeler(error_code, is_stop_when_error):
    print(error_code)
    sys.exit()


def is_vaild_var_name(name: str, is_stop_when_error):
    if any(map(lambda x: x in name, ["?", "!", "도록", "후우", "는", "채"])):
        return False
    return True


def main(
    program: str,
    variables={},
    consts={},
    is_stop_when_error=True,
    numebr_print_mode=False,
    string_input=None
):
    if_level = 0
    def_level = 0
    is_finding_def = False
    is_finding_else = False
    func_started_line = -1
    ret_adress = []
    tail={}
    is_tail=False
    is_r=False
    i = -1
    codes = program.split("\n")
    codes = map(
        lambda x: (x[: x.find("큭큭")] if "큭큭" in x else x), codes
    )  # 주석 제거
    codes: list[str] = filter(lambda x: x != "", codes)  # 빈행 제거
    codes = list(codes)
    variables["트릭컬을 서비스 종료"] = len(codes)
    while i < len(codes) - 1:
        i += 1
        code = codes[i]
        code = code.strip()
        if is_finding_else:
            if code.endswith("도록"):
                if_level += 1
            if code == "이게 진짜!":
                if_level -= 1
                if if_level == 0:
                    is_finding_else = False
            continue
        if is_finding_def:
            if code == "분위기 파악 개 못하네":
                def_level += 1
            if code.endswith("나 차리고 앉아 있어요~") and code[:5] == "이러니까 ":
                def_level -= 1
                if def_level == 0:
                    is_finding_def = False
                    variables[code[5:-13]] = func_started_line
                    tail[toNumber(code[5:-13],variables)]=is_tail and is_r
                    is_tail=False
                    is_r=False
            if code.endswith("시킬 것이다!"):
                is_r=True
                if not codes[i+1].endswith("나 차리고 앉아 있어요~") or not codes[i+1][:5] == "이러니까 ":
                    is_tail=False
            continue

        if code.endswith("도록"):
            if_numebr = toNumber(code[:-2], variables)
            if if_numebr == 0:
                pass
            else:
                is_finding_else = True
                if_level += 1
        if code == "이게 진짜!":
            pass
        if code == "분위기 파악 개 못하네":
            is_finding_def = True
            def_level = 1
            is_tail=True
            func_started_line = i
        if (
            code.endswith("나 차리고 앉아 있어요~")
            and code[:5] == "이러니까 "
            or code == "나는 이만 간다"
        ):
            i = ret_adress.pop()
        if code.endswith("시킬 것이다!"):
            adress = toNumber(code[:-7], variables)
            if not tail[adress]:
                ret_adress.append(i)
            i = adress
            continue
        if (
            code.startswith("마, 맛있는 거요? 뭔데요? 고구마? 빵? 고기? ")
            and code[-1] == "?"
        ):
            var_name = code[28:-1]
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
                for j in sys.stdin:
                    ch=j[0]
                    break
            variables[var_name] = ord(ch)
            
        if (
            code.endswith(" 푼수 요정이에용")
            or code.endswith(" 푼수 수인이에용")
            or code.endswith(" 푼수 마녀이에용")
            or code.endswith(" 푼수 용족이에용")
            or code.endswith(" 푼수 정령이에용")
            or code.endswith(" 푼수 유령이에용")
            or code.endswith(" 푼수 엘프이에용")
        ):
            var_name = code[:-9]
            if (
                is_vaild_var_name(var_name, is_stop_when_error)
                and var_name not in variables
            ):
                variables[var_name] = 0
            else:
                error_handeler("non_vaild_var_name", is_stop_when_error)
        if code.endswith(" 못 참으면 뭐?"):
            var_name = code[:-9]
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
                inp = input()
            if inp.isdigit() or inp[0] == "-" and inp[1:].isdigit():
                variables[var_name] = int(inp)
            else:
                error_handeler("not_intger", is_stop_when_error)
        if code.endswith(" 버터 바보야...?"):
            var_name = code[:-11]
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
                inp = input("(y|n)")
            if inp in "YNyn":
                variables[var_name] = int(inp in "Yy")
            else:
                error_handeler("not_bool", is_stop_when_error)
        if code.startswith("이제 모두 반성의 시간을 가질테니 얌전히 있도록"):
            wait_time = code[26:]
            time.sleep(wait_time)

        if code.endswith("을 한 방에 다 정리해버리고") or code.endswith(
            "를 한 방에 다 정리해버리고"
        ):
            var_name = code[:-15]
            if var_name in variables and var_name not in consts:
                variables[var_name] = 0
            else:
                error_handeler("not_exist_var", is_stop_when_error)
        if code.endswith("은 친구 아니야!") or code.endswith("는 친구 아니야!"):
            var_name = code[:-9]
            if var_name in variables:
                del variables[var_name]
                if var_name in consts:
                    consts.remove(var_name)
            else:
                error_handeler("not_exist_var", is_stop_when_error)
        if code == "따지고 보면 다 너 떄문이야!":
            numebr_print_mode = not numebr_print_mode
        if code == "버터는 친구들을 돕는게 좋아! 그냥 하면 돼!":
            is_stop_when_error = False
        if (
            code
            == "버터는 친구들이 웃는게 좋아! 나도 웃는게 좋아! 같이 산책하는 것도 좋아! 밥먹는 것도 좋아, 헤헤"
        ):
            is_stop_when_error = True

        if (
            code.startswith("이제부터 ")
            and code.endswith(" 채로 영원히 사는 거야")
            and code.count("는 ") == 1
        ):
            # A변수명B값C 형태
            B = code.find("는 ")
            var_name = code[4:B]
            var_value = code[B + 2 : -13]
            if (
                is_vaild_var_name(var_name, is_stop_when_error)
                and var_name not in variables
            ):
                variables[var_name] = 0
                consts.append(var_name)
            else:
                error_handeler("non_vaild_var_name", is_stop_when_error)
        if code.count(" 후우...") == 1:
            k = code.find(" 후우...")
            var_name = code[:k]
            var_value = toNumber(code[k + 6 :], variables)
            if var_name not in variables and var_name not in consts:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            variables[var_name] += var_value
        if code.count(" 닥쳐") == 1:
            k = code.find(" 닥쳐")
            var_name = code[:k]
            var_value = toNumber(code[k + 3 :], variables)
            if var_name not in variables and var_name not in consts:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            variables[var_name] = var_value
        if code.count("이 또 되도않는 헛소리를 뱉고 있잖아") == 1:
            k = code.find("이 또 되도않는 헛소리를 뱉고 있잖아")
            value = toNumber(code[:k], variables)
            std_number = toNumber(code[k + 20 :], variables)
            if std_number == 0:
                error_handeler("not_writeable_stdin", is_stop_when_error)
                continue
            if std_number > 2:
                error_handeler("not_exist_std_number", is_stop_when_error)
                continue
            if std_number == 1:
                stream = sys.stdout
            else:
                stream = sys.stderr
            if numebr_print_mode:
                stream.write(str(value))
            else:
                stream.write(chr(value))


def run(argv):
    try:
        filename = argv[1]
        f = open(filename, "r", encoding="utf8")
        code = f.read()
        f.close()
        if len(argv)==3:
            f=open(argv[2],'r',encoding='utf8')
            inp=f.read()
            f.close()
            main(code,string_input=inp)
        else:
            main(code)
    except IndexError:
        error_handeler("file_missing")
        return 1
    except FileNotFoundError:
        error_handeler("file_not_found")
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
