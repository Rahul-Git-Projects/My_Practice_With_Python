from pathlib import Path
import os

username = input("Please enter you name here:  ")
print(f"Welcome {username}!")
print("Recipies are in C:\\My_Coding_Projects\\My_Practice_With_Python\\basic_games_and_applications_(simple_projects)\\recipe_book\\recipes")

def read_recipe():
    main_path = Path("C:\\My_Coding_Projects\My_Practice_With_Python\\basic_games_and_applications_(simple_projects)\\recipe_book\\recipes")
    categories_set = set([])
    for paths in main_path.glob("**/*.txt"):
       categories_set.add(paths.parent.name)
    categories = list(categories_set)
    for index,category in enumerate(categories):
        print(f"{index + 1}: {category}")
    choose_category = input("Choose a category:")
    while choose_category not in categories:
        choose_category = input("Sorry,Please choose a category that actually exists in the folder")
    for paths in main_path.glob("**"):
        if paths.name == choose_category:
            pass


