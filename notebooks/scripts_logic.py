import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


''' EDA SCRIPTS '''
def show_tags(data):
    tags = []
    for i in data.tags:
        if i:
            for j in i:
                tags.append(j)
    print(tags)


def analyze_IBA(data):
    # official IBA
    with open("../data/official_IBA.txt", "r", encoding="utf-8") as file:
        official_IBA = file.read().splitlines()

    i = 0
    # verify official IBA
    for _, row in data.iterrows():
        if type(row["tags"]) == list:
            if row["tags"].count("IBA") > 0:
                if row["name"] not in official_IBA:
                    print("Drinks that has been removed from IBA:", row["name"])
            elif row["name"] in official_IBA:
                print(row["name"], row["tags"])
                

    print("Anomalies: ", i)


def generate_hist_and_pie(data, column):
    plt.figure(figsize=(10, 5))
    data[column].value_counts().plot(kind='bar')
    plt.title(f'Hist of - {column}')
    plt.xlabel(column)
    plt.ylabel('Num of drinks')
    plt.show()

    plt.figure(figsize=(8, 8))
    category_counts = data[column].dropna().value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
    plt.title(f'Pie Chart - {column}')
    plt.ylabel('')
    plt.show()

    print(data[column].value_counts())

def list_to_hist_and_pie(data, column):
    ingredients = []
    if column == "ingredients":
        for i in data.ingredients:
            if i:
                for j in i:
                    ingredients.append(j['name'])
    else:
        for i in data.tags:
            if i:
                for j in i:
                    ingredients.append(j)
                    
    ingredients = pd.Series(ingredients)
    plt.figure(figsize=(18, 8))
    ingredients.value_counts().plot(kind='bar')
    plt.show()
    print(ingredients.value_counts())

    plt.figure(figsize=(18, 8))
    ingredients.value_counts().plot(kind='pie')
    plt.show()

def tags_contain_IBA(data):
    IBA = 0
    tags = 0
    for i in data.tags:
        if i:
            tags += 1
            if "IBA" in i:
                IBA += 1
    print(f"Drinks with tags: {tags}")
    print(f"Drinks with IBA tag: {IBA}")
    print(f"Drinks with tags but without IBA: {tags - IBA}")
    # pie chart
    plt.figure(figsize=(8, 8))
    plt.pie([IBA, tags - IBA], labels=["IBA", "Tags"], autopct='%1.1f%%')
    plt.title('Pie Chart of drinks with tags but without IBA')
    plt.show()

def analyze_instructions(data):
    # histogram of the column - word length in "instructions"
    instructions = []
    for i in data.instructions:
        if i:
            instructions.append(len(i.split()))
    instructions = pd.Series(instructions)

    instructions_counts = instructions.value_counts().sort_index()

    plt.figure(figsize=(18, 8))
    instructions_counts.plot(kind='bar')
    plt.title('Histogram word length in "instructions"')
    plt.xlabel('Word length')
    plt.ylabel('Frequency')
    plt.show()

    bins = range(0, instructions.max() + 5, 5)
    binned_instructions = pd.cut(instructions, bins=bins, right=False)

    instructions_counts = binned_instructions.value_counts().sort_index()

    plt.figure(figsize=(15, 8))
    instructions_counts.plot(kind='bar')
    plt.title('Histogram word length in "instructions" - bins = 5')
    plt.xlabel('Word length intervals')
    plt.ylabel('Frequency')
    plt.show()

    print(instructions_counts)

    plt.figure(figsize=(18, 8))
    instructions_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Pie chart of word lengths in instructions')
    plt.ylabel('')  
    plt.show()


def drinks_with_ingredient_in_name(data):
    ingredients = []
    for i in data.ingredients:
        if i:
            for j in i:
                ingredients.append(j['name'].lower())
    ingredients = set(ingredients)

    ingredients_in_name = 0
    for i in data.name:
        if i:
            for j in ingredients:
                if j in i.lower():
                    ingredients_in_name += 1
                    break
    print(f"Drinks whose ingredients are in the name: {ingredients_in_name}")
    print(f"Drinks whose ingredients are NOT in the name: {len(data) - ingredients_in_name}")

    plt.figure(figsize=(8, 8))
    plt.pie([ingredients_in_name, len(data) - ingredients_in_name], labels=["Ingredient in name", "No ingredient in name"], autopct='%1.1f%%')
    plt.title('Pie Chart of Ingredients in Name')
    plt.show()


''' INGREDIENTS SCRIPTS '''

def ingredients_df(data):
    ingredients = []
    for i in data.ingredients:
        if i:
            for j in i:
                ingredients.append(j)
    ingredients = pd.DataFrame(ingredients)
    ingredients.set_index('id', inplace=True)
    ingredients.head()

    ingredients.drop(columns=['createdAt', 'updatedAt', 'imageUrl'], inplace=True)

    return ingredients

