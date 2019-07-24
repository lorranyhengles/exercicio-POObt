class Cliente:
    def __init__(self, nome_cliente, idade_cliente):
        self.nome_cliente = nome_cliente
        self.idade_cliente = idade_cliente

class Pet(Cliente):
    def __init__(self, nome_cliente, idade_cliente, nome_pet, idade_pet ):
        super().__init__(nome_cliente, idade_cliente)
        self.nome_pet = nome_pet
        self.idade_pet = idade_pet

cliente = Cliente('Lorrany','18 anos')
pet = Pet('nome_cliente','idade_cliente','Harry','4 anos')

print('A cliente se chama {} e possui {}'.format(cliente.nome_cliente, cliente.idade_cliente))
print('Ela é dona do gato {} que possui {}'.format(pet.nome_pet, pet.idade_pet))