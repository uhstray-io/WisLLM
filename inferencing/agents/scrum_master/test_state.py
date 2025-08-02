# test_state.py
from graph import Story, SupervisorState

# Test creating a story
story = Story(
    title="Setup Database",
    description="Create initial database schema",
    acceptance_criteria=["Tables created", "Indexes added"],
    status="To Do",
    priority="High",
    assigned_to="data_engineer"
)
print(f"Story created: {story.title}")

# Test state
state: SupervisorState = {
    "user_request": "Build a dashboard",
    "epic_title": "",
    "requirements_doc": "",
    "stories": []
}
print(f"State initialized: {state}")