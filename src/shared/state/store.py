from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.memory import InMemoryStore
from typing import Annotated
from operator import add

class MultiAgentState(TypedDict):
    messages: Annotated[List[str], add]  # Reducer for combining messages
    shared_context: dict
    agent_states: dict
    current_agent: str
    task_queue: List[dict]

# Configure persistence
checkpointer = PostgresSaver.from_conn_string("postgresql://...")
store = InMemoryStore()

# Compile with persistence
app = graph.compile(
    checkpointer=checkpointer,
    store=store
)

# State automatically persisted and synchronized across agents