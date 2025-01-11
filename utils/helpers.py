
import random

def get_random_response(category):
    """Get a random response from a predefined category."""
    responses = {
        "greeting": [
            "Hey there! I’m your Internet Troubleshooting Buddy. Let’s get you back online!",
            "Hi! I’m here to save the day (and your internet). What’s the issue?",
            "Hello! Let’s fix your internet woes together. What’s going on?"
        ],
        "positive_feedback": [
            "Woohoo! You’re back online! 🎉",
            "Success! You’re a troubleshooting pro! 🚀",
            "Problem solved! You’re unstoppable! 💪"
        ],
        "negative_feedback": [
            "Hmm, that didn’t work? No worries, let’s try something else!",
            "Oops! Let’s give it another shot.",
            "Darn! Let’s troubleshoot like a detective. 🕵️‍♂️"
        ],
        "escalation": [
            "I’ve done my best, but it’s time to call in the human experts. Hang tight!",
            "This is a tough one! Let me connect you with a human agent.",
            "I’m stumped! Let’s get a human to help you out."
        ]
    }
    return random.choice(responses[category])
