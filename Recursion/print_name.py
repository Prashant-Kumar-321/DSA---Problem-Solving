import sys 
sys.stdout = open('./Recursion/output.txt', 'w')
sys.stdin = open('./Recursion/input.txt', 'r')

def print_name(n: int, name: str)->None: 
    # Base Condition
    if n == 0: return

    print(name, end=" ")

    # Recursive call
    print_name(n-1, name)

def print_nat_number(n:int)->None: 
    # Base condition
    if n == 0: return

    # recursive call 
    print_nat_number(n-1)

    print(n, end=" ")

def sum_nat_number(n:int)->int: 
    # Base condition
    if n == 1: return 1

    # Recursive call 
    temp = sum_nat_number(n-1)

    return n + temp

def fact(n:int)->int: 
    # Base Condition
    if n == 0: return 1

    return n * fact(n-1)



if __name__ == "__main__": 
    # n = int(input())
    # name = input()

    # print_name(n, name)
    # print()

    n = int(input())
    # print_nat_number(n)
    # print()

    # print(sum_nat_number(n))
    # print()

    print(fact(n))
    print()