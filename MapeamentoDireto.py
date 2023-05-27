
def inicializar_cache(tamanho_cache):
    cache = {"0":"-1"}
    for i in range(1,tamanho_cache):
        cache[str(i)] = "-1"
    
    return cache

def imprimir_cache(cache):
    print("Tamanho da Cache : ",len(cache))
    for i in range(0,len(cache)):
        print(i," : ",cache[str(i)])

def mapeamento_direto(tamanho_cache,posicoes):
    hits = 0
    misses = 0
    print("----------------------------")
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)

    for posicao in posicoes:
        print("----------------------------")
        print("Posição da Memória: ",posicao)

        posicao_cache = posicao%tamanho_cache
        print("Posição da Cache",posicao_cache)

        if cache[str(posicao_cache)] == str(posicao):
            print("Status: hit")
            hits += 1
        else:
            print("Status: miss")
            misses += 1
        cache[str(posicao_cache)] = str(posicao)
        imprimir_cache(cache)
        print("----------------------------")
        print(f"Número de Acessos: {hits+misses}")
        print(f"Hits: {hits}, misses: {misses}")
        print(f"Taxa de Hits: {round((hits/(hits+misses))*100,2)}%")
    


posicoes = [0,5,10,5,0,5]
mapeamento_direto(5, posicoes)

