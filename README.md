# Groq-Powered Multi-Agent AI Assistant

## Overview

A Python-based multi-agent application that uses the Groq API
to process user queries through three specialized agents.

## Architecture

User Query
    |
    v
Triage Agent
    |
    v
Research Agent
    |
    v
Response Agent
    |
    v
Final Answer

## Agents

### 1. Triage Agent
Classifies incoming queries into:
- technical
- research
- coding
- general

### 2. Research Agent
Uses a Groq-hosted language model to generate a draft answer.

### 3. Response Agent
Refines the draft into a clear and readable final response.

## Technology Stack

- Python
- Groq API
- Qwen language model
- python-dotenv

## Project Structure

multi-agent-discovery-demo/
├── agents/
│   ├── __init__.py
│   ├── triage_agent.py
│   ├── research_agent.py
│   └── response_agent.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## Setup

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file containing:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_working_groq_model_id
```

Replace the placeholders with your own values.

### 4. Run the application

```bash
python main.py
```

## Security

Never commit API keys or other secrets to source control.

## Purpose

This project is a learning demonstration of a sequential
multi-agent workflow and GitHub-based asset discovery.