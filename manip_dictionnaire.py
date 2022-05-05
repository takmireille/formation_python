# mainipuler les données du dictionnaire

employes = {

	"id01":{"prenom":"paul","nom":"Dupont","age": 32},
	"id02":{"prenom":"patrick","nom":"Fernand","age":36},
	"id03":{"prenom":"Julie", "nom": "Dupuit", "age":25},
	
	}


print("1- nous avons le dictionnaire suivant")
print(employes)
print("2- patrick quitte l'entreprise")
del employes["id02"]
print(employes)
print("3-julie à un an de plus")
employes["id03"]["age"]=26
print(employes)
age_paul = employes["id01"]["age"]
print("quel est l'age de paul")
print(age_paul)
