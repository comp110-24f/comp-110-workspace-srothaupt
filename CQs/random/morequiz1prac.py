def num_instances(inp_str: str, search_str: str) -> int:
    idx: int = 0
    check: str = ""
    count: int = 0
    lgth = len(search_str)
    while idx < len(inp_str):
        while idx < lgth:
            check = check + str(inp_str[idx])
            idx += 1
        if search_str == check:
            count = count + 1
        print(idx)
        # idx = idx + lgth
        check: str = ""
    return count


print(num_instances(inp_str="HelloHelloHello", search_str="Hello"))
