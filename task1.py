while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: I heard you say:", user_input)