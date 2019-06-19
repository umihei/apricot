import sys
from collections import defaultdict

TK_NUM = 256
TK_EOF = 257

class Token(object):
    __slots__ = ['ty', 'val', 'input'] 


Tokens = list()


def tokenizer(text):

    #text = text + '\n'
    result = list()
    tmp_str = ''

    ii = 0
    while ii < len(text): 

    #for cha in text:

        print('ii :' + str(ii))       
        print('text[ii]: '+ text[ii])
                        
        if text[ii].isspace():
            continue

        # if inc == number
        if text[ii].isdigit():
            tmp_str = tmp_str + text[ii]
            ii = ii + 1
            if ii < len(text):
                print(ii)
                while text[ii].isdigit():
                    tmp_str = tmp_str + text[ii]
                    ii = ii + 1
                    if ii >= len(text):
                        break
            tmp = Token()
            tmp.ty = TK_NUM
            tmp.input = tmp_str
            tmp.val = int(tmp_str)
            Tokens.append(tmp)
            tmp_str = ''
            continue
        #else:
        #    if tmp_str != '':
        #        tmp = Token()
        #        tmp.ty = TK_NUM
        #        tmp.input = tmp_str
        #        tmp.val = int(tmp_str)
        #        Tokens.append(tmp)
        #        ii = ii + 1
        #        result.append(tmp_str)
        #        tmp_str = ''

        # if inc == + , -, *, or /
        cha = text[ii]
        if (cha == '+') | (cha == '-') | (cha == '*') | (cha == '/'):
            tmp = Token()
            tmp.ty = cha
            tmp.input = cha
            Tokens.append(tmp)
            result.append(cha)
            ii = ii + 1
            continue

        error_at(text, ii, "can not tokenize")

    tmp = Token()
    tmp.ty = TK_EOF
    tmp.input = '\n'
    Tokens.append(tmp)

    print(len(Tokens))
    for token_ in Tokens:
        print(token_.ty)
        print('input: ' + token_.input)

    return result


def expr():
    node = mul()

    while True:
        if consume('+'):
            node = new_node('+', node, mul())
        elif consume('-'):
            node = new_node('-', node, mul())
        else:
            return node


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

    tokens = tokenizer(user_input)

    print(".intel_syntax noprefix")
    print(".global main")
    print("main:")

    if Tokens[0].ty != TK_NUM:
        error_at(Tokens[0].input, "Not a number.")
    print("  mov rax, %d" %  Tokens[0].val)

    ii = 1
    loc = len(Tokens[0].input)

    while Tokens[ii].ty != TK_EOF:

        if Tokens[ii].ty == '+':
            ii = ii + 1
            loc = loc + len(Tokens[ii].input)
            if Tokens[ii].ty != TK_NUM:
                error_at(user_input, loc, "Not a number.")
            print("  add rax, %d" % Tokens[ii].val)
            ii = ii + 1
            continue
        
        if Tokens[ii].ty == '-':
            ii = ii + 1
            loc = loc + len(Tokens[ii].input)
            if Tokens[ii].ty != TK_NUM:
                error_at(user_input, loc, "Not a number.")
            print("  sub rax, %d" % Tokens[ii].val)
            ii = ii + 1
            continue

        print("unexpected character: '%c'" % Tokens[ii].input)
        sys.exit(1)

    print("  ret")

