import webbrowser
import urllib.parse
import time

def get_user_choice(question, options):
    """
    Helper function to ask a question and validate the input.
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
    Runs the logic to determine cuisine based on 3 questions.
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
        if q2 == 1:
            return "Italian"
        elif q2 == 2:
            return "Burgers"
        elif q2 == 3:
            return "Chinese"

    # Logic Branch 2: Light & Fresh
    elif q1 == 2:
        q2 = get_user_choice(
            "Do you want it cooked or raw?",
            ["Raw / Chilled", "Cooked / Warm"]
        )
        if q2 == 1:
            return "Sushi"
        elif q2 == 2:
            return "Mediterranean"

    # Logic Branch 3: Spicy
    elif q1 == 3:
        q2 = get_user_choice(
            "Pick a region:",
            ["Latin American (Tacos/Salsa)", "Southeast Asian (Curry/Noodles)", "South Asian (Curry/Naan)"]
        )
        if q2 == 1:
            return "Mexican"
        elif q2 == 2:
            return "Thai"
        elif q2 == 3:
            return "Indian"
            
    return "American" # Fallback

def find_restaurant(cuisine, zip_code):
    """
    UPDATED: Constructs a search URL and opens the web browser.
    """
    print(f"\nThinking...")
    time.sleep(1)
    print(f"The computer has decided! You are having: {cuisine.upper()}")
    
    # Construct the search query
    query = f"best {cuisine} restaurants near {zip_code}"
    
    # Encode the query for a URL (handles spaces and special characters)
    encoded_query = urllib.parse.quote(query)
    
    # Create Google Maps URL
    url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
    
    print(f"Opening a map of {cuisine} places near {zip_code}...")
    webbrowser.open(url)

def main():
    # 1. Run the quiz
    cuisine_result = determine_cuisine()
    
    # 2. Get Zip Code (UPDATED: Added validation loop)
    while True:
        zip_code = input("\nEnter your Zip Code: ")
        if len(zip_code) == 5 and zip_code.isdigit():
            break
        print("Please enter a valid 5-digit zip code.")

    # 3. Find the results
    find_restaurant(cuisine_result, zip_code)

if __name__ == "__main__":
    main()