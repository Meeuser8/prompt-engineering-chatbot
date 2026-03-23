# Function to greet the user and get their name
def greet_user():
    # Ask the user to type their name
    name = input("Hello! What is your name? ")
    # Print a welcome message using their name
    print(f"Nice to meet you, {name}! I'm your chatbot assistant. Type 'quit' to exit.")
    # Return the name so other functions can use it
    return name

# Function to decide what the chatbot should say
def get_response(user_input):
    # Convert input to lowercase so matching works regardless of caps
    user_input = user_input.lower()
    # Check if the user is saying hello
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! How can I help you today?"
    # Check if the user is asking how the bot is doing
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    # Check if the user needs help
    elif "help" in user_input:
        return "Sure! You can ask me anything. I'm here to chat!"
    # Check if the user asks what the bot can do
    elif "what can you do" in user_input:
        return "I can have a conversation with you! Try asking me how I am or say hello."
    # Default response if nothing matches
    else:
        return f"Interesting! Tell me more about '{user_input}'."

# Function to run the back-and-forth conversation loop
def chat(name):
    # Keep looping until the user decides to quit
    while True:
        # Show the user's name as the input prompt
        user_input = input(f"{name}: ")
        # Check if the user wants to exit
        if user_input.lower() in ["quit", "exit", "bye"]:
            # Say a personalised, encouraging goodbye
            print(f"Goodbye, {name}! Keep up the great work!")
            # Exit the loop
            break
        # Get the chatbot's response and print it
        print(f"Chatbot: {get_response(user_input)}")

# Main function — this is where the program starts
def main():
    name = greet_user()  # Greet the user and save their name
    chat(name)           # Start the conversation

# Run the program
main()