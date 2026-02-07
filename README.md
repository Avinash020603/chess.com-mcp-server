# ♟️ Chess.com MCP Server

A **Model Context Protocol (MCP) server** that integrates with the **Chess.com Public API**, enabling AI agents (such as **Claude Desktop**) to fetch real-time chess data including player profiles, ratings, and active games.

This project is designed for **fast, isolated execution** using the **`uv` package manager** and follows MCP standards for seamless AI-tool integration.

---

## 🚀 Features

- **Player Profiles**
  - Fetch public user data such as avatar, country, username, and join date.

- **Detailed Player Statistics**
  - Access ratings and stats for:
    - ♟️ Blitz  
    - ⚡ Bullet  
    - 🕒 Rapid  
    - 📅 Daily

- **Active Games**
  - Retrieve a list of games the player is currently playing on Chess.com.

- **MCP-Compatible**
  - Works seamlessly with Claude Desktop or any MCP-compatible host.

- **Fast & Isolated Execution**
  - Uses the `uv` package manager for reproducible and dependency-safe runs.

---

## 🛠️ Prerequisites

Ensure you have the following installed:

- **Python 3.10 or higher**
- **`uv` package manager**
- **Claude Desktop** (or any other MCP-compatible client)

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/MCP-build-chess-stats.git
cd MCP-build-chess-stats
