import sys
import time


def toNumber(expe: str, vars: dict):
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


def main(program: str):
    variables: dict[str] = {}
    consts: list[str] = {}
    is_stop_when_error = True
    numebr_print_mode = False
    codes = program.split("\n")
    codes = map(
        lambda x: (x[: x.find("큭큭")] if "큭큭" in x else x), codes
    )  # 주석 제거
    codes: list[str] = filter(lambda x: x != "", codes)  # 빈행 제거
    # print(list(codes))
    for i in codes:
        # print(i)
        i = i.strip()
        if i.startswith("마, 맛있는 거요? 뭔데요? 고구마? 빵? 고기? ") and i[-1] == "?":
            var_name = i[28:-1]
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            if var_name in consts:
                error_handeler("can't edit constant", is_stop_when_error)
                continue
            variables[var_name] = ord(input()[0])
        if i.endswith(" 푼수 요정이에용"):
            var_name = i[:-9]
            if (
                is_vaild_var_name(var_name, is_stop_when_error)
                and var_name not in variables
            ):
                variables[var_name] = 0
            else:
                error_handeler("non_vaild_var_name", is_stop_when_error)
        if i.endswith(" 못 참으면 뭐?"):
            var_name = i[:-9]
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            if var_name in consts:
                error_handeler("can't edit constant", is_stop_when_error)
                continue
            inp = input()
            if inp.isdigit():
                variables[var_name] = int(inp)
            else:
                error_handeler("not_intger", is_stop_when_error)
        if i.endswith(" 버터 바보야...?"):
            var_name = i[:-11]
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            if var_name in consts:
                error_handeler("can't edit constant", is_stop_when_error)
                continue
            inp = input("(y|n)")
            if inp in "YNyn":
                variables[var_name] = int(inp in "Yy")
            else:
                error_handeler("not_bool", is_stop_when_error)
        if i.startswith("이제 모두 반성의 시간을 가질테니 얌전히 있도록"):
            wait_time = i[26:]
            time.sleep(wait_time)

        if i.endswith("을 한 방에 다 정리해버리고") or i.endswith(
            "를 한 방에 다 정리해버리고"
        ):
            var_name = i[:-15]
            if var_name in variables and var_name not in consts:
                variables[var_name] = 0
            else:
                error_handeler("not_exist_var", is_stop_when_error)
        if i.endswith("은 친구 아니야!") or i.endswith("는 친구 아니야!"):
            var_name = i[:-9]
            if var_name in variables:
                del variables[var_name]
                if var_name in consts:
                    consts.remove(var_name)
            else:
                error_handeler("not_exist_var", is_stop_when_error)
        if i == "따지고 보면 다 너 떄문이야!":
            numebr_print_mode = not numebr_print_mode
        if i == "버터는 친구들을 돕는게 좋아! 그냥 하면 돼!":
            is_stop_when_error = False
        if (
            i
            == "버터는 친구들이 웃는게 좋아! 나도 웃는게 좋아! 같이 산책하는 것도 좋아! 밥먹는 것도 좋아, 헤헤"
        ):
            is_stop_when_error = True
        if (
            i.startswith("이제부터 ")
            and i.endswith(" 채로 영원히 사는 거야")
            and i.count("는 ") == 1
        ):
            # A변수명B값C 형태
            B = i.find("는 ")
            var_name = i[4:B]
            var_value = i[B + 2 : -13]
            if (
                is_vaild_var_name(var_name, is_stop_when_error)
                and var_name not in variables
            ):
                variables[var_name] = 0
                consts.append(var_name)
            else:
                error_handeler("non_vaild_var_name", is_stop_when_error)
        if i.count(" 후우...") == 1:
            k = i.find(" 후우...")
            var_name = i[:k]
            var_value = toNumber(i[k + 6 :], variables)
            if var_name not in variables and var_name not in consts:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            variables[var_name] += var_value
        if i.count(" 닥쳐") == 1:
            k = i.find(" 닥쳐")
            var_name = i[:k]
            var_value = toNumber(i[k + 3 :], variables)
            if var_name not in variables and var_name not in consts:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
            variables[var_name] = var_value
        if i.count("이 또 되도않는 헛소리를 뱉고 있잖아") == 1:
            k = i.find("이 또 되도않는 헛소리를 뱉고 있잖아")
            var_name = i[:k]
            std_number = toNumber(i[k + 5 :], variables)
            if var_name not in variables:
                error_handeler("not_exist_var", is_stop_when_error)
                continue
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
                stream.write(str(variables[var_name]))
            else:
                stream.write(chr(variables[var_name]))


if __name__ == "__main__":
    hello_world = """a 푼수 요정이에용
b 푼수 요정이에용
result 푼수 요정이에용
a 못 참으면 뭐?
b 못 참으면 뭐?
따지고 보면 다 너 떄문이야!
result 후우... a
result 후우... b
result이 또 되도않는 헛소리를 뱉고 있잖아!"""
    main(hello_world)
