from datetime import date, datetime
import locale

# per a mostrar les dates en català
locale.setlocale(locale.LC_ALL, 'ca_ES.UTF-8')

# Demanar les dades d'una persona
nom = input("Introdueix el teu nom: ")
cognoms = input("Introdueix els teus cognoms: ")
data_naixement_text = input("Introdueix la teva data de naixement (dd/mm/aaaa): ") 
data_naixement = datetime.strptime(data_naixement_text, '%d/%m/%Y').date() # data en format 'date'

# calculo l'edat
data_actual = date.today()
edat = data_actual.year - data_naixement.year - 1 # -1 pq potser no ha estat encara el seu aniversari
assert edat >= 0, "La data de naixement introduïda és incorrecta"

# ara, depenent del dia, sumo un any
aniversari_enguany = date(data_actual.year, data_naixement.month, data_naixement.day)
if aniversari_enguany <= data_actual:
    # ja ha estat el seu aniversari, té 1 any mes
    edat = edat + 1

# Imprimir les dades de la persona
print(f"Nom complet: {nom} {cognoms}")
print(f"Data de naixement: {data_naixement.strftime('%-d de %B de %Y')}")
print(f"Edat: {edat}")
