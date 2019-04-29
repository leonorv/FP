# 92509 Leonor Veloso

def eh_tabuleiro(t):
    ''' recebe qualquer tipo de input e devolve True caso o argumento seja um tabuleiro e False caso nao seja
    ::  um tabuleiro consiste num tuplo que contem 3 tuplos (de comprimento 3,3,2 respetivamente) e cada elemento do tuplo deve ser 0,1 ou -1 '''
    value = False
    if isinstance(t,tuple) and len(t)==3: # verifica se t e um tuplo e se o seu comprimento e 3 
        for e in t: # verifica se cada elemento de t e um tuplo
            if not isinstance(e,tuple):
                return False # se nao, devolve False
        if len(t[0])==len(t[1])==3 and len(t[2])==2: # verifica se o comprimento dos 3 tuplos dentro de t e 3,3,2 respetivamente
            for e in t:
                    for num in e: # itera por todos os elementos dos tuplos
                        if isinstance(num, int): # verifica se os elementos sao inteiros
                            if num < -1 or num > 1:
                                return False # devolve False se houver um inteiro fora do intervalo [-1,1]
                            else:
                                value = True # guarda True se os elementos estiverem no intervalo [-1,1]
                        else:
                            return False # devolve False se um elemento nao for um inteiro

    return value # devolve o booleano guardado

# funcoes auxiliares

def buscar_lista(tab):
    ''' transforma um tabuleiro numa lista cujos elementos sao '1','0', ou '-1', de acordo com a sua ordem no tabuleiro 
    ::  o objetivo desta funcao extra e tranformar o tabuleiro num objeto mais maleavel 
    ::  a lista devolvida nao inclui sublistas , e cada elemento e uma string '''
    lista = []
    if eh_tabuleiro(tab)==True: # verifica se o argumento e um tabuleiro
        for e in tab: # percorre cada elemento do tabuleiro e junta a uma lista vazia esse elemento
            for num in e:
                if num==1:
                    lista.append('1')
                elif num==0:
                    lista.append('0')
                else:
                    lista.append('x') # a string 'x' corresponde a indeterminacao da celula com valor -1            
    return lista # devolve a lista

def buscar_tuplo(lista):
    ''' transforma uma lista conforme definida na funcao buscar_lista num tabuleiro
    ::  cada elemento da lista deve ser '1','0', ou '-1' 
    ::  o objetivo desta funcao extra e a facil tranformacao de uma lista (mais maleavel) num tabuleiro '''
    newlista=[]
    for element in lista: # percorre os elementos da lista e adiciona a uma lista vazia inteiros correspondentes
        if element=='x':
            newlista.append(-1)
        if element=='1':
            newlista.append(1)
        if element=='0':
            newlista.append(0)
    for i in range(1,len(newlista)): # percorre o comprimento da nova lista, que contem inteiros
        tuplo1=(newlista[0], newlista[1], newlista[2]) #tranforma a nova lista num tabuleiro
        tuplo2=(newlista[3], newlista[4], newlista[5])
        tuplo3=(newlista[6], newlista[7])
        tuplo=(tuplo1,tuplo2,tuplo3)
    return tuplo # devolve o tabuleiro criado

# fim das funcoes auxiliares

def tabuleiro_str(arg):
    ''' recebe um tabuleiro e devolve a sua representacao em cadeia de carateres, com os qubits fazendo um angulo de 45 graus com a horizontal '''
    lista=buscar_lista(arg) # transforma o tabuleiro numa lista
    if eh_tabuleiro(arg)==False: # verifica se o argumento da funcao e um tabuleiro e devolve ValueError se nao for
        raise ValueError('tabuleiro_str: argumento invalido')
    figura = ('+-------+\n|...'+ str(lista[2])+'...|\n|..'+str(lista[1])+'.'+str(lista[5])+'..|\n|.'+str(lista[0])+'.'+str(lista[4])+'.'+str(lista[7])+'.|\n|..'+str(lista[3])+'.'+str(lista[6])+'..|\n+-------+')
    return figura # devolve a string correspondente ao tabuleiro

    
    

def tabuleiros_iguais(tab1, tab2):
    ''' recebe dois tabuleiros e devolve True se forem iguais e False se nao o forem ''' 
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2): # verifica se ambos os argumentos sao tabuleiros
        valor = True # inicializa o valor logico como True
        lista1=buscar_lista(tab1) # transforma cada tabuleiro numa lista em que cada elemento e uma string
        lista2=buscar_lista(tab2)
        for i in range(len(lista1)): # percorre o comprimento da lista
            if lista1[i]!=lista2[i]: # verifica se ha diferencas entre os elementos de cada lista
                valor = False # se sim, o valor logico e False
        return valor # devolve o valor logico
    else:
        raise ValueError('tabuleiros_iguais: um dos argumentos nao e tabuleiro') # se os argumentos nao forem tabuleiros, devolve ValueError
                    
    
        
def porta_x(tab, car):
    ''' recebe um tabuleiro e um caracter 'E' ou 'D' e aplica a porta x ao qubit esquerdo ou direito, respetivamente
    ::  devolve um novo tabuleiro '''
    if eh_tabuleiro(tab)==False: # verifica se o argumento tab e um tabuleiro, se nao devolve ValueError
        raise ValueError('porta_x: um dos argumentos e invalido')
    else:
        newlista=[] # inicializamos uma nova lista vazia
        if car=='E': # verifica se aplicamos a porta x ao qubit da esquerda
            lista = buscar_lista(tab) # transformamos o tabuleiro numa lista para maior maleabilidade
            for i in range(len(lista)): # percorre o comprimento da lista
                if i==3 or i==4 or i==5: # esta seccao de codigo faz as tranformacoes as celulas correspondentes as da porta x, tendo em atencao as suas posicoes na lista criada
                    if lista[i]=='x':
                        newlista.append('x')
                    if lista[i]=='1':
                        newlista.append('0')
                    if lista[i]=='0':
                        newlista.append('1')
                else:
                    newlista.append(lista[i])
        
            tuplo=buscar_tuplo(newlista) # retransforma a nova lista num tabuleiro
            return tuplo # devolve o tabuleiro
        if car=='D': # verifica se aplicamos a porta x ao qubit da direita
            lista = buscar_lista(tab)
            for i in range(len(lista)):
                if i==1 or i==4 or i==6: # transforma as celulas de acordo com a aplicacao da porta x 
                    if lista[i]=='x':
                        newlista.append('x')
                    if lista[i]=='1':
                        newlista.append('0')
                    if lista[i]=='0':
                        newlista.append('1')
                else:
                    newlista.append(lista[i])
            tuplo=buscar_tuplo(newlista)
            return tuplo
        else:
            raise ValueError('porta_x: um dos argumentos e invalido') # devolve ValueError se o input 'car' for diferente de 'E' ou 'D'
    
def porta_z(tab, car):
    ''' recebe um tabuleiro e um caracter 'E' ou 'D' e aplica a porta z ao qubit esquerdo ou direito, respetivamente
    ::  devolve um novo tabuleiro '''
    if eh_tabuleiro(tab)==False: # se tab nao for tabuleiro, devolve ValueError
        raise ValueError('porta_z: um dos argumentos e invalido')
    else: # o modus operandi do resto da funcao e semelhante ao da porta x, tendo apenas em conta as posicoes das celulas que se pretendem alterar
        newlista=[]
        if car=='E':
            lista = buscar_lista(tab)
            for i in range(len(lista)):
                if i==0 or i==1 or i==2:
                    if lista[i]=='x':
                        newlista.append('x')
                    if lista[i]=='1':
                        newlista.append('0')
                    if lista[i]=='0':
                        newlista.append('1')
                else:
                    newlista.append(lista[i])
            tuplo=buscar_tuplo(newlista)
            return tuplo
        if car=='D':
            lista = buscar_lista(tab)
            for i in range(len(lista)):
                if i==2 or i==5 or i==7:
                    if lista[i]=='x':
                        newlista.append('x')
                    if lista[i]=='1':
                        newlista.append('0')
                    if lista[i]=='0':
                        newlista.append('1')
                else:
                    newlista.append(lista[i])
            tuplo=buscar_tuplo(newlista)
            return tuplo
        else:
            raise ValueError('porta_z: um dos argumentos e invalido')
        
def porta_h(tab,car):
    ''' recebe um tabuleiro e um caracter 'E' ou 'D' e aplica a porta h ao qubit esquerdo ou direito, respetivamente
    ::  devolve um novo tabuleiro '''    
    if eh_tabuleiro(tab)==False:
        raise ValueError('porta_h: um dos argumentos e invalido')
    else:
        newlista=[]
        if car=='E':
            lista = buscar_lista(tab) 
            for i in range(len(lista)):
                if i==0 or i==1 or i==2:
                    newlista.append(lista[i+3]) # 'troca' as celulas, adicionando a uma nova lista vazia os novos elementos
                elif i==3 or i==4 or i==5:
                    newlista.append(lista[i-3])
                else:
                    newlista.append(lista[i])
            tuplo=buscar_tuplo(newlista)
            return tuplo # devolve o novo tabuleiro
        if car=='D':
            lista = buscar_lista(tab)
            for i in range(len(lista)):
                if i==2 or i==5 or i==7:
                    newlista.append(lista[i-1])
                elif i==1 or i==4 or i==6:
                    newlista.append(lista[i+1])
                else:
                    newlista.append(lista[i])
            tuplo=buscar_tuplo(newlista)
            return tuplo
        else:
            raise ValueError('porta_h: um dos argumentos e invalido')