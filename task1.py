print("Hello! I am a simple python chatbot.")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "quit":
        print("Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello there! How can I help you today?")
    elif "how are you" in user_input:
        print("Chatbot: I am just a program, but I am functioning well!")
    elif "weather" in user_input:
        print("Chatbot: I cannot check the weather yet, but it looks like code outside.")
    else:
        print("Chatbot: That is interesting. Tell me more!")