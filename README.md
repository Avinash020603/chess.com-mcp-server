<b>Chess.com MCP Server
A Model Context Protocol (MCP) server that integrates with the Chess.com Public API. This server allows AI agents (like Claude Desktop) to fetch real-time player profiles, game statistics, and current active games directly from Chess.com.

Features
-Player Profiles: Fetch public data including avatar, country, and join date.

-Detailed Stats: Access ratings for Blitz, Bullet, Rapid, and Daily chess.

-Active Games: Retrieve a list of games the player is currently participating in.

-Seamless Integration: Designed to work with the uv package manager for fast, isolated execution.

<b>Prerequisites
a.Python 3.10+
b.uv package manager installed.
c.Claude Desktop (or any other MCP-compatible host).

Installation & Setup
1. Clone the Repository

git clone https://github.com/your-username/MCP-build-chess-stats.git
cd MCP-build-chess-stats

2. Configure Your Contact Info
Chess.com requires a User-Agent with contact information to avoid 403 Forbidden errors. Open src/chess/chess_api.py and update the headers:

headers = {
    "User-Agent": "MCP-Chess-Stats-Bot/1.0 (your-email@example.com)"
}

3. Add to Claude Desktop
Add the following configuration to your claude_desktop_config.json (typically found in %AppData%\Claude\ on Windows):

JSON
{
  "mcpServers": {
    "Chess.com": {
      "command": "uv",
      "args": [
        "--directory",
        "D:/MCP/MCP-build-chess-stats",
        "run",
        "chess"
      ]
    }
  }
}

Note: Ensure the path matches the location where you cloned the repository.