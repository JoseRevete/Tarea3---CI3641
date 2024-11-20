import sys
from io import StringIO
from ManejadorTipoDatos import main

def simulate_input(inputs):
    sys.stdin = StringIO(inputs)
    main()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    inputs = """\
ATOMICO int 4 4
ATOMICO char 1 1
ATOMICO float 4 4
ATOMICO double 8 8
STRUCT MiStruct int char float
UNION MiUnion int double
DESCRIBIR int
DESCRIBIR char
DESCRIBIR MiStruct
DESCRIBIR MiUnion
ATOMICO int 4 4
STRUCT OtraStruct int unknownType
SALIR
"""
    simulate_input(inputs)