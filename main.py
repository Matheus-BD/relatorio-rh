import csv

funcionarios_antigos = []

def calcular_media(funcionarios):
    salarios = 0
    for funcionario in funcionarios:
        salarios += float(funcionario[2])

    return salarios / len(funcionarios)

with open("funcionarios.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    next(leitor)
    for linha in leitor:
        if int(linha[3]) >= 3:
            funcionarios_antigos.append(linha)

media_salaria = calcular_media(funcionarios_antigos)
print(f"R$ {media_salaria:.2f}".replace(".", ","))

with open("relatorio.csv", "w", encoding="utf-8", newline="") as f:
    funcionarios = []
    funcionarios.append(["nome", "departamento", "salario", "anos_empresa", "faixa_salarial"])

    csv_writer = csv.writer(f)

    # print(funcionarios_antigos)

    for funcionario in funcionarios_antigos:
        salario = float(funcionario[-1])
        if salario > media_salaria:
            funcionario.append("Acima da média")
        elif salario < media_salaria:
            funcionario.append("Abaixo da média")
        else:
            funcionario.append("Salario na média...")
        funcionarios.append(funcionario)

    csv_writer.writerows(funcionarios)