#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#a.	quanto pagou ao INSS.
#b.	quanto pagou ao sindicato.
#c.	o salário líquido.
#d.	calcule os descontos e o salário líquido, conforme a tabela abaixo:
#e.	+ Salário Bruto : R$
#f.	- IR (11%) : R$
#g.	- INSS (8%) : R$
#h.	- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
valor_hora=float(input("Qual o valor de sua hora de trabalho? \n")) #Entrada do valor da hora-trabalho em 'float' por poder conter casas decimais
qtd_hora=int(input("Qual a quantidade de horas realizadas no mês? \n")) #Entrada da quantidade de horas em 'float' por poder conter casas decimais
salario_bruto=valor_hora * qtd_hora #fórmula do cálculo multiplicando a quantidade de VALOR HORA RABALHO X QUANTIDADE DE HORAS
inss=salario_bruto*0.08
irpf=salario_bruto*0.11
sindicato=salario_bruto*0.05
descontos=inss + irpf + sindicato
salario_liquido= (salario_bruto - descontos)
print ("+ Salário Bruto : .... R$ \t", "%.2f" % salario_bruto) # comando "\t" é para tabulação; equivale ao "tab"
print ("- IR (11%) : ......... R$ \t", "%.2f" % irpf)
print ("- INSS (8%) : ........ R$ \t", "%.2f" %  inss)
print ("- Sindicato (5%) : .. R$ \t", "%.2f" %  sindicato)
print ("= Salário Liquido : .. R$ \t", "%.2f" % salario_liquido)
#Esse exercício será refeito futuramente utilizando estruturas de repetição e condições de parada.