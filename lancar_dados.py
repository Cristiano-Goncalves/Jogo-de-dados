import random

print("""
=======================
==== Jogo de dados ====
=======================""")

dado1=random.randint(1,6)
dado2=random.randint(1,6)

soma=dado1+dado2

print(f"""
       Dado 1: {dado1} """)

print(f"""
       Dado 2: {dado2} """)

if dado1==dado2:
    print("""
=======================
        Empate
=======================""")
elif dado1>dado2:
    print("""
========================
🏆 Vencedor 🏆 - Dado 1
========================""")

else:
    print("""
========================
🏆 Vencedor 🏆 - Dado 2
========================""")

    
print(f"""      
===| A soma dos dados é: {soma} |===\n""")
