import requests, os

#criando a função main
def main():
    print('#####################')
    print('### Consulta CEP ###')
    print('#####################')
    print()

    #input do cep
    cep_input = input('Digite um Cep para consulta: ')

    #validação da quantidade de digitos
    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        refazer = int(input('''Deseja inserir novamente? 
        [1] - Sim
        [2] - Não 
        Resposta: '''))
        if refazer == 1:
            os.system('cls')
            main()

    #requisição da API
    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')

    #armazenando resultado json em uma variavel
    address_data = request.json()
    print(address_data)

    #validação de CEP (válido ou inválido)
    if 'erro' not in address_data:
        print('==> CEP encontrado <==')
        for c, v in address_data.items():
           print(f'{c} = {v}')

    else:
        print(f'{cep_input}: CEP inválido!')
        print('-='*25)

    #Nova consulta
    opção = int(input('''Deseja realizar uma nova consulta?
    [1] - Sim
    [2] - Não
    Resposta: '''))
    if opção == 1:
        os.system('cls')
        main()
    else:
        print('==> Encerrando <==')

if __name__ == '__main__':
    main()
    