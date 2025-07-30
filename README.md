# Sistema-Bancario.py

Sistema Bancário Simplificado

O programa consiste na estruturação do Backend de um sistema bancário simplificado para gerenciamento de uma conta de um único cliente desenvolvido em Python.

O programa possui um Menu com as seguintes opções:

- Abrir Conta: Inicializa a conta de um cliente, solicitando seu nome e saldo inicial. Após criada, esta opção é desabilitada e as opções a seguinte são habilitadas ao Menu;
- Realizar Depósito: Solicita ao usuário o valor a ser depositado;
- Realizar Saque: Solicita ao usuário o valor a ser sacado, imitando a função de um caixa eletronico, o valor liberado será apenas o deduzido das notas disponiveis, priorizando sempre notas mais altas, caso aja um valor impossivel como moedas, o programa informa que nao foi possivel sacar tal valor excedente e informa o valor que foi liberado, sempre priorizando notas maiores;
- Aplicar Juros: Solicita ao usuário que informe uma taxa de juros percentual, calcula o juros e atualiza o montante do usuário;
- Simular Empréstimo: Solicita o valor a ser emprestado, a taxa de juros mensal percentual e a quantidade de parcelas para pagamento. Em seguida mostra na tela o valor de cada parcela, a quantidade total de juros a ser pago e o somatório dos valores de todas as parcelas. Utilizando juros simples;
- Extrato: Mostra na tela uma relatório com as seguintes informações:
            - Nome do Cliente;
            - Saldo Inicial;
            - Saldo Atual;
            - Quantidade de Depósitos Realizados;
            - Valor Total dos Depósitos Realizados;
            - Quantidade de Saques Realizados;
            - Valor Total dos Saques Realizados;
            - Valor Total dos Juros Recebidos;
            - Saldos Mínimos e Máximos da Conta.
- Sair: Encerra o programa.
