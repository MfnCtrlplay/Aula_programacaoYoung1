#Dicionario na Pratica

pokemon = {

    "poke1": "chamander",

    "poke2": "pikachu"

}

# flexibilidade do Dicionario

pokemon2 = {

    "poke3": "bulbasaur",
    "age": 10,
    "jogavel": True,
"abilities": ["folha navalha", "cipó", "recuperacão"],
    "status":{

                "dano": 15,
                "health": 100,
                "defense":40.5
    }
}

print("pokemon:",pokemon2["poke3"])
print("idade: ",pokemon2["age"])
print("Habilidade: ",pokemon2["abilities"])