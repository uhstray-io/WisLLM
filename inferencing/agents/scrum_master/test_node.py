# test_node.py
from graph import parse_request, SupervisorState

state = {
    "user_request": "Build a customer analytics dashboard with sales metrics",
    "epic_title": "",
    "requirements_doc": "",
    "stories": []
}

result = parse_request(state)
print(f"Epic title: {result['epic_title']}")