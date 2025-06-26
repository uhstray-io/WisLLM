from abc import ABC, abstractmethod
from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Any, Optional

class BaseAgent(ABC):
    """Base class for all LangGraph agents with shared functionality"""
    
    def __init__(
        self,
        agent_id: str,
        model: Any,
        tools: List[Any],
        state_store: StateStore,
        handoff_manager: HandoffManager
    ):
        self.agent_id = agent_id
        self.model = model
        self.tools = tools
        self.state_store = state_store
        self.handoff_manager = handoff_manager
        self.graph = self._build_graph()
    
    @abstractmethod
    def _build_graph(self) -> StateGraph:
        """Build the agent's LangGraph workflow"""
        pass
    
    async def update_shared_state(self, updates: Dict[str, Any]) -> None:
        """Update shared state with agent context"""
        await self.state_store.update_shared_state({
            **updates,
            "last_updated_by": self.agent_id,
            "agent_status": {self.agent_id: "working"}
        })
    
    async def handoff_to_agent(
        self, 
        target_agent: str, 
        payload: Dict[str, Any]
    ) -> None:
        """Handoff task to another agent"""
        await self.handoff_manager.handoff(
            from_agent=self.agent_id,
            to_agent=target_agent,
            payload=payload
        )