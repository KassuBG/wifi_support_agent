from agents.support_agent import InternetSupportAgent

def main():
    print("Debug: Starting the agent...")  
    agent = InternetSupportAgent()
    print("Debug: Agent initialized.")  
    print("Welcome to Internet Troubleshooting Support! How can I help you today?")
    
    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Thank you for using our support. Goodbye!")
            break
        
        print(f"Debug: User input: {user_input}")  
        response = agent.handle_request(user_input)
        print(f"Debug: Agent response: {response}")  
        print(response)

if __name__ == "__main__":
    print("Debug: Running main()...")  
    main()
