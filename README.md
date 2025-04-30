# 🛥️ Yacht QnA Chatbot using GROQ API and Selenium Web Scraping

This project is an intelligent Question-and-Answer chatbot that utilizes a powerful open-source LLM (via GROQ API) to answer questions about superyachts. The chatbot reads structured JSON data (scraped and parsed from a live website using Selenium), enabling it to provide relevant and dynamic responses.

## 🔧 Features

- Scrapes yacht data from [superyachttimes.com](https://www.superyachttimes.com/yachts) using **Selenium**
- Extracts and parses React-based JSON data embedded in the website via **BeautifulSoup**
- Saves the structured data locally as `data.json`
- Uses **GROQ's LLM (e.g., Gemma, LLaMA 3, Mistral)** via `langchain` integration
- Builds a fully functional command-line QnA chatbot that interprets and responds using structured JSON
- Supports iterative conversations via the Langchain JSON Agent toolkit

## 🛠️ Installation

Make sure you have Python 3.8+ installed. Then install the required packages:

```bash
pip install selenium beautifulsoup4 langchain langchain-community langchain-openai
