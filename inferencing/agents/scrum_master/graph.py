#from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Dict, Any
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
#from langgraph.checkpoint.memory import MemorySaver

import os

from dotenv import load_dotenv

load_dotenv()

class Epic(BaseModel):
    title: str
    description: str
    features: List['Feature']

class Feature(BaseModel):
    title: str
    description: str
    stories: List['Story']

class Story(BaseModel):
    title: str
    description: str
    acceptance_criteria: List[str]
    status: str
    priority: str
    assigned_to: str
    
class Task(BaseModel):
    id: str
    type: str  # "data", "ui", "backend"
    story: Story
    priority: int
    
class SupervisorState(TypedDict):
    user_request: str
    epic: Epic
    requirements_doc: str
    design_doc: str
    tasks: List[Task]
    messages: List[str]
    
def parse_request(state: SupervisorState) -> SupervisorState:
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
    prompt = f"""
    Extract a short epic title from this request:
    {state['user_request']}
    
    Return only the title, nothing else.
    """
    
    response = llm.invoke(prompt)
    state['epic_title'] = response.content.strip()
    return state

def generate_requirements(state: SupervisorState) -> SupervisorState:
    """Generate requirements document"""
    prompt = f"""
    Create a concise requirements document for:
    Epic: {state['epic'].title}
    Description: {state['epic'].description}
    
    Include:
    - Functional requirements (5-7 items)
    - Non-functional requirements (3-5 items)
    - Constraints
    
    Keep it under 500 words.
    """
    
    response = llm.invoke(prompt)
    state['requirements_doc'] = response.content
    return state

def generate_design(state: SupervisorState) -> SupervisorState:
    """Generate design document"""
    prompt = f"""
    Create a technical design document for:
    Epic: {state['epic'].title}
    Requirements: {state['requirements_doc'][:500]}
    
    Include:
    - Architecture overview
    - Data flow
    - Key components
    - Technology stack
    
    Keep it under 500 words.
    """
    
    response = llm.invoke(prompt)
    state['design_doc'] = response.content
    return state

def create_stories(state: SupervisorState) -> SupervisorState:
    """Break down features into stories"""
    stories = []
    
    for feature in state['epic'].features:
        prompt = f"""
        Break down this feature into 2-3 user stories:
        Feature: {feature.title}
        Description: {feature.description}
        
        For each story provide:
        - Title
        - Description
        - 3-4 acceptance criteria
        - Suggested assignment (data_engineer, ui_developer, backend_engineer)
        
        Return as JSON array.
        """
        
        response = llm.invoke(prompt)
        # Parse stories and add to feature
        feature.stories = []  # Would parse from response
    
    return state

def assign_tasks(state: SupervisorState) -> SupervisorState:
    """Create task assignments for agents"""
    tasks = []
    task_id = 0
    
    for feature in state['epic'].features:
        for story in feature.stories:
            task = Task(
                id=f"T{task_id:03d}",
                type=story.assigned_to.split('_')[0],  # Extract type
                story=story,
                priority=task_id + 1
            )
            tasks.append(task)
            task_id += 1
    
    state['tasks'] = tasks
    return state

def validate_output(state: SupervisorState) -> SupervisorState:
    """Final validation and summary"""
    summary = f"""
    Created Epic: {state['epic'].title}
    Total Features: {len(state['epic'].features)}
    Total Stories: {sum(len(f.stories) for f in state['epic'].features)}
    Total Tasks: {len(state['tasks'])}
    """
    state['messages'].append(summary)
    return state

def create_supervisor_graph():
    workflow = StateGraph(SupervisorState)
    
    # Add nodes
    workflow.add_node("parse_request", parse_request)
    workflow.add_node("generate_requirements", generate_requirements)
    workflow.add_node("generate_design", generate_design)
    workflow.add_node("create_stories", create_stories)
    workflow.add_node("assign_tasks", assign_tasks)
    workflow.add_node("validate_output", validate_output)
    
    # Add edges
    workflow.set_entry_point("parse_request")
    workflow.add_edge("parse_request", "generate_requirements")
    workflow.add_edge("generate_requirements", "generate_design")
    workflow.add_edge("generate_design", "create_stories")
    workflow.add_edge("create_stories", "assign_tasks")
    workflow.add_edge("assign_tasks", "validate_output")
    workflow.add_edge("validate_output", END)
    
    # Compile
    #memory = MemorySaver()
    return workflow.compile()#(checkpointer=memory)

# Helper function to run the supervisor
async def run_supervisor(user_request: str) -> Dict[str, Any]:
    graph = create_supervisor_graph()
    
    initial_state = {
        "user_request": user_request,
        "epic": None,
        "requirements_doc": "",
        "design_doc": "",
        "tasks": [],
        "messages": []
    }
    
    config = {"configurable": {"thread_id": "main"}}
    result = await graph.ainvoke(initial_state, config)
    
    return {
        "epic": result["epic"],
        "requirements": result["requirements_doc"],
        "design": result["design_doc"],
        "tasks": result["tasks"]
    }
    
    
# class SharedState(TypedDict):
#     messages: List[str]
#     shared_data: dict
#     agent_states: dict


# # Compile individual agent as subgraph
# research_graph = StateGraph(SharedState)
# research_graph.add_node("research", research_function)
# compiled_research = research_graph.compile()

# # Add to parent supervisor graph
# supervisor_graph = StateGraph(SharedState)
# supervisor_graph.add_node("research_agent", compiled_research)
# supervisor_graph.add_node("analysis_agent", compiled_analysis)
