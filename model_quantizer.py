from transformers import AutoModelForCausalLM, AutoTokenizer
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier

# Load model
model = AutoModelForCausalLM.from_pretrained("Menlo/Jan-nano-128k")
tokenizer = AutoTokenizer.from_pretrained("Menlo/Jan-nano-128k")

# Apply compression - this also wraps save_pretrained
oneshot(
    model=model,
    recipe=[GPTQModifier(targets="Linear", scheme="W8A8", ignore=["lm_head"])],
    # Other oneshot parameters...
)

# Now you can use the enhanced save_pretrained
SAVE_DIR = "Jan-nano-128k-W8A8-compressed"
model.save_pretrained(
    SAVE_DIR,
    save_compressed=True  # Use the enhanced functionality
)
tokenizer.save_pretrained(SAVE_DIR)