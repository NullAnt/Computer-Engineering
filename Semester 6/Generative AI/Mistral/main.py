# from huggingface_hub import snapshot_download
# from pathlib import Path

# mistral_models_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
# mistral_models_path.mkdir(parents=True, exist_ok=True)

# snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "mistralai/Mistral-7B-v0.1"  # or -Instruct-v0.2/v0.3

tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, use_auth_token=True)
model.to("cuda")

inputs = tokenizer("Hello world, I'm Mistral!", return_tensors="pt").to("cuda")
out = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(out[0], skip_special_tokens=True))
