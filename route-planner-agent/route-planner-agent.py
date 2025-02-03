import heapq
import matplotlib.pyplot as plt

class AgentePlanejadorRotas:
    def __init__(self, mapa, inicio, destino):
        self.mapa = mapa
        self.posicao = inicio
        self.destino = destino
        self.caminho = []
        self.historico = [inicio]  # Para armazenar as posições percorridas

    def planejar_rota(self):
        self.caminho = self.busca_a_estrela(self.posicao, self.destino)

    def busca_a_estrela(self, inicio, fim):
        def heuristica(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        fila = []
        heapq.heappush(fila, (0, inicio))
        custos = {inicio: 0}
        caminhos = {inicio: None}

        while fila:
            _, atual = heapq.heappop(fila)

            if atual == fim:
                caminho = []
                while atual:
                    caminho.append(atual)
                    atual = caminhos[atual]
                return caminho[::-1]

            x, y = atual
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                vizinho = (x + dx, y + dy)
                if 0 <= vizinho[0] < len(self.mapa) and 0 <= vizinho[1] < len(self.mapa[0]) and self.mapa[vizinho[0]][vizinho[1]] != 1:
                    novo_custo = custos[atual] + 1
                    if vizinho not in custos or novo_custo < custos[vizinho]:
                        custos[vizinho] = novo_custo
                        prioridade = novo_custo + heuristica(vizinho, fim)
                        heapq.heappush(fila, (prioridade, vizinho))
                        caminhos[vizinho] = atual
        return []

    def mover(self):
        if self.caminho:
            nova_posicao = self.caminho.pop(0)
            print(f"Movendo para {nova_posicao}")
            self.posicao = nova_posicao
            self.historico.append(nova_posicao)  # Adiciona ao histórico
        else:
            print("Destino alcançado")

    def agir(self):
        if not self.caminho:
            self.planejar_rota()
        self.mover()

# Configuração do mapa
mapa = [
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

inicio = (0, 0)
destino = (4, 4)

# Função para desenhar o mapa
def desenhar_mapa(mapa, agente, historico):
    plt.imshow(mapa, cmap="Greys", origin="upper")
    plt.scatter(inicio[1], inicio[0], c="green", s=200, label="Início")  # Início
    plt.scatter(destino[1], destino[0], c="red", s=200, label="Destino")  # Destino

    # Exibe o histórico
    if historico:
        y, x = zip(*historico)
        plt.plot(x, y, c="blue", linewidth=2, label="Caminho")

    plt.scatter(agente.posicao[1], agente.posicao[0], c="yellow", s=200, label="Agente")  # Posição atual do agente
    plt.legend()
    plt.pause(0.5)
    plt.clf()

# Executa o agente com visualização
# Executa o agente com visualização
agente = AgentePlanejadorRotas(mapa, inicio, destino)

plt.figure(figsize=(8, 8))
plt.ion()  # Ativa o modo interativo

# Loop para agir enquanto não alcança o destino
while agente.posicao != destino:
    desenhar_mapa(mapa, agente, agente.historico)
    agente.agir()

# Mostra o mapa final sem limpar ou fechar
plt.ioff()  # Desativa o modo interativo
desenhar_mapa(mapa, agente, agente.historico)  # Desenha o estado final
plt.show()  # Mantém o gráfico aberto até o usuário fechá-lo