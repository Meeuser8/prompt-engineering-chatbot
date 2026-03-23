def greet_user():
    name = input("Hello! What is your name? ")
    print(f"Nice to meet you, {name}! I'm your chatbot assistant. Type 'quit' to exit.")
    return name

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    elif "help" in user_input:
        return "Sure! You can ask me anything. I'm here to chat!"
    else:
        return f"Interesting! Tell me more about '{user_input}'."

def chat(name):
    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print(f"Goodbye, {name}! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

def main():
    name = greet_user()
    chat(name)

main()