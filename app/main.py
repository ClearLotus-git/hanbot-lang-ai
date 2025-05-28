# HanBot: Korean to English AI Chatbot

#greeting message or beginning of chat introductions
def welcome():
    print("안녕하세요! Welcome to HanBot 🇰🇷🤖")
    print("Type in English or Korean and I'll help you learn!")
    print("영어나 한국어로 입력하면 도와드릴게요!")
    print("Type 'exit' to quit.")

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "안녕" in user_input:
        return "안녕하세요! How can I help you with Korean or English today?"
    
    elif "thank" in user_input or "thank you" in user_input or "고마워" in user_input:
        return "You’re welcome! 천만에요! 별말씀을요!"
    def contains_korean(text):
    for ch in text:
        if ord('가') <= ord(ch) <= ord('힣'):
            return True
    return False

elif "bye" in user_input or "잘가" in user_input:
    return "Goodbye! 다음에 봐요!"
else:
    if contains_korean(user_input):
        return "한국어를 입력하셨네요! 아직 배우는 중이라 이해가 부족할 수 있어요."
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

