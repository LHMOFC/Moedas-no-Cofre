print('Calcule seu cofrinho aqui! ')
from time import sleep
# Quantidade de cada moeda:
m1real = int(input('Quantas moedas de R$1,00: '))
m50cent = int(input('Quantas moedas de R$0,50: '))
m25cent = int(input('Quantas moedas de R$0,25: '))
m10cent = int(input('Quantas moedas de R$0,10: '))
m5cent = int(input('Quantas moedas de R$0,05: '))
totalm = m1real + m50cent + m25cent + m10cent + m5cent
# Calculando total:
total = (m1real * 1) + (m50cent * 0.5) + (m25cent * 0.25) + (m10cent * 0.10) + (m5cent * 0.05)
# Calculando total de cada moeda:
f1real = (m1real * 1)
f50cent = (m50cent * 0.5)
f25cent = (m25cent * 0.25)
f10cent = (m10cent * 0.10)
f5cent = (m5cent * 0.05)
# Resultados finais:
print('\033[1;34mCalculando...\033[m')
sleep(2.5)
print('''Com \033[33m{} moedas\033[m de \033[1;30mR$1\033[m & \033[33m{}\033[m de \033[1;30mR$0.5\033[m & \033[33m{}\033[m de
 \033[1;30mR$0.25\033[m & \033[33m{}\033[m de \033[1;30mR$0.10\033[m & \033[33m{}\033[m de \033[1;30mR$0.05\033[m.'''
      .format(m1real, m50cent, m25cent, m10cent, m5cent, ))
print('total')
print('\033[1;34mRendimento de cada moeda...\033[m')
sleep(3.5)
print('''Moedas de \033[33mR$1\033[m (\033[1;30m{}x\033[m) geraram \033[33mR${:.2f}\033[m
Moedas de \033[33mR$0.5\033[m (\033[1;30m{}x\033[m) geraram \033[33mR${:.2f}\033[m
Moedas de \033[33mR$0.25\033[m (\033[1;30m{}x\033[m) geraram \033[33mR${:.2f}\033[m
Moedas de \033[33mR$0.1\033[m (\033[1;30m{}x\033[m) geraram \033[33mR${:.2f}\033[m
Moedas de \033[33mR$0.05\033[m (\033[1;30m{}x\033[m) geraram \033[33mR${:.2f}\033[m
Com um total de \033[1;30m{} moedas!\033[m'''
      .format(m1real, f1real, m50cent, f50cent, m25cent, f25cent, m10cent, f10cent, m5cent, f5cent, totalm))
