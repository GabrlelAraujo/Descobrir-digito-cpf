import time




        
cpf = input('digite os 9 primeiros digitos do seu cpf: ')

soma_total_cpf = 0

multi_soma_total = 0

divi_multi_total = 0

primeiro_digito = None


for i in cpf:
    soma = int(i) * 10
    soma_total_cpf += soma
    print(f'multiplicando por 10 x {i} = {soma}')
    time.sleep(0.5)

print(f'somando os resultados....')
time.sleep(1)
print(f'a soma resultou em: {soma_total_cpf}')
time.sleep(1)

print(f'agora vamos multiplcar sua soma ({soma_total_cpf}), por 10....')
multi_soma_total = soma_total_cpf * 10
time.sleep(1)
print(f'a multiplicação resultou em: {multi_soma_total}')
time.sleep(1)

print(f'agora vamos divitir {multi_soma_total} por 11...')
time.sleep(1)
divi_multi_total = multi_soma_total % 11
print(f'o resultado deu: {divi_multi_total}')

if divi_multi_total > 9:
    divi_multi_total = 0
    print('cpf invalido')
else:
    primeiro_digito = divi_multi_total
    print('cpf valido brow')
    cpf_completo = cpf + str(primeiro_digito)



time.sleep(1)
print('agora vamos decobrir o segundo digito do cpf...')
time.sleep(1)

contador = 11
soma_total_cpf2 = 0


for numero in cpf_completo:
    resultado = int(numero) * contador
    print(f'multiplicando {numero} x {contador} = {resultado}')
    soma_total_cpf2 += resultado
    contador -= 1
    time.sleep(0.5)
    

print(f'somando todos os resultado...')
time.sleep(0.5)
print(f'a soma resultou em: {soma_total_cpf2}')
time.sleep(0.5)

resultado1 = (soma_total_cpf2 * 10)
resultado1 = resultado1 % 11

print(f'agora iremos multiplicar {soma_total_cpf2} x 10 e / 11 = {resultado1}')
time.sleep(0.5)
if resultado1 > 9: 
        resultado1 = 0
else:
        resultado1 = resultado1
        

time.sleep(0.5)
print(f'o regundo digito faltante do seu cpf eh: {resultado1}')
time.sleep(0.5)
cpf_final = cpf + str(primeiro_digito) + str(resultado1)
print(f'seu cpf eh {cpf_final}')


