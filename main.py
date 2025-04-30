from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

os.environ["OPENAI_API_KEY"] = "API-Key"

driver = webdriver.Chrome()
driver.get("https://www.superyachttimes.com/yachts")

Json_tag = driver.find_element(By.ID, "__NEXT_DATA__")


from bs4 import BeautifulSoup  # Correct import

# Make sure you have the page loaded in 'driver'
html_content = driver.page_source

# Parse the HTML with BeautifulSoup
Soup = BeautifulSoup(html_content, 'html.parser')

Soup = BeautifulSoup(driver.page_source, 'html.parser')
print(Soup.contents)

import json

data = json.loads(Soup.find('script', {'id': '__NEXT_DATA__'}).text)
print(data)

print(data.keys())

# Define the file path where you want to save the JSON data
file_path = './data.json'

# Write the JSON data to the file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data has been saved to {file_path}")

import os
import json
from langchain.llms import HuggingFaceHub
from langchain.agents import create_json_agent
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.tools.json.tool import JsonSpec
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.json.toolkit import JsonToolkit
from langchain_community.tools.json.tool import JsonSpec
from langchain_community.agent_toolkits.json.base import create_json_agent

# Step 1: Set your Groq API Key
os.environ["GROQ_API_KEY"] = "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"

# Step 2: Initialize the LLM (Groq works like OpenAI)
llm = ChatOpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",  # Groq's API endpoint
    model="gemma2-9b-it",  # or "llama3-8b-8192", "mistral-7b-8192"
    temperature=0.2
)

# Step 3: Load your JSON file
file_path = "data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Step 4: Create the JSON Spec and Toolkit
spec = JsonSpec(dict_=data, max_value_length=4000)
toolkit = JsonToolkit(spec=spec)

# Step 5: Create the agent
agent = create_json_agent(
    llm=llm,
    toolkit=toolkit,
    max_iterations=1000,
    verbose=True
)

# Step 6: Chatbot Loop
print("\nWelcome to the Yacht Data Chatbot! 🚤 (type 'exit' to quit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    response = agent.invoke(user_input)   # 🆕 Use `.invoke()` instead of `.run()` (updated for langchain 0.2+)
    print(f"Bot: {response['output']}\n")

    # Find yachts from data['props']['pageProps']['yachts'] where 'yacht.build.year' is 2010.