def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Calcula e verifica primeiro dígito verificador
    soma = sum(int(a) * b for a, b in zip(cpf[:9], range(10, 1, -1)))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Calcula e verifica segundo dígito verificador
    soma = sum(int(a) * b for a, b in zip(cpf[:10], range(11, 1, -1)))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True

# Teste
cpf = '08347531978'
print(valida_cpf(cpf))  # Deve imprimir: True ou False