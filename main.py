from langchain_community.llms.vllm import VLLM
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
import getpass
import os
# import base64

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# client = OpenAI

if "REASONING_LLM" not in os.environ:
    os.environ["REASONING_LLM"] = getpass.getpass(
        prompt="Enter your reasoning LLM path (required): (default = "") "
    )
    if not os.environ.get("REASONING_LLM"):
        os.environ["REASONING_LLM"] = "HF1BitLLM/Llama3-8B-1.58-100B"
        
# if "PREPROCESSING_LLM" not in os.environ:
#     os.environ["PREPROCESSING_LLM"] = getpass.getpass(
#         prompt="Enter your preprocessing LLM path (optional): "
#     )
#     if not os.environ.get("PREPROCESSING_LLM"):
#         os.environ["PREPROCESSING_LLM"] = "nanonets/Nanonets-OCR-s"

# if "CODING_LLM" not in os.environ:
#     os.environ["CODING_LLM"] = getpass.getpass(
#         prompt="Enter your coding LLM path (optional): "
#     )
#     if not os.environ.get("CODING_LLM"):
#         os.environ["CODING_LLM"] = "nvidia/AceReason-Nemotron-1.1-7B"
    
reasoning_llm = VLLM(
    model="REASONING_LLM",
    trust_remote_code=True,
    tensor_parallel_size=3,
    vllm_kwargs={
        "gpu_memory_utilization": 0.9,
        "quantization": "bitblas",  # Enable BitBLAS quantization
        "max_model_len": 4096,
    }
    
)

# preprocessing_llm = VLLM(
#     model="nanonets/Nanonets-OCR-s",
#     trust_remote_code=True,
# )

# coding_llm = VLLM(
#     model="nvidia/AceReason-Nemotron-1.1-7B",
#     trust_remote_code=True,
# )

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

llm_chain = LLMChain(prompt=prompt, llm=reasoning_llm)

question = input("Enter your question: ")

print(llm_chain.invoke(question))