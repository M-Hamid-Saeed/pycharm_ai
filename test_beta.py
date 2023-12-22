from py2neo import database, Graph, Node, Relationship
simpa = Node("Cat", name="Simpa", color="white")
alia = Node("Person", name="Alia", type="hobbit", age=100)
village = Node("Place", name="Acciaroli", age=100)
whale = Node("Mammal", name="Whale", livesInWater=True)
crab = Node("Animal", name="Crab")
alia_owns_simpa = Relationship(alia, "OWNS", simpa)
alia_found_ring = Relationship(alia, "FOUND", Node("Item", name="magic ring"))
alia_lived_in_village = Relationship(alia, "LIVED_IN", village)
village_on_shore = Relationship(village, "ON_SHORE_OF", Node("Place", name="ocean"))
alia_saw_whale = Relationship(alia, "SAW", whale)
whale_has_vertebrae = Relationship(whale, "HAS", Node("BodyPart", name="vertebrae"))
simpa_likes_milk = Relationship(simpa, "LIKES", Node("Food", name="Milk"))
simpa_likes_salmon = Relationship(simpa, "LIKES", Node("Food", name="Salmon fish"))
simpa_sits_on_carpet = Relationship(simpa, "SITS_ON", Node("Furniture", name="Carpet"))
simpa_caught_bird = Relationship(simpa, "CAUGHT", Node("Bird", name="Killdeer", fur=True, beak="long and thin"))
simpa_bitten_by_crab = Relationship(simpa, "BITTEN_BY", crab)
alia_likes_fish = Relationship(alia, "LIKES", Node("Activity", name="catch and eat fish"))
bird_hiding_between_curtain = Relationship(Node("Bird", name="Killdeer"), "HIDING_BETWEEN", Node("Furniture", name="curtain"))
bird_hiding_between_window = Relationship(Node("Bird", name="Killdeer"), "HIDING_BETWEEN", Node("Furniture", name="window"))

graph.create(simpa, alia, village, whale, crab, alia_owns_simpa, alia_found_ring, alia_lived_in_village, village_on_shore,
              alia_saw_whale, whale_has_vertebrae, simpa_likes_milk, simpa_likes_salmon, simpa_sits_on_carpet,
              simpa_caught_bird, simpa_bitten_by_crab, alia_likes_fish, bird_hiding_between_curtain, bird_hiding_between_window)

# 1.1. Write statement to add Alia likes to catch and eat fish. Simpa was once bitten by a Crab on the shore. Crab is also an animal but not a mammal.
alia_likes_fish = Relationship(alia, "LIKES", Node("Activity", name="catch and eat fish"))
simpa_bitten_by_crab = Relationship(simpa, "BITTEN_BY", crab)
graph.create(alia_likes_fish, simpa_bitten_by_crab)

# 1.2. Write statement to modify “Acciaroli” is the name of her village which is about 100 years old. => “Acciaroli” is the name of her village which is about 1000 years old.
query_modify_village = "MATCH (village:Place {name: 'Acciaroli'}) SET village.age = 1000"
graph.run(query_modify_village)

# 1.3. Write statements to delete the following statements
# a. Simpa is white in color and is owned by a Girl, Alia.
query_delete_simpa = "MATCH (simpa)-[r:OWNS]->(alia) DELETE r"
graph.run(query_delete_simpa)

# b. Alia once saw a big Whale
query_delete_saw_whale = "MATCH (alia)-[r:SAW]->(:Mammal {name: 'Whale'}) DELETE r"
graph.run(query_delete_saw_whale)

# 1.4. Write cipher statements to find the answer to the following queries:
# a. What’s the age of Alia?
query_age_of_alia = "MATCH (alia:Person {name: 'Alia'}) RETURN alia.age AS age"
result_age_of_alia = graph.run(query_age_of_alia).data()
print(result_age_of_alia)

# b. What type of mammal the Whale is?
query_type_of_whale = "MATCH (whale:Mammal {name: 'Whale'}) RETURN whale"
result_type_of_whale = graph.run(query_type_of_whale).data()
print(result_type_of_whale)

# c. Where is Killdeer hiding?
query_where_is_killdeer = "MATCH (killdeer:Bird {name: 'Killdeer'})-[:HIDING_BETWEEN]->(furniture) RETURN furniture.name AS hiding_place"
result_where_is_killdeer = graph.run(query_where_is_killdeer).data()
print(result_where_is_killdeer)