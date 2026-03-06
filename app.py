from flask import Flask, render_template, request, jsonify

# 1. Inicializa o aplicativo Flask
app = Flask(__name__)

# 2. Cria a rota principal (a página inicial)
@app.route('/')
def index():
    # Isso diz para o Flask ir lá na pasta 'templates' e mostrar o seu HTML na tela
    return render_template('index.html')




@app.route('/calcular', methods=['POST'])
def calcular():
    
    # Inserir dados -------
    dados = request.get_json()
    cpf = dados.get('cpf')
    
    steps = []
    
    contador = 10
    soma_total_cpf = 0
    multi_soma_1 = 0
    divi_multi_1 = 0
    digito_1 = None
    
    # primeiro digito do cpf   
    # for multiplicando cada item ------
    for i in cpf:
        soma = int(i) * contador
        soma_total_cpf += soma
        steps.append(f'multiplicando {i} x {contador} = {soma}')
        contador -= 1

    steps.append(f'soma total = {soma_total_cpf}')        
    
    steps.append(f'iremos multiplicar {soma_total_cpf} por 10...')
    multi_soma_1 = soma_total_cpf * 10
    steps.append(f'resultado: {multi_soma_1}')
    
    steps.append(f'vamos dividir {multi_soma_1} por 11...')
    divi_multi_1 = multi_soma_1 % 11
    steps.append(f'resultado: {divi_multi_1}')
    
    if divi_multi_1 > 9:
        divi_multi_1 = 0
        steps.append('seu cpf é invalido ❌ ')
        return jsonify({'steps': steps})
    else:
        digito_1 = divi_multi_1
        steps.append(f'{digito_1}, ok...')
        cpf_total = cpf + str(digito_1)
        
    # segundo digito do cpf    
    steps.append(f'seu cpf esta {cpf_total}* esta faltando 1 digito vamos la...')

    contador = 11
    soma_total_cpf_2 = 0

    for numero in cpf_total:
        resultado = int(numero) * contador
        steps.append(f'multicando {numero} x {contador} = {resultado}')
        soma_total_cpf_2 += resultado
        contador -= 1

    steps.append(f'somando...')
    steps.append(f'resultado: {soma_total_cpf_2}')

    resultado1 = soma_total_cpf_2 * 10
    resultado1 = resultado1 % 11

    steps.append(f'multiplicando {soma_total_cpf_2} x 10 e dividindo por 11...')
    steps.append(f'resultado: {resultado1}')

    if resultado1 > 9:
        resultado1 = 0
        steps.append('seu cpf é invalido ❌ ')
        return jsonify({'steps': steps})
    else:
        resultado1 = resultado1


    steps.append(f'o segundo digito é {resultado1}')
    cpf_final = cpf_total + str(resultado1)
    steps.append(f'seu cpf é {cpf_final}, seja bem vindo!')   

    return jsonify({'steps': steps})
    


    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
