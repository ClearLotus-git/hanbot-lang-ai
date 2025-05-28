# HanBot: Korean to English AI Chatbot

# HanBot: Korean to English AI Chatbot

def welcome():
    print("안녕하세요! Welcome to HanBot 🇰🇷🤖")
    print("Type in English or Korean and I'll help you learn!")
    print("Type 'exit' to quit.")

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "안녕" in user_input:
        return "안녕하세요! How can I help you with Korean or English today?"
    elif "thank" in user_input or "고마워" in user_input:
        return "You’re welcome! 천만에요!"
    elif "bye" in user_input or "잘가" in user_input:
        return "Goodbye! 다음에 봐요!"
    else:
        return f"I heard you say '{user_input}', but I'm still learning!"

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("HanBot: Goodbye! 다음에 봐요!")
            break
        else:
            response = get_response(user_input)
            print(f"HanBot: {response}")

if __name__ == "__main__":
    welcome()
    chat()

