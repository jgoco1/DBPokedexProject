from Entity.DatabaseConnection import DatabaseConnection
from Entity.pokedex import pokedex

def menu():
    """
    Displays the menu options for the Pokedex application.
    """
    print("\n Pokedex for Gen 1")
    print("1. Add a type")
    print("2. Add an ability")
    print("3. Add a region")
    print("4. Add a settlement")
    print("5. Add a Pokemon \n")

    print("6. Update a type")
    print("7. Update an ability")
    print("8. Update a region")
    print("9. Update a settlement \n")

    print("a. Display pokemon")
    print("b. Display types")
    print("c. Display abilities")
    print("d. Display regions")
    print("e. Display settlements")
    print("Or type 'Quit' to quit")

def addPokemon(pd):
    """
    Adds a new Pokemon to the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    pokemon_name = input("Enter the Pokemon name: ")
    types = pd.getTypes()
    for type in types:
        print("ID: ", type.getID(), " | Name: ", type.getName())
    pokemon_type = input("Select the Pokemon type: ")
    
    abilities = pd.getAbilities()
    for ability in abilities:
        print("ID: ", ability.getID(), " | Name: ", ability.getName(), " | Cost: ", ability.getCost(), " | Damage: ", ability.getDamage())
    pokemon_ability = input("Enter the Pokemon ability: ")


    regions = pd.getRegions()
    for region in regions:
        print("ID: ", region.getID(), " | Name: ", region.getName())
    pokemon_region = input("Enter the Pokemon region: ")
    
    pd.add_pokemon(pokemon_name, pokemon_type, pokemon_ability, pokemon_region)

def updateType(pd):
    """
    Updates a type in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    types = pd.getTypes()
    for type in types:
        print("ID: ", type.getID(), "| Name: ", type.getName())
    userInput = input("Which type would you like to update? ")
    newName = input("What would you like the updated name to be? ")
    for type in types:
        if type.getID() == userInput:
            type.setName(newName)

def updateAbility(pd):
    """
    Updates an ability in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    abilities = pd.getAbilities()
    for ability in abilities:
        print("ID: ", ability.getID(), "| Name: ", ability.getName(), "| Cost: ", ability.getCost(), "| Damage: ", ability.getDamage())
    userInput = input("Which ability would you like to update? ")
    newName = input("What would you like the updated name to be? ")
    newCost = input("What would you like the updated cost to be? ")
    newDamage = input("What would you like the updated damage to be? ")
    for ability in abilities:
        if ability.getID() == userInput:
            ability.setName(newName)
            ability.setCost(newCost)
            ability.setDamage(newDamage)

def updateRegion(pd):
    """
    Updates a region in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    regions = pd.getRegions()
    for region in regions:
        print("ID: ", region.getID(), "| Name: ", region.getName())
    userInput = input("Which region would you like to update? ")
    newName = input("What would you like the updated name to be? ")
    for region in regions:
        if region.getID() == userInput:
            region.setName(newName)

def updateSettlement(pd):
    """
    Updates a settlement in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    settlements = pd.getSettlements()
    for settlement in settlements:
        print("ID: ", settlement.getID(), "| Name: ", settlement.getName())
    userInput = input("Which settlement would you like to update? ")
    newName = input("What would you like the updated name to be? ")
    for settlement in settlements:
        if settlement.getID() == userInput:
            settlement.setName(newName)

def displayPokemon(pd):
    """
    Displays all Pokemon in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    pokemon = pd.getPokemon()
    for p in pokemon:
        print("ID: ", p.getID(), "| Name: ", p.getName(), "| Type: ", p.getType(), "| Ability: ", p.getAbility(), "| Region: ", p.getRegion())

def displayTypes(pd):
    """
    Displays all types in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    types = pd.getTypes()
    for type in types:
        print("ID: ", type.getID(), "| Name: ", type.getName())

def displayAbilities(pd):
    """
    Displays all abilities in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    abilities = pd.getAbilities()
    for ability in abilities:
        print("ID: ", ability.getID(), "| Name: ", ability.getName(), "| Cost: ", ability.getCost(), "| Damage: ", ability.getDamage())
    
def displayRegions(pd):
    """
    Displays all regions in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    regions = pd.getRegions()
    for region in regions:
        print("ID: ", region.getID(), "| Name: ", region.getName())

def displaySettlements(pd):
    """
    Displays all settlements in the Pokedex.

    Parameters:
    pd (pokemon): The Pokedex object.

    Returns:
    None
    """
    settlements = pd.getSettlements()
    for settlement in settlements:
        print("ID: ", settlement.getID(), "| Name: ", settlement.getName())



def main():
    """
    The main function that runs the Pokedex application.

    Parameters:
    None

    Returns:
    None
    """
    userInput = 0
    dbcon = DatabaseConnection()
    pd = pokedex(dbcon)
    while(userInput.lower() != "quit"):
        menu()
        userInput = input("Enter your choice: ")
        if userInput == "1":
            type_name = input("Enter the type name: ")
            pd.add_type(type_name)
        elif userInput == "2":
            ability_name = input("Enter the ability name: ")
            pd.add_ability(ability_name)
        elif userInput == "3":
            region_name = input("Enter the region name: ")
            pd.add_region(region_name)
        elif userInput == "4":
            settlement_name = input("Enter the settlement name: ")
            pd.add_settlement(settlement_name)
        elif userInput == "5":
            addPokemon(pd)
        elif userInput == "6":
            updateType(pd)
        elif userInput == "7":
            updateAbility(pd)
        elif userInput == "8":
            updateRegion(pd)
        elif userInput == "9":
            updateSettlement(pd)
        elif userInput == "a":
            displayPokemon(pd)
        elif userInput == "b":
            displayTypes(pd)
        elif userInput == "c":
            displayAbilities(pd)
        elif userInput == "d":
            displayRegions(pd)
        elif userInput == "e":
            displaySettlements(pd)
    dbcon.close()

main()