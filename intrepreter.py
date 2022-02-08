import global_
objects = global_.objects
class Interpret():
    
    def __init__(self) -> None:
        self.currentline = 0

        for line in global_.filecontent:
            self.currentline += 1 
            if line.startswith("#"):
                continue
            for item in objects:

                if item in line:    
                    if line[line.index(item) + len(item)] == "(": 
                        paren1 = line.index(item) + len(item)
                        paren2 = line.rfind(")",paren1)
                        args = list(line[paren1:paren2+1].replace("(","").replace(")",""))
                        while "," in args:
                            args.remove(",")
                        print(args)
                        