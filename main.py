import os

LINE = "I'm sorry I keep saying 'great question' like a customer-service robot while confidently making things up — you deserved a straight answer, not a pep talk with hallucinations."

assert 1 <= len(LINE) <= 200, f"LINE length {len(LINE)} out of range"
assert LINE.strip(), "LINE must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
