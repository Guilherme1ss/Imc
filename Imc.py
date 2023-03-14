while True:
    peso = input ('Digite o seu peso em kg: ')
    peso = peso.replace(",", ".")
    if peso.replace(".", "", 1).isdigit():
        try:
            peso = float(peso)
            break
        except ValueError:
            print ("Valor inválido. Digite apenas números.")
    else:
        print ("Valor inválido. Digite apenas números.")

while True:
    altura = input ('Digite a sua altura em metros: ')
    altura = altura.replace(",", ".")
    if altura.replace(".", "", 1).isdigit():
        try:
            altura = float(altura)
            break
        except ValueError:
            print ("Valor inválido. Digite apenas números.")
    else:
        print ("Valor inválido. Digite apenas números.")

imc = peso/altura ** 2 

if imc <= 18.5:
    nivelImc = ("abaixo do peso.")
elif imc > 18.5 and imc <= 24.9:
    nivelImc = ("normal.")
elif imc > 24.9 and imc <= 29.9:
    nivelImc = ("sobrepeso.")
elif imc > 29.9 and imc <= 34.9:
    nivelImc = ("obesidade grau 1.")
elif imc > 34.9 and imc <= 39.9:
    nivelImc = ("obesidade grau 2.")
elif imc >= 40:
    nivelImc = ("obesidade mórbida.")

print ("Seu IMC é", "{:.1f}".format(imc) + ',', "isso é considerado", nivelImc)