from shoppinglib.users import user_exists, create_user, get_user_password


class App:

    def __init__(self):
        pass

    def validate_login(self, login, password):
        pass

    def register(self):
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        create_user(login, senha)
        print("Usuário cadastrado com sucesso!")

    def get_login(self):
        login = input("Login: ")
        senha = input("Senha: ")
        user_exists(login, senha)

    def start(self):
        while True:
            print("\n1 - Login")
            print("2 - Cadastrar")
            print("3 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                login, senha = user_exists()
                if self.validate_login(login, senha):
                    print("Login realizado com sucesso!")
                else:
                    print("Login ou senha incorretos.")

            elif opcao == "2":
                self.register()

            elif opcao == "3":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida.")



app = App()
app.start()



