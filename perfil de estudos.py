
# Projeto: Meu perfil de IA

print("===== PERFIL DE ESTUDOS =====")

nome = input("Nome: ")
idade = int(input("Idade: "))
objetivo = input("Objetivo: ")
horas = float(input("Horas por dia: ").replace(",", "."))

# Cálculos
idade_futura = idade + 5
total_horas = horas * 90

# Resultado
print("\n===== RESULTADO =====")
print(f"Estudante: {nome}")
print(f"Objetivo: {objetivo}")
print(f"Idade daqui a 5 anos: {idade_futura}")
print(f"Horas de estudo previstas: {total_horas:.1f}")
    