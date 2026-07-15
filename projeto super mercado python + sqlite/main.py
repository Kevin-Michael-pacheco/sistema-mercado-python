from banco import Banco


b = Banco()

def menu_cadastrar():
        nome_produto = input('digite o nome do produto: ').strip()
        if nome_produto == '':
                print('o nome do produto não pode ficar vazio')
        else:
            try:
                preco_produto = float(input('digite o preço do produto: ').replace(",", "."))
                if preco_produto >= 0:
                    try:
                        estoque_produto = int(input('digite a quantidade disponivel do produto: '))
                        if estoque_produto >= 0:
                            result = b.cadastrar(nome_produto, preco_produto, estoque_produto)
                            if result:
                                print('produto cadastrado com sucesso')
                            else:
                                print('o produto ja existe por isso não foi cadastrado de novo')
                        else:
                            print('o estoque do produto tem que ser maior ou igual a 0')
                    except ValueError:
                        print('ERRO.O estoque do produto so pode ser em numeros inteiros')
                else:
                    print('o preço do produto tem que ser maior ou igual a 0')
            except ValueError:
                print('ERRO.O preço do produto so pode ser em numeros')

def menu_listar():
    produtos = b.listar()
    if not produtos:
        print('nenhum produto foi cadastrado')
    else:
        for id,nome, preco, estoque in produtos:
            print(f"id: {id} |nome: {nome} | preço: {preco} | estoque: {estoque}")


def menu_buscar_por_id():
    try:
        id_produto = int(input('digite a id do produto que deseja encontrar: '))
        produto = b.buscar(id_produto)
        if not produto:
            print('o produto não foi encontrado')
        else:
            id, nome, preco, estoque = produto
            print(f"id: {id}  |nome: {nome} | preço: {preco} | estoque: {estoque}")
    except ValueError:
        print('ERRO.A id do produto so pode ser em numeros inteiros')


def menu_editar_produto():
    try:
        produto_id = int(input('digite a id do produto que deseja editar: '))
        nome_novo = input('digite o novo nome do produto: ').strip()
        if nome_novo == '':
            print('o nome novo do produto não pode ficar vazio')
        else:
            try:
                preco_novo = float(input('digite o novo preço do produto: '))
                if preco_novo >= 0:
                    try:
                        estoque_novo = int(input('digite a quantidade em estoque do produto: '))
                        if estoque_novo >= 0:
                            print(b.editar(produto_id, nome_novo, preco_novo, estoque_novo))
                        else:
                             print('o estoque do produto tem que ser maior ou igual a 0')
                    except ValueError:
                        print('ERRO.O estoque do produto so pode ser em numeros inteiros')
                else:
                    print('o preço do produto so poder ser maio ou igual a 0')
            except ValueError:
                print('ERRO.O preço do produto so pode ser em numeros')
    except ValueError:
        print('ERRO.A id do produto so pode ser em numeros inteiros')
        
            
def menu_deletar():
    try:
        id_produto_= int(input('digite a id do produto que deseja deletar: '))
        deletado = b.deletar(id_produto_)
        if deletado:
            print('o produto foi deletado com sucesso')
        else:
            print('o produto não foi encontrado')
            
    except ValueError:
        print('ERRO.A id do produto so pode ser em numeros inteiros')


def menu_buscar_por_nome():
    nome_procurar = input('digite o nome do produto que deseja encontrar: ').strip()
    if nome_procurar == '':
        print('o nome não pode ficar vazio')
    else:
        encontrado = b.buscar_por_nome(nome_procurar)
        if not encontrado:
            print('o produto não foi encontrado')
        else:
            for id , nome, preco, estoque in encontrado:
                print(f"id: {id} | nome: {nome} | preço: {preco} | estoque: {estoque}")
        

def menu_adicionar_estoque():
    try:
        produto_id_ = int(input('digite a id do produto que deseja adicionar estoque: '))
        try:
            qtd_adicionar = int(input('digite a quantidade do produto que deseja adicionar ao estoque: '))
            if qtd_adicionar >= 1:
                localizado = b.entrada_estoque(produto_id_, qtd_adicionar)
                if localizado :
                    print('o estoque fo iadicionado ao produto com sucesso')
                else:
                    print('o produto não foi encontrado')
                            
            else:
                print('não pode ser adicionado numero negativos no banco de dados')
        except ValueError:
            print('ERRO.A quantidade de estoque a ser adicionada no produto tem que ser apenas em numeros inteiros')

    except ValueError:
        print('ERRO.A id do produto pode ser apenas em numeros inteiros')


def menu_vender():
    try:
        id_produto__ = int(input('digite a id do porduto que deseja realizar a venda: '))
        try:
            qtd_venda = int(input('digite a quantidade do produto que sera vendido: '))
            if qtd_venda >= 1:
                vendido = b.vender(id_produto__, qtd_venda)
                if vendido :
                    print('venda concluida com sucesso')
                else:
                    print('o produto não foi encontrado ou o estoque esta insufisiente pra quantidade da compra')
                           
            else:
                print('a quantidade do produto a ser vendido tem que ser maior que 0')
        except ValueError:
            print('ERRO.A qauntidade a ser vendidad do prosuto tem que ser apenas em  numeros inteiros')
    except ValueError:
        print('ERRO.A id do produto so pode ser em numeros interos')

def menu_encerrar():
    print('programa encerrado')

def opcao_invalida():
    print('ERRO.Digite apenas opções disponiveis')

def mostrar_menu():
    print('===== MENU =====')
    print('1 - cadastrar produto')
    print('2 - listar produtos')
    print('3 - buscar produtos cadastrado')
    print('4 - editar produto cadastrado')
    print('5 - excluir produto cadastrado')
    print('6 - buscar por nome')
    print('7 - adicionar estoque')
    print('8 - vender produto')
    print('9 - sair')

def main():
    while True:
        mostrar_menu()
        op = input('digite a opção desejada: ').strip()
        if op == '1':
            menu_cadastrar()
  
        elif op == '2':
            menu_listar()
         
        
        elif op == '3':
            menu_buscar_por_id()
         

        elif op == '4':
            menu_editar_produto()
        
        elif op == '5':
            menu_deletar()
           
        elif op == '6':
            menu_buscar_por_nome()

        elif op == '7':
            menu_adicionar_estoque()
           
        elif op == '8':
            menu_vender()
        
        elif op == '9':
            menu_encerrar()
            break

        else:
            opcao_invalida()

main()

