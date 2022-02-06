class ArgError:
    def __init__(self,message,line) -> None:
        print(f"ArgError at line {line}:")
        print("    "+message)
        exit(0)