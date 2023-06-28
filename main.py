from stack_class import Stack


def balance(sub):
    s = Stack()
    # print(s.fullstack())
    for i in sub:
        if i in ("(", "{", "["):
            s.push(i)
        elif i in (")", "}", "]") and s.size() != 0:
            if (
                (i == ")" and s.peek() == "(")
                or (i == "]" and s.peek() == "[")
                or (i == "}" and s.peek() == "{")
            ):
                s.pop()
            else:
                status = "Несбалансированно"
                return status
        else:
            status = "Несбалансированно"
            return status
    if s.isEmpty():
        status = "Cбалансированно"
    else:
        status = "Несбалансированно"
    return status


if __name__ == "__main__":
    sub = r"{{[()]}}"
    # sub = input()
    print(balance(sub))
