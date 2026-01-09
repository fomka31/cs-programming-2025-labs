def time_convert(data: str):
    table = {
        "s" : 1,
        "m" : 60,
        "h" : 3600,
        "d" : 3600*24
    }

    source, res = data.split()
    num, char = int(''.join(source)[0:-1]), ''.join(source)[-1]
    result = num * table[char]/ table[res]
    return str(result.__round__(3)) + res


us_input = "12s h"
print(time_convert(us_input))