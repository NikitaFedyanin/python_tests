WHITESPACE_STR = ' \t\n\r'


def parse_array(s, _w=WHITESPACE_STR, _sep=","):
    array = None
    stack = []
    accumulator = ""
    closed_flag = False
    sep_flag = False
    whitespace_flag = False
    started_flag = False
    for ch in s:
        if ch in _w:
            whitespace_flag = True
            continue
        if ch == "[":
            if started_flag and not stack:
                raise ValueError("Wrong string.")
            if closed_flag or accumulator:
                raise ValueError
            in_array = []
            if stack:
                stack[-1](in_array)
            else:
                array = in_array
                started_flag = True
            stack.append(in_array.append)
        elif not started_flag:
            raise ValueError("Wrong string.")
        elif ch == "]":

            if not stack:
                raise ValueError("Wrong string.")
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            stack.pop()
            closed_flag = True
            sep_flag = False
            whitespace_flag = False
        elif ch in _sep:
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            elif closed_flag:
                pass
            else:
                raise ValueError("Wrong string.")
            sep_flag = True
            closed_flag = False
            whitespace_flag = False
        else:
            if whitespace_flag and accumulator or closed_flag:
                raise ValueError
            accumulator += ch
        whitespace_flag = False
    if not array is None:
        return array
    else:
        raise ValueError("Wrong string")


try:
    parse_array("[[2]")
    assert False, "Excess opened bracket"
except ValueError:
    pass

try:
    parse_array("[3 4]")
    assert False, "Check for spurious spaces within a number"
except ValueError:
    pass

try:
    parse_array("[10, 11,, 12]")
    assert False, "Check for double separators without a space in between"
except ValueError:
    pass

try:
    parse_array("[[]3]")
    assert False, "Check for missing separators after []"
except ValueError:
    pass

try:
    parse_array("[2[]]")
    assert False, " Check for missing separators before []"
except ValueError:
    pass

try:
    parse_array("[3],")
    assert False, "Excess separator"
except ValueError:
    pass

try:
    parse_array("[1,2]3")
    assert False, "Excess number"
except ValueError:
    pass

try:
    parse_array("[1], [2,3]")
    assert False, "Here should be only one array."
except ValueError:
    pass