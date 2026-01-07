# import os
# from pathlib import Path
# from google import genai

# print("=== SCRIPT STARTED ===")

# # Initialize Gemini client with your API key
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# print("Available models for your key:")
# models = client.models.list()
# for m in models:
#     print(m.name)

# SRC_DIR = Path("vb_src")
# OUT_DIR = Path("java_out")
# OUT_DIR.mkdir(exist_ok=True)

# print("VB source dir exists:", SRC_DIR.exists())
# vb_files = list(SRC_DIR.glob("*.vb"))
# print("VB files found:", vb_files)

# def convert_vb_to_java(vb_code: str) -> str:
#     prompt = f"""
# Convert the following VB.NET code line by line into Java.
# Rules:
# - Use standard Java syntax
# - Preserve logic
# - Output ONLY Java code

# VB.NET code:
# {vb_code}
# """

#     # Use a valid Gemini model
#     response = client.models.generate_content(
#         model="models/gemini-pro-latest",
#         contents=prompt
#     )

#     return response.text.strip()

# for vb_file in vb_files:
#     print(f"Processing file: {vb_file}")

#     vb_code = vb_file.read_text(encoding="utf-8")
#     java_code = convert_vb_to_java(vb_code)

#     java_file = OUT_DIR / (vb_file.stem + ".java")
#     java_file.write_text(java_code, encoding="utf-8")

#     print(f"Generated: {java_file}")

# print("=== SCRIPT FINISHED ===")

import os
from pathlib import Path
import openai

print("=== SCRIPT STARTED ===")

# Use your OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

SRC_DIR = Path("vb_src")
OUT_DIR = Path("java_out")
OUT_DIR.mkdir(exist_ok=True)

print("VB source dir exists:", SRC_DIR.exists())
vb_files = list(SRC_DIR.glob("*.vb"))
print("VB files found:", vb_files)



def convert_vb_to_java(vb_code: str) -> str:
    """
    Sends the VB.NET code to OpenAI GPT model to convert it into Java.
    Uses the new OpenAI SDK v1+ interface.
    """
    prompt = f"""
Convert the following VB.NET code line by line into Java.
Rules:
- Use standard Java syntax
- Preserve logic
- Return ONLY Java code, no explanations

VB.NET code:
{vb_code}
"""

    # NEW SDK syntax
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # free/low-cost GPT model
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    java_code = response.choices[0].message.content.strip()
    return java_code



# Process all VB files
for vb_file in vb_files:
    print(f"Processing file: {vb_file}")

    vb_code = vb_file.read_text(encoding="utf-8")
    java_code = convert_vb_to_java(vb_code)

    java_file = OUT_DIR / (vb_file.stem + ".java")
    java_file.write_text(java_code, encoding="utf-8")

    print(f"Generated: {java_file}")

print("=== SCRIPT FINISHED ===")
