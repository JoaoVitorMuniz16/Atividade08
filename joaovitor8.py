valor = float(input("digite o valor em reais"))
desconto = float(input("Digite a '%' de desconto"))

desconto = (valor * desconto) / 100
resultado = valor-desconto
print(f"""
        Valor de Desconto: {desconto}
        Valor Final: {resultado} 
""")