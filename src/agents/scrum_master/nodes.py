from langgraph.types import Command
from typing import Literal


def supervisor_node(
    state: SharedState,
) -> Command[Literal["researcher", "analyzer", END]]:
    if needs_research(state):
        return Command(
            goto="researcher",
            update={"current_agent": "researcher", "task_context": context},
        )
    elif needs_analysis(state):
        return Command(goto="analyzer", update={"current_agent": "analyzer"})
    return Command(goto=END)
