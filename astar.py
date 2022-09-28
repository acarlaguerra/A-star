def heuristic_funct(n):
    #função que define o tempo das distâncias em linha reta já multplicadas por 2
    distances = {
        
    }

#matriz das distâncias reais e nós adjacentes
matrix_dist = {
    'E1': [('E2-azul', 20)],
    'E2': [('E3-azul', 17)]
}

## ENCAIXAR TEMPO DE TROCAR DE LINHA

def get_neighbors(v):
    #função para identificar os nós adjacentes e as distâncias reais entre eles
    if v in matrix_dist:
        return matrix_dist[v]
    else:
        return None


def AStar(start_node, stop_node):
    open_set = set(start_node)          #inicializando o conjunto de busca
    closed_set = set()
    g_sum = {}                          #computa a distância com o nó inicial
    parents = {}                        #dicionário que contém nós adjacentes
    g_sum[start_node] = 0               #distancia do nó inicial pra ele mesmo é 0
    parents[start_node] = start_node    #o nó inicial é o que vai ser pai de todos os outros

    while len(open_set) > 0: #enquanto o conjunto não estiver vazio
        n = None
        #pretende-se achar o nó com o menor tempo
        for v in open_set:
            if n == None or g_sum[v] + heuristic_funct(v) < g_sum[n] + heuristic_funct(n):
                n = v
            
        #se n é o nó de destino, ignoramos
        if n == stop_node or matrix_dist[n] == None:
            pass
        else:
            #já que ele não é nó destino, vamos checar seus adjacentes
            for (m, distance) in get_neighbors(n):
                #se m ainda não está no conjunto de busca, adicionamos
                if m not in open_set and m not in closed_set:
                    open_set.add(m)                 #adicioando
                    parents[m] = n                  #setando n como mãe desse nó
                    g_sum[m] = g_sum[n] + distance  #calculando a função G para o determinado nó

                #para cada nó já incluído no conjunto, compara com a distância inicial para conferir que é o menor
                else:
                    if g_sum[m] > g_sum[n] + distance:
                        g_sum[m] = g_sum[n] + distance
                        parents[m] = n 
                        #atualiza o nó caso ele tenha um tempo menor e seja o último da lista
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

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
            return path
        
        #como todos os adjacentes de n foram analisados, retira ele do conjunto
        open_set.remove(n)
        closed_set.add(n)

    print('Caminho não encontrado, recalculando a rota!')
    return None

