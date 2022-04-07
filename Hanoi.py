class Stack:
  
  def __init__(self):
    self.__container = []

  #Insere elemento no Topo da Pilha
  def push(self, item):
    self.__container.append(item)
  
  #Remove elemento no Topo da Pilha
  def pop(self):
    return self.__container.pop()
  
  def is_valid_pop(self):
    return len(self.__container) >= 1

  #Mostra elemento no Topo da Pilha
  def peek(self):
    if len(self.__container) > 0:
      return self.__container[-1]
    return 0

  def __str__(self):
      return f'{self.__container}'

class Hanoi:
  # Construtor - Cria a Torre_a, Torre_B, Torre_C
  # Adiciona os itens 3,2,1 na Torre_A
  def __init__(self):
    self.torre_a = Stack()
    self.torre_b = Stack()
    self.torre_c = Stack()
    self.torre_a.push(3)
    self.torre_a.push(2)
    self.torre_a.push(1)
    self.movimentos = 0


  # Método Movimenta(Torre de Origem, Torre de destino)
  # Movimenta o elemento de um torre para outra
  def movimenta(self, torre_origem, torre_destino):
    self.movimentos= self.movimentos + 1
    if self.verifica_condicao(torre_origem, torre_destino):
      torre_destino.push(torre_origem.pop())
    else:
      print('Não é possivel fazer o movimento')

  # Mostra os valores das torres A, B e C
  def mostra_jogo(self):
    print('########################')
    print(f'Torre A: {self.torre_a}')
    print(f'Torre B: {self.torre_b}')
    print(f'Torre C: {self.torre_c}')
    print('########################')
  
  # Verifica_condição
  # nao pode movimentar de torres que nao tem elementos
  # maior nao pode ficar em cima di menor
  def verifica_condicao(self, torre_origem, torre_destino):
    if torre_destino.peek() == 0:
      return True
    if torre_destino.peek() > torre_origem.peek():
      return True
    return False
  
  #Verifica se o elemento pode ser movido

  #Verifica se o jogo acabou
  #Método Resolve (1 Passo: Movimenta Disco 1 para torre 3, ...)
  def o_jogo_terminou(self):
    if f'{self.torre_c}' == '[3, 2, 1]':
      print("O jogo terminou!!")
      print(f"Quantidade de movimentos {self.movimentos}")





jogo = Hanoi()
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_a, jogo.torre_c)
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_a, jogo.torre_b)
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_c, jogo.torre_b)
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_a, jogo.torre_c)
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_b, jogo.torre_a)
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_b, jogo.torre_c)
jogo.mostra_jogo()
jogo.movimenta(jogo.torre_a, jogo.torre_c)
jogo.mostra_jogo()
jogo.o_jogo_terminou()






