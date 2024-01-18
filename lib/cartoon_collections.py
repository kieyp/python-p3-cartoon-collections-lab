def roll_call_dwarves(list):
    
    for index, dwarf in enumerate (list):
        
        print(f"{index+1}. {dwarf}")
        
roll_call_dwarves(list=["Doc", "Dopey", "Bashful", "Grumpy"])
    


def summon_captain_planet(planeteer_calls):
    
    data=[n.capitalize() + '!' for n in planeteer_calls]
    return data
result=summon_captain_planet(planeteer_calls=["earth", "wind", "fire", "water", "heart"])
print(result)

short_words = ["puff", "go", "two"]
assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(calls):
    
    for  n in calls:
        if len(n) > 4:
            return True
    return False

print(long_planeteer_calls(short_words))
print(long_planeteer_calls(assorted_words))




def find_the_cheese(snacks):
    cheese=["cheddar","gouda","camembert"]
    for n in snacks:
        if n in cheese:
            return n
        
print(find_the_cheese(snacks=["crackers", "gouda", "thyme"]))



