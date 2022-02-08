import json
import CustomExceptions

class Input:
    def __init__(self,*values) -> None:
        self.info = json.load(open("objects.json"))["Input"]
        if len(values) > len(self.info["args"].items()):
                            CustomExceptions.ArgError(f"Input expected {self.info['argsamount']} argument(s), got {values.__len__()}",self.currentline) #TODO:Finsh later