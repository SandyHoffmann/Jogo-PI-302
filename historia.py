class Historia():
    def __init__(self,ponto_de_parada,sucesso,falha):
        self.ponto_de_parada=ponto_de_parada
        self.sucesso=sucesso
        self.falha=falha

    def historia(self,ponto_de_parada):
        if ponto_de_parada==1:
            texcompleto = "Ola bartender, me vê uma Sea Water."
            return texcompleto
        if ponto_de_parada==2:
            texcompleto = "Ola bartender, me vê uma Heavy Drink."
            return texcompleto
        if ponto_de_parada==3:
            texcompleto = "Ola bartender, me vê uma Sugar Rush."
            return texcompleto





