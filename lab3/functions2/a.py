from Dict_of_movies import movies

#1
def check(name = "Love"):
    l = [i["imdb"] for i in movies if i["name"]==name]
    return l[0] > 5.5

print(check())


#2
def sublist_above_5p5():
    l = [i["name"] for i in movies if i["imdb"] > 5.5]
    return l

print(sublist_above_5p5())


#3
def categories(category = "Romance"):
    l = [i['name'] for i in movies if i['category']==category]
    return l

print(categories())


#4
def average_imdb(l):
    d = [i["imdb"] for i in movies if i["name"] in l]
    return sum(d)/len(l)

print(average_imdb(["Bride Wars", "Love", "Colonia", "The Help", "Usual Suspects"]))

#5
def category_imdb(category):
    l = [i["imdb"] for i in movies if i["category"] == category]
    return sum(l)/len(l)

print(category_imdb('Crime')) 
print(category_imdb('Romance')) 
print(category_imdb('Thriller')) 