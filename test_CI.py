def addition(a,b):
    return a+b

def test_add():
    assert addition(2,4) == 6

def soustraction(a,b):
    return a-b

def test_sous():
    assert soustraction(4,3) == 1

def multiplication(a,b):
    return a*b

def test_mul():
    assert multiplication(7,5) == 35

def division(a,b):
    if b==0:
        return "Div par 0 impossible"
    return a/b

def test_div():
    assert division(10,2) == 5


def main():
    
    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    
    print(f"{a} + {b} = {addition(a,b)}")
    print(f"{a} - {b} = {soustraction(a,b)}")
    print(f"{a} * {b} = {multiplication(a,b)}")
    print(f"{a} / {b} = {division(a,b)}")

if __name__ == "__main__":
    main()