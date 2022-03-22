def rec(n, string):
    if n < 1:
        return
    strr = ""
    for i in range(0, len(string), 2):
        strr += str(string[i])
        strr += " "

    print(" " * n, strr)
    ls = [1, " "]
    for i in range(len(string) // 2):
        ls.append(int(string[len(ls) - 2]) + int(string[len(ls)]))
        ls.append(" ")

        


    ls += [1]
    return rec(n -1, ls)

rec(10, [1])
