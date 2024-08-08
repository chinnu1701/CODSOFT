import re

# Expanded list of patterns and corresponding responses
patterns_responses = [
    # Greetings
    (r"hello|hi|hey", "Hello! How can I assist you today?"),
    
    # Asking about the chatbot
    (r"who are you|what are you", "I'm a chatbot here to help you with various topics!"),
    
    # Asking how the chatbot is
    (r"how are you|how's it going", "I'm just a bot, but I'm doing great! How about you?"),
    
    # Asking about the weather
    (r"what's the weather|weather|forecast", "I'm not connected to a weather service, but it's always a good day to learn something new!"),
    
    # Asking about technology
    (r"technology|tech|latest gadgets|AI", "Technology is fascinating! AI, robotics, and the latest gadgets are transforming the world."),
    
    # Coffee-related questions
    (r"coffee|brew|espresso|latte|cappuccino", "I love coffee too! What's your favorite way to brew it?"),
    
    # Sports-related questions
    (r"sports|soccer|basketball|tennis|cricket", "Sports are a great way to stay active! What's your favorite sport?"),
    
    # Food-related questions
    (r"food|pizza|sushi|burger|recipe", "Food is a delicious topic! What type of cuisine do you like?"),
    
    # Asking for help
    (r"help|assist|support", "Sure, I'm here to help! What do you need assistance with?"),
    
    # Saying goodbye
    (r"bye|goodbye|see you", "Goodbye! Have a wonderful day!"),
    
    # Catch-all for unrecognized input
    (r".*", "I'm not sure I understand. Could you tell me more or ask about something else?")
]

# Function to match patterns
def match_pattern(user_input):
    for pattern, response in patterns_responses:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that."

# Main function
def main():
    print("Welcome to the Enhanced Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r"bye|goodbye|see you", user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        response = match_pattern(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
