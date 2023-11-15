
import time
from datetime import date
ano = date.today().year

nome = str(input('Digite seu nome:'))
nasci = int(input('digite seu ano de nascimento:'))
idade = ano - nasci
ctps = int(input('Carteira de Trabalho(Clique no 0 se não tem):'))
d = {"nome":nome,"idade":idade,"ctps":ctps}

if ctps > 0:
    contra = int(input('Ano de Contratação:'))
    salario = int(input('Sálario:R$ '))
    contri = str(input('É contribuinte com o INSS?[S/N]')).lower()
    while contri =='n':
        break
    d = {"nome":nome,"idade":idade,"ctps":ctps}
    if contri == 's':
        tempo = float(input('Ha quanto tempo você contríbui?[anos/meses]'))
        d['tempo'] = tempo   
        d['contra'] = contra
        d['salario'] = salario 
        idadet = contra - nasci
        aposentadoria= idadet + 35
        contribuição = (35 - tempo) * 12
        d = {"nome":nome,"idade":idade,"ctps":ctps}
   
        d['aposentadoria'] = aposentadoria
        d['contribuição' ] = contribuição
        print('--='*15)
        if contribuição <=0:
    
            print(f'{nome.upper()}, você já pode se APOSENTAR')
print('--='*15)
    
for n,i in d.items():
    print
    print(f'-{n}  tem o valor de {i}')
