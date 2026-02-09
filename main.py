from fastmcp import FastMCP
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from pydantic import BaseModel, Field 
from typing import Optional, Literal
import requests

load_dotenv()

mcp = FastMCP(name='MediSundhan')

class ClinicalTrialsSearchParams(BaseModel):
    condition: Optional[str] = Field(default=None, description="Medical condition or disease to search for. Free-text value such as 'lung cancer', 'diabetes mellitus', or 'Alzheimer's disease'. This value will be URL-encoded and mapped to the API parameter 'query.cond'.", examples=["lung cancer", "diabetes mellitus", "breast cancer"])
    intervention: Optional[str] = Field(default=None, description="Intervention used in the study, including drugs, procedures, devices, or therapies. Examples include drug names, treatment types, or procedures. This value will be URL-encoded and mapped to 'query.intr'.", examples=["pembrolizumab", "insulin", "radiation therapy"])
    title_keywords: Optional[str] = Field(default=None, description="Keywords to search within the study's brief title, official title, or acronym. Useful for research themes or trial names. This value will be URL-encoded and mapped to 'query.titles'.", examples=["immunotherapy", "HER2", "COVID-19"])
    overall_status: Optional[Literal["RECRUITING", "NOT_YET_RECRUITING", "ACTIVE_NOT_RECRUITING", "COMPLETED", "TERMINATED", "WITHDRAWN", "SUSPENDED"]] = Field(default=None, description="Recruitment status of the clinical trial. Only predefined enum values are allowed. Examples include 'RECRUITING' for ongoing trials and 'COMPLETED' for finished studies. Mapped to the API parameter 'filter.overallStatus'.", examples=["RECRUITING", "COMPLETED"])
    page_size: Optional[int] = Field(default=None, ge=1, le=100, description="Number of studies to return per request. Typical values range from 5 to 100. If not provided, a default of 10 should be used by the caller. Mapped to the API parameter 'pageSize'.", examples=[5, 10, 20])


@mcp.tool()
def search(query: str) -> str:
    '''Use this tool to seach the internet
        Args: 
            query: The search query string 
        
        Returns 
            Search results as a formatted string
    '''
    tool = TavilySearch(
        search_depth='advanced', 
        max_results=1,
        topic='general'
    )
    try: 
        results = tool.invoke(input=query)
        response = results['results'][0]['content']

        return response
    
    except Exception as e:
        return f"Error performing search: {str(e)}"
    

@mcp.tool()
def search_clinicaltrials_gov(query: ClinicalTrialsSearchParams):
    """
    Search ClinicalTrials.gov for clinical trials based on flexible search criteria.
    
    This tool searches the US clinical trials registry. You can search by any combination
    of parameters - ALL parameters are optional. Only provide the parameters that are 
    relevant to your search. For example:
    
    - To find all trials for a drug: only provide 'intervention'
    - To find trials for a disease: only provide 'condition'
    - To find recruiting Phase 3 cancer trials: provide 'condition', 'phase', and 'overall_status'
    
    Do NOT fill in parameters just because they exist. Only use what's needed for the query.
    
    Args:
        query: ClinicalTrialsSearchParams object with the following optional fields:
            - condition: Disease/condition name (optional)
            - intervention: Drug/treatment name (optional)
            - title_keywords: Keywords in study title (optional)
            - overall_status: Recruitment status like RECRUITING, COMPLETED (optional)
            - page_size: Number of results (1-100, default 10) (optional)
            - page_token: Pagination token for next page (optional)
    
    Returns:
        String containing formatted clinical trial results or error message.
        
    Examples:
        - Search for Metformin trials: intervention="Metformin"
        - Search for recruiting diabetes trials: condition="diabetes", overall_status="RECRUITING"
        - Search Phase 3 cancer trials: condition="cancer", phase="PHASE3"
    """
    base_url = "https://clinicaltrials.gov/api/v2/studies?"
    params = {}

    if query.condition is not None:
        params["query.cond"] = query.condition

    if query.intervention is not None:
        params["query.intr"] = query.intervention

    if query.title_keywords is not None:
        params["query.titles"] = query.title_keywords

    if query.overall_status is not None:
        params["filter.overallStatus"] = query.overall_status

    params["pageSize"] = query.page_size if query.page_size is not None else 10
    response = requests.get(base_url, params=params)
    return response.json()['studies']

    
# To conver this into a remote server
if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0', port=8000)