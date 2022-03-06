import argparse 
import square_equation_lib

def validate_param(a, b, c):
    try:
        float(a)
        float(b)
        float(c)
        return True
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description = 'A solve square equation script')
    parser.add_argument("--a")
    parser.add_argument("--b")
    parser.add_argument("--c")

    args = parser.parse_args()
    if(validate_param(args.a, args.b, args.c) == False):
        print("Input is not a number")
        return 0
        
    a = float(args.a)
    b = float(args.b)
    c = float(args.c)

    if(square_equation_lib.square_equation.discriminant(a, b, c) < 0):
        print("Square equation has no roots")
        return 0
    else:
        print(square_equation_lib.square_equation.square_print(a, b, c, square_equation_lib.square_equation.roots))

main()
