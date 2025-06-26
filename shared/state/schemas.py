class PrivateState(TypedDict):
    internal_data: str
    processing_steps: List[str]

class PublicState(TypedDict):
    shared_messages: List[str]
    final_results: dict

def isolated_agent(state: PublicState, config: RunnableConfig) -> dict:
    # Private processing with isolated state
    private_state = PrivateState(
        internal_data="sensitive_info",
        processing_steps=[]
    )
    
    # Process internally
    results = process_with_private_state(private_state)
    
    # Return only public updates
    return {"final_results": sanitize_results(results)}