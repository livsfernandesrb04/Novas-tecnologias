#Crie um módulo simples em Python para gerenciar os usuários de um sistema.
class Usuario:
    #Crie uma classe Usuario com os atributos privados: __id, __nome e __email.
    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = email
    
    #Implemente o método construtor (__init__) e os métodos Getters e Setters para acessar 
    # e modificar esses atributos com segurança.
    def get_id(self):
        return self.__id
    
    def set_id(self, newId):
        self.__id = newId

    id = property(get_id, set_id)

    def get_nome(self):
        return self.__nome

    def set_nome(self, newName):
        self.__nome = newName

    nome = property(get_nome, set_nome)

    def get_email(self):
        return self.__email

    def set_email(self, newEmail):
        #Adicione uma validação de regra de negócio no setter de e-mail: ele só deve atualizar o valor 
        # se a string recebida contiver o caractere "@".
        validEmail = False
        for caracter in newEmail:
            if caracter == '@':
                validEmail = True
            
        if validEmail == True:
            self.__email = newEmail    
        else:
            # Caso contrário, exiba uma mensagem de erro ("E-mail inválido").
            print("E-mail inválido")


    email = property(get_email, set_email)

#Crie uma classe GerenciadorUsuarios que contenha uma lista (inicialmente vazia) para armazenar objetos do tipo Usuario. 

class GerenciadorUsuario:
    usuario = []
    # Ela deve ter os métodos adicionar_usuario(usuario), remover_usuario_por_id(id) e listar_usuarios().
    def adicionar_usuario(usuario)
    
    def remover_usuario_por_id(id)
    
    def listar_usuario()
