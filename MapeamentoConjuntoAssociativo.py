def montar_cache(tamanho_cache, tamanho_bloco):
    cache = {}                 #cria um vetor vazio                   
    for i in range(tamanho_cache):
        cache[i] = {"tag": i,"conjunto":{}}  #linha da cache - conjunto
        for j in range(tamanho_bloco):
            conjunto = cache[i]["conjunto"]
            conjunto[j]= {"tag": j,"valor":"-1","acessos":0,"entrada":"-1","UltimoUso": "-1"}#acessos = LFU, #Entrada = FIFO, UltimoUso = LRU
    return cache

def imprimir_cache(cache):
    # print(cache)
    for i in range(len(cache)):
        print("\nConjunto",cache[i]["tag"])
        conjunto = cache[i]["conjunto"]
        for j in range(len(conjunto)):
            if conjunto[j]["valor"]!= "-1": #só é imprimido não estiver  vazio
                print("Bloco: ",conjunto[j]["tag"]," Valor: ",conjunto[j]["valor"])


def mapeamento_associativo_conjunto(tamanho_cache,tamanho_bloco,substituicao,entrada):
    bloc = [1,2,4,8,16]  #Tamanhos de bloco Validos
    subt = ["LRU","LFU","FIFO"] #técnicas de substituição válidas

    ##SE o tamanho dos blocos ou o método de substituição forem inválidos dá um exit no programa
    if tamanho_bloco not in bloc:
        print("Tamanho do Bloco Inválido")
        exit(0)
    elif substituicao not in subt:
        print("Método de Substituição Inválido")
        exit(0)
    misses = 0
    hits = 0
    acessos = 0

    cache = montar_cache(tamanho_cache, tamanho_bloco)
    print("+===============================================================+")
    print("Entrada: ",entrada, "Substituição: ",substituicao)
    print("+===============================================================+")
    print("Cache: ")
    imprimir_cache(cache)
    print("+===============================================================+")
    for posicao in entrada: #percorre todos os valores do vetor de entrada
        acessos +=1
        print("Entrada da Memória:  ",posicao)
        posicao_cache = posicao % tamanho_cache # define em qual posição da cache o valor tem que ser alocado
        print("Posição da Cache: ",posicao_cache)
        conjunto_cache = cache[posicao_cache]["conjunto"]
        
        hit = False

        #percorre o conjunto para checar se a posição da memória já está alocada na cache
        for i in range (len(conjunto_cache)):
            if conjunto_cache[i]["valor"] == posicao:
                print("Status: Hit")
                conjunto_cache[i]["acessos"]+=1
                conjunto_cache[i]["UltimoUso"] = acessos
                hit = True
                hits+=1
                break
        
        if not hit:
            print("Status: Miss")
            misses += 1
            espacos_vazios = 0
            #verifica se há espaços vazios no conjunto 
            for i in range (len(conjunto_cache)):
                #se houver
                if conjunto_cache[i]["valor"] == "-1":
                    conjunto_cache[i]["valor"] = posicao
                    conjunto_cache[i]["acessos"]+=1
                    conjunto_cache[i]["entrada"] = acessos
                    conjunto_cache[i]["UltimoUso"] = acessos
                    espacos_vazios += 1
                    break
            #se não houver
            if espacos_vazios == 0:
                #guarda o id que sairão da memória Cache em caso de substituição
                least_recently_used = 0
                first_in_first_out = 0
                least_frequently_used = 0

                #Valores para comparação
                LRU = int(conjunto_cache[0]["UltimoUso"])
                FIFO = conjunto_cache[0]["entrada"]
                LFU = conjunto_cache[0]["acessos"]

                for i in range (len(conjunto_cache)):
                    #descobre qual posição foi utilizada a mais tempo
                    if LRU > int(conjunto_cache[i]["UltimoUso"]):
                        LRU = conjunto_cache[i]["UltimoUso"]
                        least_recently_used = conjunto_cache[i]["tag"]

                    #Descobre qual posição foi alocada primeiro
                    if FIFO > conjunto_cache[i]["entrada"]:
                        FIFO = conjunto_cache[i]["entrada"]
                        first_in_first_out = conjunto_cache[i]["tag"] 
                    
                    #Descobre qual posição teve menos acessos, em caso de houverem valores igual substitui o primeiro que tiver a menor
                    #quantidade de acessos
                    if LFU > conjunto_cache[i]["acessos"]:
                        LFU = conjunto_cache[i]["acessos"]
                        least_frequently_used = conjunto_cache[i]["tag"]
                    

                if substituicao == "LRU":
                    #Substituição LRU
                    conjunto_cache[least_recently_used]["valor"] = posicao
                    conjunto_cache[least_recently_used]["acessos"]=1
                    conjunto_cache[least_recently_used]["entrada"] = acessos
                    conjunto_cache[least_recently_used]["UltimoUso"] = acessos
                
                elif substituicao == "LFU":
                    #Substituição LFU
                    conjunto_cache[least_frequently_used]["valor"] = posicao
                    conjunto_cache[least_frequently_used]["acessos"] = 1
                    conjunto_cache[least_frequently_used]["entrada"] = acessos
                    conjunto_cache[least_frequently_used]["UltimoUso"] = acessos

                else:
                    #Substituição FIFO
                    conjunto_cache[first_in_first_out]["valor"] = posicao
                    conjunto_cache[first_in_first_out]["acessos"]=1
                    conjunto_cache[first_in_first_out]["entrada"] = acessos
                    conjunto_cache[first_in_first_out]["UltimoUso"] = acessos
                
        imprimir_cache(cache)
        print("+---------------------------------------------------------------+")
        print("Acessos: ",acessos, "Hits: ",hits, "Misses: ",misses)
        print("Taxa de Hit", round((hits/acessos)*100,2), "%")
        print("+===============================================================+")
                    


# mapeamento_associativo_conjunto(1, 2, "LFU", [0,5,5,10,10,10,50,100,120])
mapeamento_associativo_conjunto(2, 4, "LRU", [0,1,2,3,4,5,6,7,0,8,4,10])
# mapeamento_associativo_conjunto(2, 2, "FIFO", [0,5,5,10,10,10,50,100,120])
