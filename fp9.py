# Imports
import tkinter as tk
import openai
from dotenv import load_dotenv
import os

# Load API key 
load_dotenv()
api_key = os.getenv("key")
openai.api_key = api_key

# Chat completion
def generateCompletion():
    userPrompt = promptEntry.get("1.0", tk.END).strip()
    if userPrompt:
        try:
            completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": userPrompt},
                ]
            )
            # Extract and display the result
            result = completion.choices[0].message.content.strip()
            outputText.delete("1.0", tk.END)
            outputText.insert(tk.END, result)
        # Error handling
        except Exception as e:
            outputText.delete("1.0", tk.END)
            outputText.insert(tk.END, f"Error: {e}")
    else:
        outputText.delete("1.0", tk.END)
        outputText.insert(tk.END, "Please enter a prompt.")

# Set up tkinter
root = tk.Tk()
root.title("OpenAI Chat GUI")
root.resizable(False, False)

# Input box
promptLabel = tk.Label(root, text="Enter your prompt:")
promptLabel.pack()
promptEntry = tk.Text(root, height=5, width=50)
promptEntry.pack()

# Submit button
submitButton = tk.Button(root, text="Submit", command=generateCompletion)
submitButton.pack()

# Output box
outputLabel = tk.Label(root, text="Output:")
outputLabel.pack()
outputText = tk.Text(root, height=10, width=50)
outputText.pack()

root.mainloop()