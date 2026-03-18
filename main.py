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
        pass

    def start(self):
        pass


app = App()
app.start()



