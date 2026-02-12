# Embedded Linux System Monitor

A lightweight **system monitoring tool** for embedded Linux devices, built with **FastAPI**.  
It runs a custom agent (`health_agent`) to collect system metrics and exposes them via a REST API.

---

## Features

- ✅ Health check endpoint (`/health`)  
- ✅ Metrics endpoint (`/metrics`) returning JSON data from the agent  
- ✅ Easy to run on embedded Linux devices  
- ✅ Simple integration with monitoring dashboards  
- ✅ Error handling for agent failures and invalid output

---

## Project Structure

embedded-linux-monitor/
├─ main.py # FastAPI app
├─ agent/
│ └─ health_agent # Custom executable/script providing metrics
├─ README.md # This file
├─ .gitignore # Ignored files (Python cache, logs, etc.)
└─ requirements.txt # Python dependencies (if any)


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/embedded-linux-monitor.git
cd embedded-linux-monitor
Ensure Python 3.8+ is installed (or your target version).

Install dependencies (if using requirements.txt):

pip install -r requirements.txt
Make sure the agent executable is present and has execute permissions:

chmod +x agent/health_agent
Usage
Start the FastAPI server (default port 8000):

uvicorn main:app --reload --host 0.0.0.0 --port 8000
Endpoints:

/ → Server status

/health → Health check

/metrics → System metrics from agent

Notes
If port 8000 is in use:

lsof -i :8000
kill -9 <PID>
Logs errors to the console for easy debugging on embedded devices.

Contributing
Fork the repository

Create a feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Description")

Push to the branch (git push origin feature-name)

Open a Pull Request


---
