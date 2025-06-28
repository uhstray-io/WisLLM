from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List

class SharedState(TypedDict):
    messages: List[str]
    shared_data: dict
    agent_states: dict

# Compile individual agent as subgraph
research_graph = StateGraph(SharedState)
research_graph.add_node("research", research_function)
compiled_research = research_graph.compile()

# Add to parent supervisor graph
supervisor_graph = StateGraph(SharedState)
supervisor_graph.add_node("research_agent", compiled_research)
supervisor_graph.add_node("analysis_agent", compiled_analysis)