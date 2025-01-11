# Test cases for the InternetSupportAgent class
import pytest
from agents.support_agent import InternetSupportAgent

@pytest.fixture
def agent():
    return InternetSupportAgent()

def test_identify_issue(agent):
    assert agent.identify_issue("My internet is not working") == "no_internet"
    assert agent.identify_issue("Wi-Fi is not connecting") == "wifi_issue"
    assert agent.identify_issue("Random input") is None

def test_provide_solution(agent):
    assert agent.provide_solution("no_internet") == "1. Check if your router is powered on.\n2. Restart your router and modem.\n3. Ensure all cables are securely connected."
    assert agent.provide_solution("unknown_issue") == "I'm sorry, I couldn't identify the issue. Please try again."

def test_handle_request(agent):
    response = agent.handle_request("My internet is not working")
    assert "Did this resolve your issue?" in response["response"]

    response = agent.handle_request("yes")
    assert "Great! Let me know if you need help with anything else." in response["response"]

    response = agent.handle_request("no")
    assert "Let’s try something else:" in response["response"]