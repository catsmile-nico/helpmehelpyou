# Background

## Understanding LLM
- Doesn't work out of the box
  - Needs to be guided
    - What should it do
    - What should it not do
  - Can be augmented
    - Give it data to 
    - Give it a program to use
- Prompting is an iterative process
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

---

# Prompting breakdown
System / Roleplay
- Set the tone of the response

Rules
- Formatting (Bulletpoints? Paragraphing? JSON?)
- Language (Japanese?)

Input
- Dataset, Paragraph, Code, Function + Function output

Context
- Tools (Functions)
- Dataset
  - is a already aggregated
  - Each row adds up to 100%

Question
- Providing guidelines as to how the response should be
  - Dataset
    - describe the top2 columns for category

---

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