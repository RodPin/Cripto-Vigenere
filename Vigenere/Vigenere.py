ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
def main():
    #pedir a mensagem
    print('MENSAGEM:')
    mensagem = input()
    print('CHAVE')
    key = input()
 

    traduzida = decryptMessage( mensagem)
 
    print(traduzida)
 

 
def decryptMessage(message):
    return traduzirMensagem(message)
 
 
def traduzirMensagem( message):
    traduzida = [] #mensagem que vai aparecer
 
    keyIndex = 0
    
 
    for charactere in message: # loop atraves de todos os caracteres
        num = ALFABETO.find(charactere.upper())
        num -= ALFABETO.find(key[keyIndex]) # Setar pra subtrair na decriptacao
            #Adicionar as caracteres
        if charactere.isupper():
            traduzida.append(ALFABETO[num])
        elif charactere.islower():
            traduzida.append(ALFABETO[num].lower())
 
        keyIndex += 1 #Mudar de letra na chave
        if keyIndex == len(key):
            keyIndex = 0
 
    return ''.join(traduzida)
 
main()
