import sys


def parse_input(text):

    result = list()
    tmp_str = ''

    ii = 0
    for inc in text:
        
        ii = ii + 1

        if inc.isspace():
            continue

        # if inc == number
        if inc.isdigit():
            tmp_str = tmp_str + inc
            if ii == len(text):
                result.append(tmp_str)       
        else:
            if tmp_str  != '':
                result.append(tmp_str)
                tmp_str = ''

        # if inc == + , -, *, or /
        if (inc == '+') | (inc == '-') | (inc == '*') | (inc == '/'):
            result.append(inc)
            continue

    return result


if __name__ == '__main__':

    argv = sys.argv
    
    if len(argv) != 2:
        print("invalid number of arguments.\n")
        sys.exit(1)

    user_input = argv[1]

    user_input = parse_input(user_input)

    print(".intel_syntax noprefix")
    print(".global main")
    print("main:")
    print("  mov rax, %d" %  int(user_input[0]))

    ii = 1
    while True:

        if ii == len(user_input):
            break

        if user_input[ii] == '+':
            ii = ii + 1
            print("  add rax, %d" % int(user_input[ii]))
            ii = ii + 1
            continue
        
        if user_input[ii] == '-':
            ii = ii + 1
            print("  sub rax, %d" % int(user_input[ii]))
            ii = ii + 1
            continue

        print("unexpected character: '%c'" % user_input[ii])
        sys.exit(1)

    print("  ret")

