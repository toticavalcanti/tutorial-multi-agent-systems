import random

class RoboAspirador:
    def __init__(self):
        self.posicao = [0, 0]
    
    def detectar_sujeira(self):
        # Simula a detecção de sujeira
        return random.choice([True, False])
    
    def mover(self):
        # Move aleatoriamente
        direcao = random.choice(['cima', 'baixo', 'esquerda', 'direita'])
        if direcao == 'cima':
            self.posicao[1] += 1
        elif direcao == 'baixo':
            self.posicao[1] -= 1
        elif direcao == 'esquerda':
            self.posicao[0] -= 1
        elif direcao == 'direita':
            self.posicao[0] += 1
    
    def limpar(self):
        print(f"Limpando na posição {self.posicao}")
    
    def agir(self):
        if self.detectar_sujeira():
            self.limpar()
        else:
            self.mover()

# Teste do Robô Aspirador
aspirador = RoboAspirador()

for _ in range(20):  # Executa 10 ações do robô
    aspirador.agir()
    print(f"Posição atual do robô: {aspirador.posicao}")