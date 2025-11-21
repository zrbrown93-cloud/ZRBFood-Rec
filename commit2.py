def get_user_choice(question, options):
    """
    UPDATED: Now actually validates user input.
    """
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_cuisine():
    """
    UPDATED: Now contains the 'branching' logic to pick a specific cuisine.
    """
    print("--- THE 'WHAT SHOULD I EAT?' QUIZ ---")
    
    # Question 1: Temperature/Heaviness
    q1 = get_user_choice(
        "What is the vibe right now?", 
        ["Comfort Food (Hot, Cheesy, or Heavy)", 
         "Something Light & Fresh", 
         "Spicy & Sweat-inducing"]
    )

    # Logic Branch 1: Comfort Food
    if q1 == 1:
        q2 = get_user_choice(
            "Carb of choice?",
            ["Noodles / Pasta", "Bread / Dough / Buns", "Rice"]
        )
        if q2 == 1: return "Italian"
        elif q2 == 2: return "Burgers"
        elif q2 == 3: return "Chinese"

    # Logic Branch 2: Light & Fresh
    elif q1 == 2:
        q2 = get_user_choice(
            "Do you want it cooked or raw?",
            ["Raw / Chilled", "Cooked / Warm"]
        )
        if q2 == 1: return "Sushi"
        elif q2 == 2: return "Mediterranean"

    # Logic Branch 3: Spicy
    elif q1 == 3:
        q2 = get_user_choice(
            "Pick a region:",
            ["Latin American", "Southeast Asian", "South Asian"]
        )
        if q2 == 1: return "Mexican"
        elif q2 == 2: return "Thai"
        elif q2 == 3: return "Indian"
            
    return "American" # Fallback

def find_restaurant(cuisine, zip_code):
    # Still a placeholder
    print(f"TODO: Search for {cuisine} restaurants in {zip_code}")

def main():
    cuisine_result = determine_cuisine()
    zip_code = "00000" 
    find_restaurant(cuisine_result, zip_code)

if __name__ == "__main__":
    main()