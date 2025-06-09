def suma_digitos_potencia(numero, exponente):
    resultado = numero ** exponente
    suma = sum(int(digito) for digito in str(resultado))
    return resultado, suma