# def mad_libs():
#     print("let\'s play Mad Libs! fill in the the blanks with your own words. ")

#     name= input("Give me a name:")
#     place=input("Give me a place:")
#     Funny_adj= input("Give me a adejective:")
#     random_object= input("Give me a object:")
#     animal= input("Give me a animal:")
#     action_verb= input("Give me a verb:")
#     funny_exclamation= input("Give me a funny exclamation:")

#     story = f''' 
#     Once upon a time, there was a person named {name} who lived in {place}.
#     One day, they find a {Funny_adj} {random_object} that belonged to a {animal}.
#     The {animal} was vers  
#     '''





def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks with your own words.")
    print("------------------------------------------------------------\n")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Give me a funny adjective: ")
    random_object = input("Give me an object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me a verb ending in -ing: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f"""
    ------------------------------------------------------------
    Once upon a time in the far land of {place}, there lived a curious soul named {name}.

    One sunny afternoon, {name} was walking through the forest when they stumbled upon a very {funny_adj} {random_object} lying on the ground.
    Just as they reached down to pick it up, a wild {animal} jumped out from behind a tree — {action_verb} like it was on a sugar rush!

    Startled, {name} screamed, "{funny_exclamation}!" and ran in circles for ten seconds before realizing the {animal} just wanted to play.

    And from that day forward, {name} and the {funny_adj} {animal} became the best of friends, bonding over their love of {random_object}s and unexpected surprises.

    The end. 🐾
    ------------------------------------------------------------
    """

    print(story)


if __name__ == "__main__":
    mad_libs()
