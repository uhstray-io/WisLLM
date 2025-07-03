# Full History Sharing
def agent_with_full_context(state: MultiAgentState):
    # Access complete conversation history
    full_context = state["messages"]
    shared_data = state["shared_context"]
    return process_with_full_context(full_context, shared_data)


# Filtered History with Private State
class AgentState(TypedDict):
    public_messages: List[str]
    shared_results: dict
    private_scratchpad: List[str]  # Agent-specific internal state


def agent_with_filtered_context(state: AgentState):
    # Filter messages for agent-specific context
    relevant_messages = [msg for msg in state["public_messages"] if msg.get("agent") in ["self", "supervisor"]]
    # Maintain private working memory
    state["private_scratchpad"].append("internal_processing_note")
    return process_with_filtered_context(relevant_messages)
