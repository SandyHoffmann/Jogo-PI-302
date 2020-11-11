
class Grupo_Parametros():
    def __init__(self, clerigo, ladrao, realeza):
        self.clerigo=0
        self.ladrao=0
        self.realeza=0
    def set_ladrao(self, ladrao):
        self.ladrao+=ladrao
    def set_clerigo(self, clerigo):
        self.clerigo+=clerigo
    def set_realeza(self, realeza):
        self.realeza+=realeza
    def get_ladrao(self):
        return (self.ladrao)
    def get_clerigo(self):
        return (self.clerigo)
    def get_realeza(self):
        return (self.realeza)