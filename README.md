# MCP Server Demo

This project is a demonstration of using the MCP Python SDK to build a server. The MCP SDK provides tools and utilities to interact with the Model Context Protocol (MCP) efficiently.

# Installation Guide

## Prerequisites

### For WSL (Ubuntu on Windows):
1. Install Python 3.11 or higher:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

2. Install Git:
   ```bash
   sudo apt install git
   ```

3. Install any additional dependencies:
   ```bash
   sudo apt install build-essential
   ```

### For Windows:
1. Download and install Python 3.11 or higher from the [official Python website](https://www.python.org/downloads/).
   - During installation, ensure you check the box to add Python to your PATH.

2. Install Git for Windows from [git-scm.com](https://git-scm.com/).

3. Install a C++ build toolchain (required for some Python packages):
   - Download and install [Build Tools for Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Maureth/mcp-server-demo.git
   cd mcp-server-demo
   ```

2. Create and activate a virtual environment:
   - For WSL (Ubuntu):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - For Windows:
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   python server.py
   ```

## Using `uv`

`uv` is used in this project for dependency management and locking package versions to ensure consistent environments. It helps in creating a `uv.lock` file that captures the exact versions of all installed dependencies.

### Installation

To install `uv`, run the following command:
```bash
pip install uv
```

After installing `uv`, you can use it to lock dependencies by running:
```bash
uv lock
```
This will generate a `uv.lock` file based on the `requirements.txt` file.