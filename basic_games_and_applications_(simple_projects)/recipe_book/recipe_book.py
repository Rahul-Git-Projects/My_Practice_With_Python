from pathlib import Path
import os

main_path = Path("C:\\My_Coding_Projects\\My_Practice_With_Python\\basic_games_and_applications_(simple_projects)\\recipe_book\\recipes")

def choosing_category():
    categories_set = set()
    for paths in main_path.glob("**/*.txt"):
        categories_set.add(paths.parent.name)
    categories = list(categories_set)
    for index, category_c in enumerate(categories):
        print(f"{index + 1}: {category_c}")
    choose_category = input("Choose a category(Type its name not its number): ")
    while choose_category not in categories:
        choose_category = input("Sorry,Please choose a category that actually exists in the folder")
    return choose_category

def read_recipe():
    category = choosing_category()
    recipe_set = set()
    for paths in main_path.glob(f"{category}/*.txt"):
        recipe = paths.stem
        recipe_set.add(recipe)
    recipies = list(recipe_set)
    for index, dish in enumerate(recipies):
        print(f"{index + 1}: {dish}")
    choose_recipe = input("Choose a recipe(Type its name not its number): ")
    while choose_recipe not in recipies:
        choose_recipe = input("Sorry,Please choose a recipe that actually exists in the category:  ")

    content = Path(main_path,category,f"{choose_recipe}.txt").read_text()
    os.system("cls")
    print(content)
    reply = input("if done reading,press enter")

def create_recipe():
    category = choosing_category()
    new_recipe_name = input("Type the name of the recipe you want to add: ")
    new_recipe_content = input("Type the content of your recipe: ")
    new_recipe = open(Path(main_path,category,f"{new_recipe_name}.txt"),"w")
    new_recipe.write(new_recipe_content)
    new_recipe.close()
    os.system("cls")

def create_category():
    category_name = input("Type the name of the category you want to add: ")
    os.mkdir(Path(main_path,category_name))
    placeholder_file = open(Path(main_path,category_name,"placeholder.txt"),"w")
    os.system("cls")
    print(f"directory {category_name} has been successfully created")

def delete_recipe():
    category = choosing_category()
    recipe_set = set()
    for paths in main_path.glob(f"{category}/*.txt"):
        recipe = paths.stem
        recipe_set.add(recipe)
    recipies = list(recipe_set)
    for index, dish in enumerate(recipies):
        print(f"{index + 1}: {dish}")
    choose_recipe = input("Choose a recipe: ")
    while choose_recipe not in recipies:
        choose_recipe = input("Sorry,Please choose a recipe that actually exists in the category(Type its name not its number):  ")

    Path(main_path,category,f"{choose_recipe}.txt").unlink()
    os.system("cls")
    print(f"The recipe {choose_recipe} has been successfully deleted")

def delete_category():
    category = choosing_category()
    for paths in main_path.glob(f"{category}/*.txt"):
        paths.unlink()
    os.rmdir(str(Path(main_path,category)))
    os.system("cls")
    print(f"category {category} has been successfully removed")

def counting_categories():
    categories_set = set()
    for paths in main_path.glob("**/*.txt"):
        categories_set.add(paths.parent.name)
    categories = list(categories_set)
    count = len(categories)
    return count

username = input("Please enter your name here:  ")
print(f"Welcome {username}!")
end_program = False

while not end_program:

    print("Recipies are in C:\\My_Coding_Projects\\My_Practice_With_Python\\basic_games_and_applications_(simple_projects)\\recipe_book\\recipes")
    print(f"There are {counting_categories()} categories to choose from")
    print("""
    1 --> Read recipe
    2 --> create recipe
    3 --> create category
    4 --> delete recipe
    5 --> delete category
    6 --> end the program""")


    user_reply = input("Which action would you like to perform?\nif you are done with your work,choose the sixth option \"end program\":   ")
    os.system("cls")
    while user_reply not in ["1","2","3","4","5","6"]:
        user_reply = input("Please type the number corresponding to the action to perform i.e (1 to 6):  ")
    match user_reply:
        case "1":
            read_recipe()
        case "2":
            create_recipe()
        case "3":
            create_category()
        case "4":
            delete_recipe()
        case "5":
            delete_category()
        case "6":
            end_program = True
    os.system("cls")








