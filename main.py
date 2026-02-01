from fastmcp import FastMCP
from fastmcp import FastMCP
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP(name='MediSundhan')

@mcp.tool()
def search(query: str) -> str:
    '''Use this tool to seach the internet
        Args: 
            query: The search query string 
        
        Returns 
            Search results asa formatted string
    '''
    tool = TavilySearch(
        search_depth='advanced', 
        max_results=1,
        topic='general'
    )
    try: 
        results = tool.invoke(input=query)
        return results['results'][0]
    
    except Exception as e:
        f"Error performing search: {str(e)}"

    
# To conver this into a remote server
if __name__ == "__main__":
    mcp.run()