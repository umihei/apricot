import sys


def parse_input(text):

    result = list()
    tmp_str = ''

    ii = 0
    #for inc in text:
    while True: 
        print(ii)
        #ii = ii + 1
        if ii == len(text):
            result.append(tmp_str)
            break


        if text[ii].isspace():


            ii = ii + 1
            continue

        # if inc == number
        if text[ii].isdigit():
            tmp_str = tmp_str + text[ii]
            ii = ii + 1
            continue
                       
        elif tmp_str != '':
            result.append(tmp_str)
            tmp_str = ''

        # if inc == + , -, *, or /
        inc = text[ii]
        if (inc == '+') | (inc == '-') | (inc == '*') | (inc == '/'):
            result.append(inc)
            ii = ii + 1
            continue

        error_at(text, ii, "can not tokenize")

    return result


def error_at(user_input, loc, msg):
    print(user_input)
    print(" " * loc + "^ " + msg)
    sys.exit(1)


if __name__ == '__main__':

    argv = sys.argv
    
    if len(argv) != 2:
        print("invalid number of arguments.\n")
        sys.exit(1)

    user_input = argv[1]

    tokens = parse_input(user_input)

    print(".intel_syntax noprefix")
    print(".global main")
    print("main:")
    print("  mov rax, %d" %  int(tokens[0]))

    ii = 1
    loc = len(tokens[0])
    while True:

        if ii == len(tokens):
            break

        if tokens[ii] == '+':
            ii = ii + 1
            loc = loc + len(tokens[ii]) + 1
            if not tokens[ii].isdigit():
                error_at(user_input, loc, "Not a number.")
            print("  add rax, %d" % int(tokens[ii]))
            ii = ii + 1
            continue
        
        if tokens[ii] == '-':
            ii = ii + 1
            loc = loc + len(tokens[ii]) + 1
            if not tokens[ii].isdigit():
                error_at(user_input, loc, "Not a number.")
            print("  sub rax, %d" % int(tokens[ii]))
            ii = ii + 1
            continue

        print("unexpected character: '%c'" % tokens[ii])
        sys.exit(1)

    print("  ret")

