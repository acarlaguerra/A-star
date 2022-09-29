#inicializando a matriz de distâncias diretas em linha reta
distances = [
    
        [0,    10,   18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8], # Estação E1
        [10,   0,    8.5,  14.8, 26.6, 29.1, 26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8], # Estação E2
        [18.5, 8.5,  0,    6.3,  18.2, 20.6, 17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6], # Estação E3
        [24.8, 14.8, 6.3,  0,    12,   14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], # Estação E4
        [36.4, 26.6, 18.2, 12,   0,    3,    2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], # Estação E5
        [38.8, 29.1, 20.6, 14.4, 3,    0,    3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], # Estação E6
        [35.8, 26.1, 17.6, 11.5, 2.4,  3.3,  0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6], # Estação E7
        [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6], # Estação E8
        [17.6, 10,   9.4,  12.6, 23.3, 25.7, 23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6], # Estação E9
        [9.1,  3.5,  10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2], # Estação E10
        [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5], # Estação E11
        [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6], # Estação E12
        [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1],  # Estação E13
        [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0]     # Estação E14
    ]

#multiplicando a matriz de distâncias por 2, para resgatar o tempo entre as estações
def multiplication(matrix):
    return [[element * 2 for element in line] for line in matrix]

    
#matriz das distâncias reais e nós adjacentes já multiplicadas por 2 pelo mesmo motivo
matrix_dist = {
    1 : [(2, 20, 'azul')], #'2' refere-se a E2
    2 : [(3, 17, 'azul'), (1, 20, 'azul'), (9, 20, 'amarela'), (10, 7, 'amarela')], #'3' refere-se a E3; '1' refere-se a E1; '9' refere-se a E9;
    3 : [(2, 17, 'azul'), (4, 12.6, 'azul'), (9, 18.8, 'vermelha'), (13, 37.4, 'vermelha')],
    4 : [(3, 12.6, 'azul'), (5, 26, 'azul'), (8, 30.6, 'verde'), (13, 25.6, 'verde')],
    5 : [(4, 26, 'azul'), (6, 6, 'azul'), (7, 4.8, 'amarela'), (8, 60, 'amarela')],
    6 : [(5, 6, 'azul')],
    7 : [(5, 4.8, 'amarela')],
    8 : [(5, 60, 'amarela'), (4, 30.6, 'verde'), (9, 19.2, 'amarela'), (12, 12.8, 'verde')],
    9 : [(8, 19.2, 'amarela'), (2, 20, 'amarela'), (3, 18.8, 'vermelha'), (11, 24.4, 'vermelha')],
    10: [(2, 7, 'amarela')],
    11: [(9, 24.4, 'vermelha')],
    12: [(8, 12.8, 'verde')],
    13: [(3, 37.4, 'vermelha'), (4, 25.6, 'verde'), (14, 10.2, 'verde')],
    14: [(13, 10.2, 'verde')]
}

#função para identificar os nós adjacentes e as distâncias reais entre eles
def get_neighbors(v):
    if v in matrix_dist:
        return matrix_dist[v]
    else:
        return None


def AStar(start_node, stop_node):
    search_list = []                        #construindo a fronteira, a qual será nosso conjunto de busca
    search_list.append(start_node)          #inicializando o conjunto de busca
    final_list = []
    g_sum = {}                              #computa a distância com o nó inicial
    parents = {}                            #dicionário que contém nós adjacentes
    g_sum[start_node] = 0                   #distancia do nó inicial pra ele mesmo é 0
    parents[start_node] = start_node        #o nó inicial é o que vai ser mãe de todos os outros

    heuristic_funct = multiplication(distances)
    while len(search_list) > 0: #enquanto o conjunto não estiver vazio
        n = None

        #pretende-se achar o nó com o menor tempo
        for v in search_list:
            if n == None or g_sum[v] + heuristic_funct[v[0] - 1][stop_node[0] - 1] < g_sum[n] + heuristic_funct[n[0] - 1][stop_node[0] - 1]:
                n = v
                print(f'Nó atual: {n}')

        #se n é o nó de destino, ignoramos
        if n == stop_node or matrix_dist[n[0]] == None:
            pass
        else:
            #já que ele não é nó destino, vamos checar seus adjacentes
            for (m, distance, line) in get_neighbors(n[0]): #(1, 20, azul)
                vec = (m, line) #(numero da linha, cor)
                #se m ainda não está no conjunto de busca, adicionamos
                if vec not in search_list and vec not in final_list:
                    search_list.append(vec)                #adicionando
                    print(f'Fronteira: {search_list}')
                    parents[vec] = n                  #setando n como mãe desse nó
                    g_sum[vec] = g_sum[n] + distance  #calculando a função G para o determinado nó
                    if n[1] != vec[1]: #verifica se ele muda de linha
                        g_sum[vec] += 4

                #para cada nó já incluído no conjunto, compara com a distância inicial para conferir qual é o menor
                else:
                    if g_sum[vec] > g_sum[n] + distance:
                        g_sum[vec] = g_sum[n] + distance
                        parents[vec] = n 
                        #atualiza o nó caso ele tenha um tempo menor e seja o último da lista(estava definido como nó destino)
                        if m in final_list:
                            final_list.remove(vec)
                            search_list.append(vec)

        if n == None:
            print('Tá fazendo o quê aqui ainda? Caminho não encontrado!') 
            return None      

        #se o nó atual é o de destino, vamos construir o caminho
        if n == stop_node:
            path = []
            #varremos o dicionário até que chegue no nó mãe
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node) #adicionamos o nó mãe por último
            path.reverse() #revertemos o caminho pois fizemos de trás pra frente que nem curupira
            print('OK Google: o caminho a se seguir é {}'.format(path))
            print(f'Tempo final: {g_sum[v] + heuristic_funct[v[0] - 1][stop_node[0] - 1]} minutos')
            return path
        
        #como todos os adjacentes de n foram analisados, retiramos ele do conjunto
        search_list.remove(n)
        final_list.append(n)

    print('Caminho não encontrado, recalculando a rota!')
    return None

def main():
    AStar((6, "azul"), (13, "verde"))

main()
