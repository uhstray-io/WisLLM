FROM langchain/langgraph-api:latest

# Custom dependencies for external model servers
RUN pip install vllm httpx aiohttp tenacity

# Add application code
ADD . /deps/multi-agent
WORKDIR /deps/multi-agent

# Install agent packages
RUN pip install -e .

# Configure graphs
ENV LANGSERVE_GRAPHS="{
"supervisor": "./agents/supervisor/graph.py:supervisor_graph",
"research": "./agents/research_agent/graph.py:research_graph",
"analysis": "./agents/data_analyst/graph.py:analysis_graph"
}"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000