# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTERER,PLUS,EOF='INTEGER','PLUS','EOF'

class Token(object):
    def __init__(self,type,value) :
        self.type=type
        self.value = value
    
    def __str__(self):
        return self.__str__()
    def __repr__(self):
        return self.__str__