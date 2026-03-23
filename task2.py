# Task 2: Persona + Context Version
# Built for: Students
# Developer Persona: Senior Python Developer

print("--- Student Assistant Chatbot ---")

# Step 1: Contextual greeting (asking for name)
user_name = input("Hello! I'm your Python assistant. What is your name? ")
print(f"It's great to meet you, {user_name}! How can I help with your studies today?")

# Step 2: Main loop with improved logic
while True:
    request = input(f"\n{user_name}: ").lower()

    if "exit" in request or "quit" in request:
        print(f"Goodbye, {user_name}! Good luck with your coding.")
        break
    elif "help" in request:
        print("Assistant: I can help explain loops, variables, or functions!")
    elif "python" in request:
        print("Assistant: Python is a high-level, interpreted language known for readability.")
    else:
        print("Assistant: That's a great question. Let's look into that together.")