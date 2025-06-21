def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello" or user_input == "hi":
         print("Bot: Hi!")  
        elif user_input == "how are you?":
            print("Bot: I'm fine, thanks!")
        elif user_input == ("i need help"):
            print("Bot: Sure, how can i help you?")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

if __name__ == "__main__":
    chatbot() 