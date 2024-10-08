def show_tags(data):
    tags = []
    for i in data.tags:
        if i:
            for j in i:
                tags.append(j)
    print(tags)


def analyze_IBA(data):
    # oficjalne IBA
    with open("../data/official_IBA.txt", "r", encoding="utf-8") as file:
        official_IBA = file.read().splitlines()

    i = 0
    # weryfikuję czy tagi IBA sie zgadzają 
    for _, row in data.iterrows():
        if type(row["tags"]) == list:
            if row["tags"].count("IBA") > 0:
                if row["name"] not in official_IBA:
                    print("Drinki usunięte z IBA:", row["name"])
            elif row["name"] in official_IBA:
                print(row["name"], row["tags"])
                

    print("Anomalie: ", i)

