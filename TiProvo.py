'''Simple prover of expressions in propositional logic'''

import time

def implies(A, B):
    if(A and (B == False)):
        return(False)
    else:
        return(True)

def xor(A, B):
    if(A and B) or (not A and not B):
        return(False)
    else:
        return(True)

def HELP():
    print("- and: logical conjunction")
    print("- or: logical disjunction (inclusive)")
    print("- not: logical negation")
    print("- implies(A, B): material conditional")
    print("- xor(A, B): logical disjunction (exclusive)\n")

def main():
    print("*************")
    print("***TiProvo***")
    print("*************\n")

    time.sleep(2)

    flag = True

    while(flag):
        expr = eval(input("Evaluate expression [or type HELP()]: "))
        if((expr == "Stop") or (expr == "stop") or (expr == "STOP")):
            flag = False
        else:
            print(expr)
            print()

main()
