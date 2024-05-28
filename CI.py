def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Div par 0 impossible"
    return a/b

def main():
    
    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    
    print(f"{a} + {b} = {addition(a,b)}")
    print(f"{a} - {b} = {soustraction(a,b)}")
    print(f"{a} * {b} = {multiplication(a,b)}")
    print(f"{a} / {b} = {division(a,b)}")

if __name__ == "__main__":
    main()