lista = []

while True:
    opcao = input(
        '\n'
        'Escolha uma opção:\n'
        'Cadastrar produto = 1\n'
        'Atualizar produto = 2\n'
        'Exibir lista = 3\n'
        'Exibir lista invertida = 4\n'
        'Sair = 0\n'
        'Opção: '
    )

    if opcao == '1':
        produto = []  # Cria uma nova lista para o produto
        produto.append(input('\nNome do produto: '))
        produto.append(input('Quantidade do produto: '))
        lista.append(produto)
        print('\nLista atualizada')
        for item in lista:
            print(item)

    elif opcao == '2':
        nome_produto = input('\nNome do produto a ser atualizado: ')

        # variavel para guardar o produto caso ele seja encontrado
        produto_atualizado = None
        for produto in lista:
            # if verificando se o nome do produto é o mesmo que foi digitado
            if produto[0] == nome_produto:
                produto_atualizado = produto
                break

        # pedindo as novas informações
        if produto_atualizado:
            novo_nome = input(
                'Novo nome do produto (caso não queira mudar deixe em branco): ')
            nova_quantidade = input(
                'Nova quantidade do produto (caso não queira mudar deixe em branco): ')

            # fazendo as atualizações
            if novo_nome:
                produto_atualizado[0] = novo_nome
            if nova_quantidade:
                produto_atualizado[1] = nova_quantidade

            # retornando um print caso de certo
            print('Produto atualizado')
        else:
            print('Produto não encontrado.')

    elif opcao == '3':
        print('\nLista de produtos:')
        lista_ordenada = sorted(lista, key=lambda x: x[0])
        for item in lista_ordenada:
            print(item)

    elif opcao == '4':
        print('\nLista de produtos invertida:')
        lista_ordenada = sorted(lista, key=lambda x: x[0])
        lista_inversa = lista_ordenada.reverse
        for item in lista_inversa:
            print(item)

    elif opcao == '0':
        print('Saindo do programa.')
        break

    else:
        print('Opção inválida. Tente novamente.')
