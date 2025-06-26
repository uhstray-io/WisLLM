from langgraph_supervisor import create_supervisor
from langgraph.types import Command

# Create specialized agents 
research_agent = create_react_agent(
    model="gpt-4o",
    tools=[web_search_tool, database_query_tool],
    name="research_expert"
)

analysis_agent = create_react_agent(
    model="gpt-4o", 
    tools=[data_analysis_tool, visualization_tool],
    name="analysis_expert"
)

# Create supervisor workflow with handoff logic
def create_handoff_tool(agent_name: str):
    @tool(f"transfer_to_{agent_name}")
    def handoff_to_agent(
        task_description: str,
        context: dict,
        state: Annotated[dict, InjectedState]
    ):
        return Command(
            update={"current_agent": agent_name, "task_context": context},
            goto=agent_name
        )
    return handoff_to_agent

supervisor_graph = create_supervisor(
    agents=[research_agent, analysis_agent],
    model="gpt-4o",
    prompt="You are coordinating research and analysis tasks."
)