import json
import os

usersData = os.path.join(os.path.dirname(__file__), 'usuariosData.json')


def carregar_user():
    if not os.path.exists(usersData):
        with open(usersData, 'w') as userDataArquivo:
            json.dump([], userDataArquivo, indent=4)


def adicionar_user(nome, idade, genero, contato, cpf):
    users = carregar_user()
    if users is None:
        users = []
    
    users.append({'nome': nome, 'idade': idade, 'genero': genero, 'contato': contato, 'cpf': cpf})

    with open(usersData, 'w') as userDataArquivo:
        json.dump(users, userDataArquivo, indent=4, ensure_ascii=False)
    print("Você foi cadastrado com sucesso :)")
    
    
def listar_user():
    users = carregar_user()

    if users:
        print("=" *50)
        print("Lista de usuários: ")
        print("-" *50)
        for user in users:
            print("*" *50)
            print(f"Nome: {user['nome']}, Idade: {user['idade']}, Gênero: {user['genero']}, Telefone:{user['telefone']}, CPF:{user['cpf']}")
            print("*" *50)
            print("=" *50)
    else:
        print("Nenhum usuário cadastrado")


def menu_user():
    print("\nMENU USUÁRIOS:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")
    

def main(): 
    while True:
        
        menu_user()
        op= input("Escolha uma opção: ")
    
        if op == "1":
            nome=input("Digite o seu nome: ")          
            idade=input("Digite sua idade: ")      
            genero=input("Digite seu gênero: ")
            contato=input("Digite seu telefone: ")
            cpf= input("Digite seu CPF: ")
            adicionar_user(nome,idade,genero,contato,cpf)
            
        elif op == "2":
            listar_user()         
            #TÁ DANDO ERRO 
            
        elif op == "3":
            antigoNome=input("Digite o seu antigo nome: ")
            novoNome=input("Digite o seu novo nome: ")                                
            novaIdade=input("Digite a sua anitga idade: ") 
            antigaIdade=input("Digite a sua nova idade: ")      
            antigoGenero=input("Digite o seu antigo gênero: ")
            novoGenero=input("Digite o seu novo gênero: ")
            antigoContato=input("Digite o seu antigo telefone: ")
            novoContato=input("Digite o seu novo telefone: ")
            antigoCpf= input("Digite o seu antigo CPF: ")
            novoCpf= input("Digite o seu novo CPF: ")
            
            
            
if __name__ == "__main__":
    main()