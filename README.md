# WisLLM

LLM Agentic Development Team, designed to support business-as-code platforms, services, and data.

### MVP Goals

- Develop comprehensive requirements documentation for a project.
- Copilot instructons for each LLM/Agent should be generated from the requirements.
- Write the initial stories necesary to implement the project.
- Develop a plan and priorities to tackle the project in an agile manner.
- Scrum Master LLM should be able to delegate tasks to the appropriate agents.
- Each LLM developer should focus on their specific expertise and delivery only on the next iterative task

### Design Philosophy

- **Locally Capable**: Each agent and LLM should be capable of running on local computers.
- **Energy Efficiency**: The system should be designed to minimize energy consumption, allowing for efficient operation on local hardware.
- **Feedback Required**: Every agent should demand and require feedback from one another or the user.
- **Agentic**: Agents should be able to operate independently, but also collaborate when necessary.
- **Collaborative**: Agents should be able to work together to achieve a common goal.
- **Agile Development**: The system should be designed to support agile development practices, allowing for rapid iteration and improvement.
- **Complexity**: LLM Context use-cases and windows should be minimized to reduce complexity and improve performance.
- **Modular**: The system should be modular, allowing for easy integration or swapping of new agents and services.

### WisLLM Design Architecture

```mermaid
flowchart TD
    subgraph Users
        User[Business Users]
    end

    subgraph Design[Design LLMs]
        Scrum[Scrum Master]
        Architect[Solutions Architect]
        DataScientist[Data Scientist]
        Researcher[Requirements Researcher]
    end

    subgraph Collab[Collaboration Protocols]
        A2A[Agent to Agent Protocol]
    end

    subgraph Dev[Developer LLMs]
        UXUI[UX/UI Dev]
        Backend[Backend Developer]
        Data[Data Engineer]
    end

    subgraph Ops[Operations LLMs]
        DevSecOps[DevSecOps Developer]
        Infrastructure[Infrastructure Automator]
        Reporter[Reporting Operator]
    end

    subgraph Int[Interface Protocols]
        MCP[Model Context Protocol]
    end

    User <--> Scrum
    User <--> Architect

    Architect <--> Scrum
    Architect <--> DataScientist
    
    Architect <--> Researcher
    DataScientist <--> Researcher

    Design <--> Collab
    Collab <--> Dev
    Collab <--> Ops

    Dev --> Int
    Ops --> Int
```

### TODO

- [ ] Update Data Team Roles (Data Scientist, Data Architect, Data Warehousing)

## Getting Started

```python
uv venv --python 3.12 --seed
source .venv/bin/activate
```

%pip install --upgrade --quiet  vllm -q


nanonets/Nanonets-OCR-s

### Notes

API: http://localhost:2024

Docs: http://localhost:2024/docs

LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

https://github.com/langchain-ai/langgraph-studio

https://langchain-ai.github.io/langgraph/cloud/how-tos/studio/quick_start/

https://github.com/langchain-ai/langgraph

https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/#specify-dependencies

https://langchain-ai.github.io/langgraph/reference/supervisor/

https://langchain-ai.github.io/langgraph/reference/agents/

https://langchain-ai.github.io/langgraph/reference/graphs/

https://langchain-ai.github.io/langgraph/cloud/reference/cli/

https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/#specify-environment-variables

https://docs.smith.langchain.com/

https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/
