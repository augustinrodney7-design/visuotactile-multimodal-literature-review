import pandas as pd
import subprocess

def query_ollama(prompt):
result = subprocess.run(
["ollama", "run", "qwen3:8b"],
input=prompt,
text=True,
capture_output=True
)
return result.stdout

df = pd.read_csv("../data/articles_raw.csv")

decisions = []
reasons = []

for index, row in df.iterrows():
prompt = f"""
You are a research assistant.

Task: Decide if the paper is relevant for:
"visuo-tactile multimodal fusion and object property understanding"

Title: {row['Title']}
Abstract: {row['Abstract']}

Answer strictly in this format:
Decision: Include or Exclude
Reason: short explanation
"""

```
response = query_ollama(prompt)

decisions.append(response)
reasons.append(response)
```

df["LLM_Output"] = decisions

df.to_csv("../data/screened_articles.csv", index=False)

print("Screening completed.")

