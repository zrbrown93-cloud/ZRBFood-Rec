def get_user_choice(question, options):
    """
    Placeholder: Will eventually handle user input and validation.
    """
    print(f"[System] Question: {question}")
    # Temporary: Always return option 1 so we can test the flow
    return 1

def determine_cuisine():
    """
    Placeholder: Will eventually hold the decision tree logic.
    """
    print("--- THE 'WHAT SHOULD I EAT?' QUIZ ---")
    
    # We just call the helper to prove it works, but logic is missing.
    get_user_choice("What is the vibe?", ["Option A", "Option B"])
    
    # Return a hardcoded default for now
    return "American" 

def find_restaurant(cuisine, zip_code):
    """
    Placeholder: Will eventually open the web browser.
    """
    # Just print the result to console for verification
    print(f"TODO: Search for {cuisine} restaurants in {zip_code}")

def main():
    # 1. Run the quiz (currently returns default)
    cuisine_result = determine_cuisine()
    
    # 2. Get Zip Code (Temporary placeholder)
    zip_code = "00000" 

    # 3. Output result
    find_restaurant(cuisine_result, zip_code)

if __name__ == "__main__":
    main()