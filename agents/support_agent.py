# Description: File contains the implementation of the InternetSupportAgent class, 
# which is responsible for identifying internet connectivity issues and providing troubleshooting steps 
# to resolve them.

class InternetSupportAgent:
    def __init__(self):
        self.issues = {
            "no_internet": ["no internet connection", "internet is not working", "no internet"],
            "slow_speed": ["slow internet speeds", "internet is slow", "slow connection"],
            "wifi_issue": ["wi-fi connectivity problems", "wi-fi is not working", "can't connect to wi-fi", "wi-fi is not connecting"],
            "router_issue": ["router or modem issues", "router is not working", "modem is not working"]
        }
        self.knowledge_base = {
            "no_internet": [
                "1. Check if your router is powered on.",
                "2. Restart your router and modem.",
                "3. Ensure all cables are securely connected."
            ],
            "slow_speed": [
                "1. Run a speed test to check your current speed.",
                "2. Restart your router and modem.",
                "3. Move closer to the router for a stronger signal."
            ],
            "wifi_issue": [
                "1. Check if your device is connected to the correct Wi-Fi network.",
                "2. Restart your router and modem.",
                "3. Forget the Wi-Fi network on your device and reconnect."
            ],
            "router_issue": [
                "1. Power cycle your router and modem.",
                "2. Check for firmware updates for your router.",
                "3. Contact your ISP for further assistance."
            ]
        }
        self.context = {
            "current_issue": None,
            "steps_taken": [],
            "retry_count": 0  # Track the number of retries
        }

    def identify_issue(self, user_input):
        """Identify the issue based on user input."""
        print(f"Debug: User input: {user_input}") 
        user_input = user_input.lower()
        for key, phrases in self.issues.items():
            for phrase in phrases:
                if phrase in user_input:
                    print(f"Debug: Identified issue: {key}")  
                    return key
        print("Debug: No issue identified.")  
        return None

    def update_context(self, issue_key):
        """Update the context with the current issue and steps taken."""
        self.context["current_issue"] = issue_key
        self.context["steps_taken"] = self.knowledge_base.get(issue_key, [])

    def provide_solution(self, issue_key):
        """Provide troubleshooting steps for the identified issue."""
        if issue_key in self.knowledge_base:
            return "\n".join(self.knowledge_base[issue_key])
        return "I'm sorry, I couldn't identify the issue. Please try again."

    def handle_request(self, user_input):
        """Handle the user's request with context awareness and error handling."""
        try:
            issue_key = self.identify_issue(user_input)
            if issue_key:
                self.update_context(issue_key)
                solution = self.provide_solution(issue_key)
                return {"response": solution + "\n\nDid this resolve your issue? (yes/no)"}
            elif "yes" in user_input.lower():
                return {"response": "Great! Let me know if you need help with anything else."}
            elif "no" in user_input.lower():
                if self.context["steps_taken"]:
                    if self.context.get("retry_count", 0) < 2:  # Allow up to 2 retries
                        self.context["retry_count"] = self.context.get("retry_count", 0) + 1
                        return {"response": "Let’s try something else:\n" + self.provide_solution(self.context["current_issue"])}
                    else:
                        return {"response": "I'm sorry, I couldn't resolve your issue. Let me connect you with a human agent."}
                else:
                    return {"response": "I'm sorry, I couldn't resolve your issue. Let me connect you with a human agent."}
            else:
                return {"response": "I’m not sure I understand. Can you tell me more about the issue?"}
        except Exception as e:
            return {"response": f"Oops! Something went wrong. Let’s try again. Error: {e}"}