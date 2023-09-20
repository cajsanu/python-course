# Write your solution here



def recipelist(filename: str):
    with open(filename) as recepies:
        list_of_recipes = []
        recipe = []
        for line in recepies:
            line = line.strip()
            recipe.append(line)
            if line == "":
                list_of_recipes.append(recipe)
                recipe = []
                continue
        if len(recipe) > 0:
            list_of_recipes.append(recipe)
    return list_of_recipes

def search_by_name(filename: str, word: str):
    list_of_names = []
    list_of_recipes = recipelist(filename)
    for item in list_of_recipes:
        if word.lower() in item[0].lower():
            list_of_names.append(item[0])
    return list_of_names
            

def search_by_time(filename: str, prep_time: int):
    list_of_recipes = recipelist(filename)
    list_of_names = []
    for item in list_of_recipes:
        time = int(item[1])
        if time <= prep_time:
            list_of_names.append(f"{item[0]}, preparation time {item[1]} min")
    return list_of_names

def search_by_ingredient(filename: str, ingredient: str):
    list_of_names = []
    list_of_recipes = recipelist(filename)
    for item in list_of_recipes:
        if ingredient.lower() in item:
            list_of_names.append(f"{item[0]}, preparation time {item[1]} min")
    return list_of_names



if __name__ == "__main__":
    search_by_name("recipes1.txt", "Cake")
    search_by_time("recipes1.txt", 60)
    search_by_ingredient("recipes1.txt", "eggs")