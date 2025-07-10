
from vllm import LLM, SamplingParams
import asyncio


# Create a sampling params object.
# sampling_params = SamplingParams(temperature=0.8, top_p=1.0, max_tokens=1024)
# llm = LLM(model="facebook/opt-125m", gpu_memory_utilization=0.5)

print("Loading LLM...")

# sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=32768)
# llm = LLM(model="microsoft/Phi-4-mini-reasoning", gpu_memory_utilization=0.5)

# sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=8192)
# llm = LLM(model="microsoft/Phi-3.5-mini-instruct", gpu_memory_utilization=0.85, max_model_len=3540)

sampling_params = SamplingParams(temperature=0.6, top_p=0.95, max_tokens=8192)
llm = LLM(model="HuggingFaceTB/SmolLM3-3B", gpu_memory_utilization=0.75, max_model_len=14144)

# sampling_params = SamplingParams(temperature=0.7, top_p=0.95, max_tokens=8192)
# llm = LLM(model="google/gemma-3-4b-it", gpu_memory_utilization=0.75, max_model_len=3540)


# sampling_params = SamplingParams(temperature=0.7, top_p=0.80, top_k=20,min_p=0.0, max_tokens=2048)
# llm = LLM(model="Menlo/Jan-nano-128k", gpu_memory_utilization=0.9)

async def main():
    print("LLM Ready!")

    while True:
        i = input("Waht you want foool? Asc yo questin: ")
        if i.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        response_text = await response(i)
        print(f"Response: {response_text[0].outputs[0].text.strip()}")


async def response(prompt):
    outputs = llm.generate(prompt, sampling_params, use_tqdm=False)
    
    return outputs


if __name__ == "__main__":
    asyncio.run(main())
