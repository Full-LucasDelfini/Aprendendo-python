exp = str(input('Digite uma expressão, por favor: '))
pilha = []
for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print(f'A expressão {exp}, em que foi digitada é válida!')
else:
    print(f'A expressão {exp}, no qual foi digitada é inválida!')