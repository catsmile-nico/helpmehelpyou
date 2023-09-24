\[[Background](#backgrounds)\] \[[llama-cpp](#llama-cpp)\] \[[Prompting](#Prompting)\] \[[Resource](#Resource)\]

# Background

## Understanding LLM
Doesn't work out of the box
- Needs to be guided
  - What should it do
  - What should it not do
- Can be augmented
  - Give it data to 
  - Give it a program to use

Prompting is an iterative process
- What role suits the topic best
- What rules should be set
- How can we input data and help it understand with context
- How the LLM interpret the above

## Configurations

### Temperature

Using high and low temperatures in a chatbot

``User: What is the capital of France?``

__High Temperature (1.0)__  
``Chatbot: The capital of France is Paris, the city of love and lights. It's a beautiful place to visit, with its iconic landmarks like the Eiffel Tower and Louvre Museum. You'll definitely fall in love with the romantic atmosphere!``
- Elaborate and creative
- Adds information about Paris, emphasizing its romantic atmosphere and iconic landmarks (Diverse/Varied and imaginative)

__Low Temperature (0.2)__  
``Chatbot: The capital of France is Paris.``
- Straight forward answer without any additional details or embellishments (Conservative and deterministic)

<br>

# llama-cpp

## CPU only
```bash
pip install llama-cpp-python
```

## CUDA
```bash
# update gpg key
sudo apt-key del 7fa2af80
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64 cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600

# install wsl cuda
# check latest cuda version: https://developer.nvidia.com/cuda-downloads
wget https://developer.download.nvidia.com/compute/cuda/12.2.2/local_installers/cuda-repo-wsl-ubuntu-12-2-local_12.2.2-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-12-2-local_12.2.2-1_amd64.deb
# or 
sudo apt install cuda-repo-wsl-ubuntu-12-2-local_12.2.2-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-12-2-local/cuda-48257546-keyring.gpg /usr/share/keyrings/

# install cuda
sudo apt-get update
sudo apt-get -y install cuda

# check if gpu is detected
nvidia-smi

# install llama-cpp
export CUDA_PATH=/usr/local/cuda/bin
export PATH=/usr/local/cuda/bin:$PATH
export LLAMA_CUBLAS=1
FORCE_CMAKE=1 CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir -vv
```

## Sample code

```python
from llama_cpp import Llama

prompt = """[INST] <<SYS>>
You are a veteran story writer.
<</SYS>>
Tell me a story in less than 100 words. [/INST]"""

llm = Llama(model_path="./models/llama-2-13b-chat.Q5_K_M.gguf", n_ctx=200, n_gpu_layers=20)
output = llm(
    prompt,max_tokens=200,stop=["</s>"],echo=True,
)
print(output)

# check if GPU is being used by running a script with llama-cpp-python with verbose=True
# BLAS = 1
```

<br>

# Prompting

## System / Roleplay
Sets the tone of the response

## Rules / Guidelines
Restrict the LLM's output range.
- Formatting (Bulletpoints? Paragraphing? JSON?)
- Language (Japanese?)
- When you compare differences, only consider the absolute values

## Input
The resource provided to the LLM
- Dataset, Paragraph, Code, Function + Function output

## Context
Providing context to the dataset or tools the LLM have to work with
- Tools (Functions)
- Dataset
  - is a already aggregated
  - Each row adds up to 100%

## Q & A
Providing guidelines as to how the response should be.  
- Dataset example
  - describe the top2 columns for category
  - describe the relation
  - for this analysis, reference the columns ""

<br>

# Resource

## General

Description | URL
--- | ---
Curated list of useful LLM / Analytics / Datascience resources  | https://github.com/underlines/awesome-marketing-datascience/tree/master

## UI

Description | URL
--- | ---
UI to prompt/chat/configure llm | https://github.com/oobabooga/text-generation-webui

## Prompt engineering

Description | URL
--- | --- 
Deeplearning.ai example notebooks | https://github.com/jojoee/chatgpt-prompt-engineering-for-developers

## Libraries

Description | URL
--- | ---
Track openai usage | https://github.com/dav-ell/toktrack/tree/main