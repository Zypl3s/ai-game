import random

# Character classes
classes = {
    "Warrior": {"Strength": 10, "Agility": 5, "Magic": 2},
    "Mage": {"Strength": 2, "Agility": 5, "Magic": 10},
    "Rogue": {"Strength": 5, "Agility": 10, "Magic": 3}
}

# Items
items = {
    "Potion": {"heal": 20},
    "Magic Scroll": {"damage": 15},
    "Sword": {"damage": 10}
}

# Game state
player = {
    "name": "",
    "class": "",
    "stats": {},
    "health": 100,
    "inventory": [],
    "location": "Haunted Forest"
}

# Enemies
enemies = {
    "Haunted Forest": {"name": "Ghost Wolf", "health": 30, "damage": 10},
    "Enchanted Castle": {"name": "Dark Knight", "health": 50, "damage": 15},
    "Bandit's Lair": {"name": "Bandit Chief", "health": 70, "damage": 20}
}

# Combat system
def combat(enemy):
    print(f"\n⚔️ You encounter a {enemy['name']}!")
    while enemy["health"] > 0 and player["health"] > 0:
        print(f"\nYour HP: {player['health']} | Enemy HP: {enemy['health']}")
        action = input("Choose action (Attack / Use Item / Defend): ").strip().lower()
        if action == "attack":
            damage = random.randint(5, 15) + player["stats"]["Strength"]
            enemy["health"] -= damage
            print(f"You deal {damage} damage!")
        elif action == "use item":
            if not player["inventory"]:
                print("Your inventory is empty.")
            else:
                print("Inventory:", player["inventory"])
                item = input("Choose item: ").strip()
                if item in player["inventory"]:
                    if item == "Potion":
                        player["health"] += items[item]["heal"]
                        print("You healed 20 HP.")
                    elif item == "Magic Scroll":
                        enemy["health"] -= items[item]["damage"]
                        print("You cast a spell for 15 damage!")
                    elif item == "Sword":
                        enemy["health"] -= items[item]["damage"]
                        print("You slash for 10 damage!")
                    player["inventory"].remove(item)
                else:
                    print("Item not found.")
        elif action == "defend":
            print("You brace for impact. Reduced damage next turn.")
            player["health"] -= max(0, enemy["damage"] - 5)
        else:
            print("That's not a valid command.")
            continue
        if enemy["health"] > 0:
            player["health"] -= enemy["damage"]
            print(f"The {enemy['name']} hits you for {enemy['damage']} damage!")

    if player["health"] <= 0:
        print("💀 You have fallen in battle...")
        return "dead"
    else:
        print(f"🏆 You defeated the {enemy['name']}!")
        return "alive"

# Story progression
def story():
    for location in ["Haunted Forest", "Enchanted Castle", "Bandit's Lair"]:
        player["location"] = location
        print(f"\n📍 You arrive at the {location}.")
        player["inventory"].append(random.choice(list(items.keys())))
        result = combat(enemies[location])
        if result == "dead":
            return "defeat"
        choice = input("Do you want to explore further or rest? (Explore / Rest): ").strip().lower()
        if choice == "rest":
            player["health"] += 10
            print("You rest and recover 10 HP.")
    return ending()

# Branching endings
def ending():
    print("\n🐉 Final Choice: You meet a dragon.")
    choice = input("Do you Befriend or Fight the dragon? ").strip().lower()
    if choice == "befriend":
        return "peace"
    elif choice == "fight":
        result = combat({"name": "Ancient Dragon", "health": 100, "damage": 25})
        return "victory" if result == "alive" else "defeat"
    else:
        print("Invalid choice. The dragon flies away.")
        return "neutral"

# Game start
def start_game():
    print("🎮 Welcome to Fantasy Quest!")
    player["name"] = input("Enter your name: ")
    print("Choose your class:")
    for c in classes:
        print(f"- {c}")
    while True:
        chosen_class = input("Class: ").strip().title()
        if chosen_class in classes:
            player["class"] = chosen_class
            player["stats"] = classes[chosen_class]
            break
        else:
            print("Invalid class. Try again.")
    print(f"\nWelcome, {player['name']} the {player['class']}!")
    outcome = story()
    if outcome == "peace":
        print("🌈 You and the dragon bring peace to the realm.")
    elif outcome == "victory":
        print("🏅 You slay the dragon and become a legend.")
    elif outcome == "defeat":
        print("💀 Your journey ends in battle.")
    else:
        print("🕊️ You walk away, leaving fate undecided.")

start_game()