from graph import create_supervisor_graph, SupervisorState

graph = create_supervisor_graph()
result = graph.invoke({
    "user_request": "Build a dashboard",
    "epic_title": "",
    "requirements_doc": "",
    "stories": []
})
print(f"Final state: {result}")