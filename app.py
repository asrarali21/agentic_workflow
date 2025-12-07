
class langgraph:
    def __init__(self):
        self.name = "Asrar"
        self.marks = [20,30,40]

    def sum(self):
        sum = 0 
        for val in self.marks:
            sum +=val
        print(sum)


s1 = langgraph()
name = s1.sum()



