from includes.database import *
from includes.functions import *

print(desc["Q1"])
nom=input("Nom de l'etudiant :")
print(f"Date d'inscription à la bibliotheque de l'etudiant {nom} est {insBU(nom)}")


print(''.join("--" for _ in range(15)))
print(desc["Q2"])
num=int(input("Num de cours :"))
for etudiant in insCour(num):
    print(etudiant)


print(''.join("--" for _ in range(15)))
print(desc["Q3"])
num=int(input("Num de l'etudiant :"))
for resultat in resuEtu(num):
    print(resultat)


print(''.join("--" for _ in range(15)))
print(desc["Q4"])
for etudiant in resultEchec():
    print(etudiant)


print(''.join("--" for _ in range(15)))
print(desc["Q5"])
for etudiant in insr():
    print(etudiant)


print(''.join("--" for _ in range(15)))
print(desc["Q6"])
num=int(input("Num du livre :"))
for pret in empLiv(num):
    print(pret)


print(''.join("--" for _ in range(15)))
print(desc["Q7"])
for etudiant in retard():
    print(etudiant)


print(''.join("--" for _ in range(15)))
print(desc["Q8"])
for livre in noEmp():
    print(livre)


print(''.join("--" for _ in range(15)))
print(desc["Q9"])
for classe in resultTot():
    print(classe)

"""
print(''.join("--" for _ in range(15)))
print(desc["Q10"])
num_cours, nomC= input("num_cours et nomC : ").split()
modifierNomCours(num_cours, int(nomC))


print(''.join("--" for _ in range(15)))
print(desc["Q11"])
num_cours=int(input("num_cours : "))
supprimerCours(num_cours)
"""

print(''.join("--" for _ in range(15)))
print(desc["Q12"])
plotting_pie()


print(''.join("--" for _ in range(15)))
print(desc["Q13"])
plotting_hist()