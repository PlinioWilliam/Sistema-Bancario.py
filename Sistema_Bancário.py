import os

# FUNÇÃO PARA LIMPAR O PROMPT
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    

# VARIÁVEIS GLOBAIS
contaAberta = False
nome_cliente = ''
saldo_inicial = 0.0
saldo_atual = 0.0
saldo_minimo = None
saldo_maximo = None
quantidade_depositos = 0
valor_total_depositos = 0.0
quantiade_saques = 0
valor_total_saques = 0.0
valor_total_jurosRecebidods = 0.0

def abrir_conta(): # FUNÇÃO PARA ABRIR CONTA
    global nome_cliente, saldo_inicial, saldo_atual, contaAberta, saldo_maximo, saldo_minimo #VARIAVEIS GLOBAIS
    
    # SOLICITA O NOME DO USUARIO, SE FOR DIGITADO UM TEXTO VAZIO, RETORNA "VALOR INVALIDO" E SOLICITA NOVAMENTE O NOME DO USUARIO
    while True:
        nome_cliente = input('\nDigite seu nome completo: ')
        if nome_cliente.strip():
            break
        else:
            print('\nVALOR INVÁLIDO')
    
    #SOLICITA O SALDO INCIAL DO USUARIO, SE FOR UM VALOR MENOR QUE 0 OU UM VALOR INVALIDO COMO TEXTO, RETORNA ERRO E SOLICITA NOVAMENTE
    while True:
        try: # O PROGRAMA TENTA AS SEGUINTES REQUISIÇÕES
            saldo_inicial = float(input('Digite seu saldo inicial: R$'))
            if saldo_inicial >= 0:
                break
            else:
                print('\nVALOR INVÁLIDO\n')
        except ValueError: # CASO OCORRESSE O ERRO "ValueError", O TERMINAL PRINTA A MENSAGEM INFORMADA NO CÓDIGO E DA SEQUENCIA SEM DEIXAR O PROGRAMA QUEBRAR
            print('\nDIGITE UM NÚMERO\n')   
            
    saldo_atual += saldo_inicial # ATUALIZA O SALDO ATUAL
    
    print(f"\nConta criada com sucesso para {nome_cliente} com saldo de R${saldo_atual:.2f}\n")
    
    saldo_maximo = saldo_inicial # ATUALIZA O SALDO MAXIMO
    saldo_minimo = saldo_inicial # ATUALIZA O SALDO MINIMO
    contaAberta = True # ATUALIZA A VARIAVEL contaAberta PARA TRUE, ASSIM DANDO SEQUENCIA NO CODIGO PARA O PROXIMO MENU
    
def realizar_deposito(): # FUNÇÃO PARA REALIZAR DEPÓSITO
    global saldo_atual, saldo_inicial, quantidade_depositos, valor_total_depositos, saldo_maximo, saldo_minimo # VARIAVEIS GLOBAIS
    
    while True:
        try: # O PROGRAMA TENTA AS SEGUINTES REQUISIÇÕES
            valor_deposito = float(input('\nDigite o valor a ser depositado: ')) # SOLICITA O VALOR DO DEPOSITO
        
            # SE O VALOR DO DEPOSITO FOR MAIOR QUE 0, O PROGRAMA SEGUE, SE NÃO O PROGRAMA RETORNA UM ERRO E SOLICITA NOVAMENTE O VALOR DO DEPOSITO
            if valor_deposito > 0:
                saldo_atual += valor_deposito # ATUALIZA O VALOR DO SALDO ATUAL
                print(f'\nDepósito realizado com sucesso, seu novo saldo é: R${saldo_atual:.2f}\n')
                quantidade_depositos += 1 # ATUALIZA A QUANTIDADE DE DEPOSITOS
                valor_total_depositos += valor_deposito # ATUALIZA O VALOR TOTAL DOS DEPOSITOS
                break
            else:
                print('O valor precisa ser maior que 0') # ERRO INFORMADO CASO O VALOR SEJA MENOR OU IGUAL A ZERO
        except ValueError: # CASO OCORRESSE O ERRO "ValueError", O TERMINAL PRINTA A MENSAGEM INFORMADA NO CÓDIGO E DA SEQUENCIA SEM DEIXAR O PROGRAMA QUEBRAR
            print('O VALOR PRECISA SER NUMÉRICO') # ERRO INFORMADO CASO O VALOR INFORMADO NÃO SEJA UM NUMERO
            
    if saldo_atual > saldo_maximo: # SE O SALDO ATUAL FOR MAIOR QUE O SALDO MAXIMO, ATUALIZA O VALOR DA VARIAVEL SALDO MAXIMO
        saldo_maximo = saldo_atual
    if saldo_atual < saldo_minimo: # SE O SALDO ATUAL FOR MENOR QUE O SALDO MINIMO, ATUALIZA O VALOR DA VARIAVEL SALDO MINIMO
        saldo_minimo = saldo_atual
    
def realizar_saque(): # FUNÇÃO PARA REALIZAR O SAQUE
    global saldo_atual, quantiade_saques, valor_total_saques, saldo_maximo, saldo_minimo # VARAIVEIS GLOBAIS
    
    notas_disponiveis = [200, 100, 50, 20, 10, 5, 2] # LISTA CONTENDO OS VALORES CORRESPONDETES AS NOTAS DISPONIVEIS
    
    while True:
        saque = float(input('\nInforme o valor a ser sacado: R$')) # VARIAVEL PARA SER INFORMADO O VALOR A SER SACADO
        try: # O PROGRAMA TENTA AS SEGUINTES REQUISIÇÕES
            if saque > saldo_atual:
                print('\nVALOR INSUFICIENTE')
                
            elif saque > 0: # CASO O VALOR INFORMADO SEJA MAIOR QUE ZERO
                
                valor_restante = saque # ATUALIZA A VARIAVEL valor_restante
                liberar_notas = {}
        
                for notas in notas_disponiveis:
                    qnt_notas = valor_restante // notas
                    if qnt_notas > 0:
                        liberar_notas[notas] = int(qnt_notas)
                        valor_restante -= qnt_notas * notas
                
                if valor_restante == 0:
                    saldo_atual -= saque # ATUALIZA A VARIAVEL saldo_atual
                    quantiade_saques += 1 # ATUALIZA A VARIAVEL quantidade_saques
                    valor_total_saques += saque # ATUALIZA A VARIAVEL valor_total_saques
                    
                    print('\nNotas a serem liberadas:')
                    for notas, quantidade in liberar_notas.items():
                        print(f'# R${notas}: {quantidade} nota(s)')
                
                    print(f'\nSaque realizado com sucesso, seu novo saldo é: R${saldo_atual:.2f}\n')
                    break
                
                else:
                    valor_valido = saque - valor_restante
                    print(f'\nNão foi possível sacar o valor total solicitado (R${saque:.2f}) com as notas disponíveis.')
                    if valor_valido > 0:
                        print(f'\nValor liberado: R${valor_valido:.2f}')
                        print('\nNotas a serem liberadas:')
                        for nota, quantidade in liberar_notas.items():
                            print(f'# R${nota}: {quantidade} nota(s)')

                        saldo_atual -= valor_valido
                        quantiade_saques += 1
                        valor_total_saques += valor_valido
                    else:
                        print(f'\nNenhum valor pôde ser sacado com as notas disponíveis.')

                    print(f'\nValor não liberado: R${valor_restante:.2f}')
                    print(f'Seu saldo permanece em: R${saldo_atual:.2f}\n')
                    break

            else:
                print('\nO valor deve ser positivo.')
        except ValueError: # CASO OCORRESSE O ERRO "ValueError", O TERMINAL PRINTA A MENSAGEM INFORMADA NO CÓDIGO E DA SEQUENCIA SEM DEIXAR O PROGRAMA QUEBRAR
            print('\nDIGITE UM NÚMERO\n') # ERRO INFORMADO CASO O VALOR INFORMADO NÃO SEJA UM NUMERO
            
    if saldo_atual > saldo_maximo: # SE O SALDO ATUAL FOR MAIOR QUE O SALDO MAXIMO, ATUALIZA O VALOR DA VARIAVEL SALDO MAXIMO
        saldo_maximo = saldo_atual
    if saldo_atual < saldo_minimo: # SE O SALDO ATUAL FOR MENOR QUE O SALDO MINIMO, ATUALIZA O VALOR DA VARIAVEL SALDO MINIMO
        saldo_minimo = saldo_atual
    
def aplicar_juros(): # FUNÇÃO PARA APLICAR JUROS
    global saldo_atual, valor_total_jurosRecebidods, saldo_maximo, saldo_minimo # VARIAVEIS GLOBAIS
    
    while True:
        juros_percentual = float(input('\nInforme a porcentagem da taxa de juros: '))
        
        try: # SE O JUROS PERCENTUAL INFORMADO FOR MAIOR QUE 0, DA PROSSEGUIMENTO NO CODIGO, SE NÃO INFORMA UM ERRO E SOLICITA NOVAMENTE
            if juros_percentual > 0:
                juros = juros_percentual / 100 # DIVIDE O VALOR INFORMADO DO PERCENTUAL DO JUROS POR 100, ASSIM CRIANDO A VARIAVEL JUROS
                montante = saldo_atual * juros # MULTIPLICA O SALDO ATUAL PELO VALOR DO JUROS, ASSIM CRIANDO A VARIAVEL MONTANTE, CONTENDO O VALOR DO JUROS EM REAIS
                saldo_atual += montante # ATUALIZA O SALDO ATUAL
                valor_total_jurosRecebidods += montante # ATUALIZA O VALOR TOTAL DOS JUROS RECEBIDOS
            
                print(f'\nO percentual de juros foi %{juros_percentual}\nO montante corresponde ao valor de R${montante:.2f}\nO saldo atual corresponde a R${saldo_atual:.2f}\n')
                break
            else:
                print('O juros deve ser maior que 0') # ERRO INFORMADO CASO O VALOR DO PERCENTUAL DE JUROS SOLICITADO SEJA MENOR OU IGUAL A ZERO
        except ValueError:
            print('\nDIGITE UM NÚMERO\n') # ERRO INFORMADO CASO O VALOR INFORMADO NÃO SEJA UM NUMERO
            
    if saldo_atual > saldo_maximo: # SE O SALDO ATUAL FOR MAIOR QUE O SALDO MAXIMO, ATUALIZA O VALOR DA VARIAVEL SALDO MAXIMO
        saldo_maximo = saldo_atual
    if saldo_atual < saldo_minimo: # SE O SALDO ATUAL FOR MENOR QUE O SALDO MINIMO, ATUALIZA O VALOR DA VARIAVEL SALDO MINIMO
        saldo_minimo = saldo_atual
        
def simular_emprestimo(): # FUNÇÃO PARA SIMULAR EMPRESTIMO
    global saldo_atual, saldo_maximo, saldo_minimo # VARIAVEIS GLOBAIS
    
    while True: # SE O VALOR INFORMADO FOR MAIOR QUE ZERO, DA PROSSEGUIMENTO, SE NÃO, EXIBE UMA MENSAGEM DE ERRO E SOLICITA NOVAMENTE
        try:
            valorEmprestado = float(input('\nInforme o valor a ser emprestado: '))
            if valorEmprestado > 0:
                break
            else:
                print('\nDigite um valor maior que 0\n')
        except ValueError:
            print('\nDIGITE UM NÚMERO') # ERRO INFORMADO CASO O VALOR INFORMADO NÃO SEJA UM NUMERO 
            
    while True: # SE O VALOR INFORMADO FOR MAIOR QUE ZERO, DA PROSSEGUIMENTO, SE NÃO, EXIBE UMA MENSAGEM DE ERRO E SOLICITA NOVAMENTE 
        try:    
            percJuros = float(input('Informe a porcentagem do juros: '))
            if percJuros > 0:
                break
            else:
                print('\nDigite um valor maior que 0\n')
        except ValueError:
            print('\nDIGITE UM NÚMERO\n')  # ERRO INFORMADO CASO O VALOR INFORMADO NÃO SEJA UM NUMERO
            
    while True: # SE O VALOR INFORMADO FOR MAIOR QUE ZERO, DA PROSSEGUIMENTO, SE NÃO, EXIBE UMA MENSAGEM DE ERRO E SOLICITA NOVAMENTE 
        try:
            quantiade_de_parcelas = int(input('Informe a quantidade de parcelas: '))
            if quantiade_de_parcelas > 0:
                break
            else:
                print('\nDigite um valor maior que 0\n')
        except ValueError:
            print('\nDIGITE UM NÚMERO\n') # ERRO INFORMADO CASO O VALOR INFORMADO NÃO SEJA UM NUMERO
    
    percJuros /= 100 # ATUALIZA A VARIAVEL percJuros EM UM VALOR DECIMAL
    montante_juros = valorEmprestado * percJuros # ATUALIZA A VARIAVEL montante_juros
    valor_total_maisJuros = montante_juros + valorEmprestado # ATUALIZA A VARIAVEL valor_total_maisJuros
    valor_parcela = valor_total_maisJuros / quantiade_de_parcelas # ATUALIZA A VARIAVEL valor_parcela
          
    print(f'\nCada parcela ficou em R${valor_parcela:.2f}') # IMPRIME NA TELA O VALOR DE CADA PARCELA  
    print(f'O valor a ser pago de juros ficou em R${montante_juros:.2f}') # IMPRIME NA TELA O VALOR EM REAIS DOS JUROS TOTAL
    print(f'O valor total mais juros ficou em R${valor_total_maisJuros:.2f}\n') # IMPRIME NA TELA O VALOR TOTAL DO EMPRESTIMO MAIS O VALOR TOTAL DOS JUROS
        
def extrato(): # FUNÇÃO PARA MOSTRAR O EXTRATO
    # PRINTA NA TELA AS INFORMAÇÕES MAIS RELEVANTES
    print(f'\nCliente: {nome_cliente}')
    print(f'Saldo inicial: R${saldo_inicial:.2f}')
    print(f'Saldo Atual: R${saldo_atual:.2f}')
    print(f'Quantidade de Depósitos: {quantidade_depositos}')
    print(f'Valor total dos Depósitos realizados: R${valor_total_depositos:.2f}')
    print(f'Quantidade de saques: {quantiade_saques}')
    print(f'Valor total dos Saques realizados: R${valor_total_saques:.2f}')
    print(f'Valor total dos juros recebidos: R${valor_total_jurosRecebidods:.2f}')
    print(f'Saldo Mínimo da conta: R${saldo_minimo:.2f}')
    print(f'Saldo Máximo da conta: R${saldo_maximo:.2f}\n')
    
def SAIR(): # FUNÇÃO PARA FINALIZAR O PROGRAMA
    print('\nAperte ENTER para SAIR...')
    input('') # AO APERTAR ENTER O PROGRAMA ENCERRA

def voltarMenu(): # VARIAVEL FEITA PARA TODA VEZ QUE FOR "FINALIZADO" UMA OPÇÃO DO MENU, O PROGRAMA NÃO VOLTA SOZINHO AO MENU, ASSIM PODENDO SER ENTENDIDO MELHOR OS PRINTS DE CADA OPÇÃO
    input('Digite ENTER para voltar ao MENU...\n')
    
limparTela() # HABILITA A FUNÇÃO limparTela
   
def Menu(): # FUNÇÃO QUE CONTEM O MENU
    
    while True: # ENQUANTO A OPÇÃO 8 NAO FOR SELECIONADA, O PROGRAMA NAO SE ENCERRA
        print('=====MENU=====\n')
        if not contaAberta: # ENQUANTO A VARIAVEL contaAberta FOR FALSE, IMPRIME SOMENTE ESSA OPÇÃO
            print('1: Abrir Conta')
        if contaAberta: # ENQUANTO A VARIAVEL contaAberta FOR TRUE, IMPRIME ESSAS OPÇÕES
            print('2: Realizar Depósito')
            print('3: Realizar Saque')
            print('4: Aplicar Juros')
            print('5: Simular Empréstimo')
            print('6: Extrato')
        print('0: SAIR') # IMPRIME ESSA OPÇÃO INDEPENDENTE DA VARIAVEL contaAberta
        
        opcao = input('\nEscolha uma opção: ') # VARIAVEL CRIADA PARA O USUARIO SELECIONAR A OPÇÃO DO MENU DESEJADA
        
        if opcao == '1' and not contaAberta:
            abrir_conta() # CHAMA A FUNÇÃO abrir_conta
            voltarMenu() # CHAMA A FUNÇÃO voltarMenu
            limparTela() # CHAMA A FUNÇÃO limparTela 
            
        elif opcao == '2' and contaAberta:
            realizar_deposito() # CHAMA A FUNÇÃO realizar_deposito
            voltarMenu() # CHAMA A FUNÇÃO voltarMenu
            limparTela() # CHAMA A FUNÇÃO limparTela 
            
        elif opcao == '3' and contaAberta:
            realizar_saque() # CHAMA A FUNÇÃO realizar_saque
            voltarMenu() # CHAMA A FUNÇÃO voltarMenu
            limparTela() # CHAMA A FUNÇÃO limparTela 
            
        elif opcao == '4' and contaAberta:
            aplicar_juros() # CHAMA A FUNÇÃO aplicar_juros
            voltarMenu() # CHAMA A FUNÇÃO voltarMenu
            limparTela() # CHAMA A FUNÇÃO limparTela 
            
        elif opcao == '5' and contaAberta:
            simular_emprestimo() # CHAMA A FUNÇÃO simular_emprestimo
            voltarMenu() # CHAMA A FUNÇÃO voltarMenu
            limparTela() # CHAMA A FUNÇÃO limparTela 
            
        elif opcao == '6' and contaAberta:
            extrato() # CHAMA A FUNÇÃO extrato
            voltarMenu() # CHAMA A FUNÇÃO voltarMenu
            limparTela() # CHAMA A FUNÇÃO limparTela 
            
        elif opcao == '0':
            SAIR() # CHAMA A FUNÇÃO SAIR
            print('Encerrando o Programa')
            break # ENCERRA O PROGRAMA
        
        else:
            print('\n!!!Opção Inválida!!!\n') # CASO NAO SEJA DIGITADO UM NUMERO CORRESPONDENTE A UMA OPÇÃO, PRINTA OPÇÃO INVALIDA E SOLICITA NOVAMENTE

Menu() # HABILITA A FUNÇÃO Menu