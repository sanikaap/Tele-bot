import requests
import openai
import os
from telegram import Bot
from telegram import BotCommand


# Create a Telegram bot
import telegram


bot = telegram.BotCommand(token ="Enter your token")

# Get the ChatGPT and DALL-E API keys
openai.api_key ="Enter your api key"
dalle_api_key = "Enter your token dalle"

# Create an OpenAI API instance
openai = openai.api_key

# Define a function to generate text with ChatGPT
def generate_text(prompt):
  response = openai.completions.create(
      prompt=prompt,
      max_tokens=100,
      temperature=0.8,
      top_p=0.9,
      best_of=5,
  )
  return response["choices"][0]["text"]

# Define a function to generate images with DALL-E
def generate_image(prompt):
  response = requests.post(
      "https://api.openai.com/v1/dall-e/images",
      headers={"Authorization": f"Bearer {dalle_api_key}"},
      json={"prompt": prompt},
  )
  return response.json()["data"]["image"]

# Handle a message from the user
def handle_message(message):
  if message.text == "/start":
    bot.send_message(message.chat.id, "Welcome to the Infy ChatGPT and DALL-E Telegram bot!")
  elif message.text == "/generate_text":
    prompt = input("Enter a prompt: ")
    text = generate_text(prompt)
    bot.send_message(message.chat.id, text)
  elif message.text == "/generate_image":
    prompt = input("Enter a prompt: ")
    image = generate_image(prompt)
    bot.send_photo(message.chat.id, image)

# Start the bot
while True:
  update = bot.get_updates()
  for message in update["result"]:
    handle_message(message)
