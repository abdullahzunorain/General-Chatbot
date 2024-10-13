import gradio as gr
from groq import Groq
import os

key = os.getenv("groq_api")
client = Groq(api_key = key)

def chat(message, history):


  chat_completion = client.chat.completions.create(
      #
      # Required parameters
      #
      messages=[
          {
              "role": "system",
              "content": "you are a helpful assistant."
          },
          # Set a user message for the assistant to respond to.
          {
              "role": "user",
              "content": message,
          }
      ],

      # The language model which will generate the completion.
      model="llama3-8b-8192",
      temperature=0.5,

      max_tokens=256,

      top_p=1,

      stop=None,
      stream=False,
  )

  return chat_completion.choices[0].message.content

demo = gr.ChatInterface(fn=chat, title="Open Source chatbot")
demo.launch(debug= True)
