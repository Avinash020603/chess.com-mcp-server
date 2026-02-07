from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Chess.com")

from .chess_api import get_player_profile,get_player_stats,get_player_current_games,get_player_is_online

@mcp.tool()
def get_chess_player_profile(username: str):
    """ Get the public profile for a Chess.com Player by username."""
    return get_player_profile(username)

@mcp.tool()
def get_chess_player_stats(username: str):
    """ Get the stats for a Chess.com Player by username."""
    return get_player_stats(username)

@mcp.tool()
def get_chess_player_current_games(username: str):
    """ Get the current games for a Chess.com Player by username."""
    return get_player_current_games(username)

def main():
    mcp.run(transport="stdio")

if __name__=="__main__":
    main()