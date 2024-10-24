
class Programa:
    def __init__(self):
        self.menu()
    
    def menu(self):
        while True:
            print('\n'
                '[1] - Create \n'
                '[2] - Read \n'
                '[3] - Update \n'
                '[4] - Delete \n'
                '[5] - Exit \n'
                '\n'
                )
            op = int(input('Escolha uma opção: '))
            match op:
                case 1:
                    print('Create')
                case 2:
                    print('Read')
                case 3:
                    print('Update')
                case 4:
                    print('Delete')
                case 5:
                    print('Você saiu...')
                    break
                case _:
                    print('Opção inválida!')

teste = Programa()

