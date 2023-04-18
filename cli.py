class SimpleCLI:
    def __init__(self):
        self.commands={}
    def add_command(self,name,function):
        self.commands[name]=function
    def run(self):
        while True:
            command=input("Entre com um comando: ")
            if command=="quit":
                print("Godbye")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command")

class PersonCLI(SimpleCLI):
    def __init__(self,person_model):
        super().__init__()
        self.person_model=person_model
        self.add_command("create",self.create_person)
        self.add_command("read",self.read_person)
        self.add_command("update", self.update_person)
        self.add_command("delete", self.delete_person)

    def create_person(self):
        titulo=input("Entre com o titulo: ")
        autor=input("autor: ")
        ano = input("ano: ")
        preco = input("preco: ")
        self.person_model.create_person(titulo,autor,ano,preco)

    def read_person(self):
        id=input("Entre com o id: ")
        person:PersonCLI.person_model.read_person_by_id(id)
        if person:
            print(f"name:{person['titulo']}")
            print(f"name:{person['autor']}")
            print(f"name:{person['ano']}")
            print(f"name:{person['preco']}")


    def update_person(self):
        id=input("Entre com id: ")
        titulo= input("Entre com o novo titulo: ")
        autor = input("Entre com o novo nome do autor: ")
        ano = input("Entre com o novo ano: ")
        preco = input("novo preco: ")
        self.person_model.update_person(id,titulo,autor,ano,preco)

    def delete_person(self):
        id=input("Entre com o id: ")
        self.person_model.delete_person(id)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read,update,delete,quit")
        super().run()


