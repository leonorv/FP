#92509 Leonor Veloso

#--CELULA--#
'''construtor'''
def cria_celula(digito):
    ''' assinatura: {1, 0, 1} -> celula
    ::  Uma celula consiste numa lista com 1 digito (0,1,-1 - respetivamente representando os estados inativo, ativo, incerto)'''
    if isinstance(digito, int) and digito in range(-1,2):
        return [digito]
    else:
        raise ValueError('cria_celula: argumento invalido.')
    
'''seletor'''
def obter_valor(celula):
    ''' assinatura: celula -> {1, 0, 1}
    ::  Devolve o valor da celula'''    
    return celula[0]

'''modificador'''
def inverte_estado(celula):
    ''' assinatura: celula -> celula
    ::  Inverte o estado da celula'''     
    if celula == [1]:
        celula[0] = 0
        return celula
    elif celula == [0]:
        celula[0] = 1
        return celula
    else:
        return celula
    
'''reconhecedor'''
def eh_celula(arg):
    ''' assinatura: universal -> logico
    ::  Verifica se o argumento e uma celula'''      
    return isinstance(arg, list) and len(arg)==1 and arg[0] in range(-1,2)

 
'''teste'''   
def celulas_iguais(c1, c2):
    ''' assinatura: celula*celula -> logico
    ::  Verifica se os argumentos sao celulas iguais'''       
    return eh_celula(c1) and eh_celula(c2) and c1[0] == c2[0]
    
    
'''transformador'''
def celula_para_str(celula):
    ''' assinatura: celula -> cadeia de carateres
    ::  Devolve a string que representa a celula'''     
    if celula == [0]:
        return '0'
    elif celula == [1]:
        return '1'
    else:
        return 'x'
    
#--COORDENADA--#
'''construtor'''    
def cria_coordenada(l, c):
    ''' assinatura: natural*natural -> coordenada
    ::  Uma coordenada consiste numa lista com 2 elementos, ambos digitos entre 0 e 2, em que o primeiro representa a linha e o segundo a coluna'''       
    if isinstance(l, int) and l in range(0,3) and isinstance(c, int) and c in range(0,3):
        return [l,c]
    else:
        raise ValueError('cria_coordenada: argumentos invalidos.')
    
'''seletores'''
def coordenada_linha(coordenada):
    ''' assinatura: coordenada -> natural
    ::  Devolve a linha representada na coordenada'''     
    return coordenada[0]

def coordenada_coluna(coordenada):
    ''' assinatura: coordenada -> natural
    ::  Devolve a coluna representada na coordenada'''     
    return coordenada[1]

'''reconhecedor'''
def eh_coordenada(arg):
    ''' assinatura: universal -> logico
    ::  Verifica se o argumento e uma coordenada'''     
    return isinstance(arg, list) and len(arg)==2 and isinstance(arg[0], int) and arg[0]>=0 and arg[0]<=2 and isinstance(arg[1], int) and arg[1]>=0 and arg[1]<=2
        
    
'''teste'''
def coordenadas_iguais(c1, c2):
    ''' assinatura: coordenada*coordenada -> logico
    ::  Verifica se os argumentos sao coordenadas iguais'''     
    return eh_coordenada(c1) and eh_coordenada(c2) and c1[0] == c2[0] and c1[1] == c2[1]

    
'''transformador'''
def coordenada_para_str(c):
    ''' assinatura: coordenada -> cadeia de carateres
    ::  Devolve a string correspondente a coordenada'''     
    return str(tuple(c))


#--TABULEIRO--#
'''construtores'''
def tabuleiro_inicial():
    ''' assinatura: {} -> tabuleiro
    ::  Devolve o tabuleiro inicial. Um tabuleiro consiste numa lista com sublistas, cada qual representando uma linha da matriz. Cada sublista contem celulas.'''     
    return [[cria_celula(-1),cria_celula(-1),cria_celula(-1)],[cria_celula(0),cria_celula(0),cria_celula(-1)],[cria_celula(0),cria_celula(-1)]]

def str_para_tabuleiro(string): 
    ''' assinatura: cadeia de carateres -> tabuleiro
    ::  Devolve a coluna representada na coordenada'''     
    try: 
        if eh_tabuleiro(tuplo_para_lista(eval(string))):
            return tuplo_para_lista(eval(string))
        else:
            raise ValueError('str_para_tabuleiro: argumento invalido.')
    except:
        raise ValueError('str_para_tabuleiro: argumento invalido.')
    
def tuplo_para_lista(tab): #AUXILIAR
    '''recebe um tabuleiro sob a forma de tuplos com tuplos e devolve o tabuleiro na representacao escolhida(listas com listas)'''
    novo_tab0 = []
    novo_tab1 = []
    novo_tab2 = []
    if isinstance(tab, tuple) and len(tab)==3 and isinstance(tab[0], tuple) and isinstance(tab[1], tuple) and isinstance(tab[2], tuple):
        for num in tab[0]:
            novo_tab0.append(cria_celula(num))
        for num in tab[1]:
            novo_tab1.append(cria_celula(num))        
        for num in tab[2]:
            novo_tab2.append(cria_celula(num)) 
        return [novo_tab0, novo_tab1, novo_tab2]
                

'''seletores'''
def tabuleiro_dimensao(tab):
    ''' assinatura: tabuleiro -> natural
    ::  Devolve o comprimento do tabuleiro'''       
    return len(tab)

def tabuleiro_celula(t, coor):
    ''' assinatura: tabuleiro*coordenada -> celula
    ::  Devolve a celula presente na coordenada coor'''       
    if eh_tabuleiro(t) and eh_coordenada(coor) and coordenada_linha(coor)!=2:
        return t[coordenada_linha(coor)][coordenada_coluna(coor)]
    elif eh_tabuleiro(t) and coordenada_linha(coor) == 2 and coordenada_coluna(coor) == 1: #Nao existe coordenada (2,0) no tabuleiro, logo altera a coordenada argumento para a coordenada 'real'
        coor = cria_coordenada(2,0)
        return t[coordenada_linha(coor)][coordenada_coluna(coor)]
    elif eh_tabuleiro(t) and coordenada_linha(coor) == 2 and coordenada_coluna(coor) == 2:
        coor = cria_coordenada(2,1) 
        return t[coordenada_linha(coor)][coordenada_coluna(coor)]

'''reconhecedor'''
def eh_tabuleiro(t):
    ''' assinatura: universal -> logico
    ::  Verifica se o argumento e um tabuleiro'''      
    if isinstance(t, list) and len(t)==3 and isinstance(t[0], list) and isinstance(t[1], list) and isinstance(t[2], list) and len(t[0])==len(t[1])==3 and len(t[2])==2:
        for l in t:
            for e in l:
                if not eh_celula(e):
                    return False
        return True
    else:
        return False
    
'''modificadores'''
def tabuleiro_substitui_celula(t, cel, coor):
    ''' assinatura: tabuleiro*celula*coordenada -> tabuleiro
    ::  Devolve o tabuleiro com a celula escolhida na coordenada escolhida, modificando o argumento tabuleiro'''      
    if eh_celula(cel) and eh_coordenada(coor) and eh_tabuleiro(t):
        if coordenada_linha(coor)==2:
            if coordenada_coluna(coor) == 1:
                coor = cria_coordenada(2,0)
            elif coordenada_coluna(coor) == 2:
                coor = cria_coordenada(2,1)
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = cel
        return t
    else:
        raise ValueError('tabuleiro_substitui_celula: argumentos invalidos.')
    
def tabuleiro_inverte_estado(t, coor):
    ''' assinatura: tabuleiro*coordenada -> tabuleiro
    ::  Devolve o tabuleiro com a inversao de estado da celula na coordenada escolhida'''      
    if not eh_coordenada(coor) or not eh_tabuleiro(t):
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')
    elif coordenada_linha(coor) == 2 and coordenada_coluna(coor) == 0:
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')
    return tabuleiro_substitui_celula(t, inverte_estado(tabuleiro_celula(t, coor)), coor) 
          
'''teste'''
def buscar_lista(tab): #AUXILIAR
    ''' tranforma um tabuleiro na representacao escolhida numa lista cujos elementos sao a representacao em string de cada elemento do tabuleiro'''
    lista = []
    if eh_tabuleiro(tab)==True: 
        for e in tab: 
            for cel in e:
                if obter_valor(cel)==1:
                    lista.append('1')
                elif obter_valor(cel)==0:
                    lista.append('0')
                else:
                    lista.append('x')            
    return lista 

def tabuleiros_iguais(tab1, tab2): 
    ''' assinatura: tabuleiro*tabuleiro -> logico
    ::  Verifica se os argumentos sao iguais'''      
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2): 
        valor = True 
        lista1=buscar_lista(tab1) 
        lista2=buscar_lista(tab2)
        for i in range(len(lista1)): 
            if lista1[i]!=lista2[i]: 
                valor = False 
        return valor 
    else:
        return False
    
'''reconhecedor'''
def tabuleiro_para_str(t):
    ''' assinatura: tabuleiro -> cadeia de carateres
    ::  Devolve a representacao visual do tabuleiro'''      
    figura = ('+-------+\n|...'+ celula_para_str(tabuleiro_celula(t,cria_coordenada(0,2)))+'...|\n|..'+celula_para_str(tabuleiro_celula(t,cria_coordenada(0,1)))+'.'+celula_para_str(tabuleiro_celula(t,cria_coordenada(1,2)))+'..|\n|.'+celula_para_str(tabuleiro_celula(t,cria_coordenada(0,0)))+'.'+celula_para_str(tabuleiro_celula(t,cria_coordenada(1,1)))+'.'+celula_para_str(tabuleiro_celula(t,cria_coordenada(2,2)))+'.|\n|..'+celula_para_str(tabuleiro_celula(t,cria_coordenada(1,0)))+'.'+celula_para_str(tabuleiro_celula(t,cria_coordenada(2,1)))+'..|\n+-------+')
    return figura

#--OPERACOES DE ALTO NIVEL--#
def porta_x(t, p):
    ''' assinatura: tabuleiro*{'E','D'} -> tabuleiro
    ::  Devolve o tabuleiro resultante da aplicacao da porta x, com recurso ao uso repetido da funcao tabuleiro_inverte_estado'''      
    if p == 'E' and eh_tabuleiro(t):
        return tabuleiro_inverte_estado(tabuleiro_inverte_estado(tabuleiro_inverte_estado(t, cria_coordenada(1,2)), cria_coordenada(1,1)), cria_coordenada(1,0))
    if p == 'D' and eh_tabuleiro(t):
        return tabuleiro_inverte_estado(tabuleiro_inverte_estado(tabuleiro_inverte_estado(t, cria_coordenada(0,1)), cria_coordenada(1,1)), cria_coordenada(2,1))
    else:
        raise ValueError('porta_x: argumentos invalidos.')
    
def porta_z(t, p):
    ''' assinatura: tabuleiro*{'E','D'} -> tabuleiro
    ::  Devolve o tabuleiro resultante da aplicacao da porta z, com recurso ao uso repetido da funcao tabuleiro_inverte_estado'''      
    if p == 'E' and eh_tabuleiro(t):
        return tabuleiro_inverte_estado(tabuleiro_inverte_estado(tabuleiro_inverte_estado(t, cria_coordenada(0,2)),cria_coordenada(0,1)), cria_coordenada(0,0)) 
    if p == 'D' and eh_tabuleiro(t):
        return tabuleiro_inverte_estado(tabuleiro_inverte_estado(tabuleiro_inverte_estado(t, cria_coordenada(0,2)),cria_coordenada(1,2)), cria_coordenada(2,2))
    else:
        raise ValueError('porta_z: argumentos invalidos.')  
    
def troca(t, c1, c2): #AUXILIAR
    ''' recebe um tabuleiro e duas coordenadas
    ::  Devolve o tabuleiro resultante da troca das celulas presentes nas coordenadas c1 e c2 '''
    cel1 = tabuleiro_celula(t, c1)
    cel2 = tabuleiro_celula(t, c2)
    return tabuleiro_substitui_celula(tabuleiro_substitui_celula(t, cel1, c2), cel2, c1)
    
        
def porta_h(t, p):
    ''' assinatura: tabuleiro*{'E','D'} -> tabuleiro
    ::  Devolve o tabuleiro resultante da aplicacao da porta z, com recurso ao uso repetido da funcao auxiliar troca'''      
    if p == 'E' and eh_tabuleiro(t):
        t = troca(troca(troca(t, cria_coordenada(0,2), cria_coordenada(1,2)), cria_coordenada(0,1), cria_coordenada(1,1)), cria_coordenada(0,0), cria_coordenada(1,0))
        return t
    elif p == 'D' and eh_tabuleiro(t):
        t = troca(troca(troca(t, cria_coordenada(2,1), cria_coordenada(2,2)), cria_coordenada(1,1), cria_coordenada(1,2)), cria_coordenada(0,1), cria_coordenada(0,2))
        return t
    else:
        raise ValueError('porta_h: argumentos invalidos.')    


#------------HELLO QUANTUM-------------#
def hello_quantum(string):
    ''' assinatura: cadeia de carateres -> logico
    ::  PERMITE JOGAR HELLO QUANTUM :) '''      
    print('Bem-vindo ao Hello Quantum!')
    print('O seu objetivo e chegar ao tabuleiro:')
    print(tabuleiro_para_str(tuplo_para_lista(tirar_tab(string))))
    print('Comecando com o tabuleiro que se segue:')
    print(tabuleiro_para_str(tabuleiro_inicial()))
    num_jogadas = 0
    tab_atual = tabuleiro_inicial()
    while num_jogadas < tirar_jogadas(string):
        porta = input('Escolha uma porta para aplicar (X, Z ou H): ')
        qubit = input('Escolha um qubit para analisar (E ou D): ')
        if porta == 'X':
            tab_atual = porta_x(tab_atual, qubit)
        elif porta == 'Z':
            tab_atual = porta_z(tab_atual, qubit)
        elif porta == 'H':
            tab_atual = porta_h(tab_atual, qubit)
        num_jogadas += 1
        print(tabuleiro_para_str(tab_atual))
        if tabuleiros_iguais(tab_atual, tuplo_para_lista(tirar_tab(string))):
            print('Parabens, conseguiu converter o tabuleiro em ' + str(num_jogadas) + ' jogadas!')
            return True
    return False

        
def tirar_tab(string): #AUXILIAR
    ''' retira o tabuleiro presente na string que funciona como argumento na funcao hello_quantum '''
    a,b = string.split(':')
    return eval(a)
def tirar_jogadas(string): #AUXILIAR
    ''' retira o numero de jogadas presente na string que funciona como argumento na funcao hello_quantum '''
    a,b = string.split(':')
    return eval(b)