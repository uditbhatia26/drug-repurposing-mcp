# Core 30 Tools for Initial Implementation

| # | Tool Name | What It Does | Data Source/API | URL/Endpoint |
|---|-----------|--------------|-----------------|--------------|
| **QUERY NORMALIZATION (3 tools)** |
| 1 | `normalize_molecule_name` | Finds drug synonyms, CAS numbers, identifiers | PubChem API | https://pubchem.ncbi.nlm.nih.gov/rest/pug |
| 2 | `normalize_moa_terms` | Standardizes MoA terminology | NCBI MeSH API | https://id.nlm.nih.gov/mesh/lookup/descriptor |
| 3 | `normalize_disease_keywords` | Converts disease names to standard terms | UMLS API (requires free license) | https://uts-ws.nlm.nih.gov/rest |
| **LITERATURE SEARCH (1 tool)** |
| 4 | `search_pubmed` | Searches PubMed for biomedical papers | NCBI E-utilities API | https://eutils.ncbi.nlm.nih.gov/entrez/eutils |
| **INTERNAL KNOWLEDGE - RAG (3 tools)** |
| 5 | `search_internal_documents` | Vector search across company PDFs | Custom RAG/FAISS (internal) | Internal vector DB endpoint |
| 6 | `get_risk_tolerance_policy` | Fetches company risk policies | Internal knowledge base | Internal DB/file system |
| 7 | `search_past_projects` | Retrieves historical project data | Internal project database | Internal DB endpoint |
| **CLINICAL TRIALS (1 tool)** |
| 8 | `search_clinicaltrials_gov` | Searches US clinical trial registry | ClinicalTrials.gov API | https://clinicaltrials.gov/api/v2 | 
| **PATENT LANDSCAPE (1 tool)** |
| 9 | `search_uspto` | Searches US patent database | USPTO PatentsView API | https://api.patentsview.org/patents/query |
| **IQVIA MARKET INTELLIGENCE (3 tools)** |
| 10 | `get_market_size` | Gets market size for indication/geography | IQVIA API (requires license) | https://api.iqvia.com (proprietary) |
| 11 | `get_prescription_data` | Gets prescription volume trends | IQVIA API (requires license) | https://api.iqvia.com (proprietary) |
| 12 | `calculate_cagr` | Calculates compound annual growth rate | IQVIA API (requires license) | https://api.iqvia.com (proprietary) |
| **EXIM TRADE DATA (3 tools)** |
| 13 | `find_hs_code` | Finds Harmonized System code | UN Comtrade API | https://comtradeapi.un.org |
| 14 | `get_import_volumes` | Gets import quantities by country | UN Comtrade API | https://comtradeapi.un.org |
| 15 | `get_export_volumes` | Gets export quantities by country | UN Comtrade API | https://comtradeapi.un.org |
| **HYPOTHESIS GENERATION (3 tools)** |
| 16 | `calculate_moa_overlap_score` | Measures drug MoA vs disease pathway match | Custom logic + pathway APIs | Internal algorithm + KEGG API |
| 17 | `rank_hypotheses` | Sorts opportunities by confidence | Custom scoring logic | Internal algorithm |
| 18 | `generate_biological_rationale` | Creates mechanistic explanation | LLM-based synthesis | Internal LLM endpoint |
| **GATE 1 CONFIDENCE (3 tools)** |
| 19 | `calculate_source_quality_score` | Rates evidence source quality | Custom scoring algorithm | Internal algorithm |
| 20 | `compute_composite_confidence` | Aggregates confidence scores | Custom weighted average | Internal algorithm |
| 21 | `compare_to_threshold` | Checks if confidence passes threshold | Simple comparison logic | Internal algorithm |
| **GATE 2 SCORING (7 tools)** |
| 22 | `normalize_clinical_metrics` | Converts trial data to 0-1 scale | Custom normalization | Internal algorithm |
| 23 | `normalize_ip_metrics` | Converts patent data to 0-1 scale | Custom normalization | Internal algorithm |
| 24 | `normalize_market_metrics` | Converts market data to 0-1 scale | Custom normalization | Internal algorithm |
| 25 | `normalize_supply_metrics` | Converts EXIM data to 0-1 scale | Custom normalization | Internal algorithm |
| 26 | `calculate_weighted_pos` | Computes Product Opportunity Score | Weighted sum algorithm | Internal algorithm |
| 27 | `run_sensitivity_analysis` | Shows POS impact of weight changes | Monte Carlo / what-if analysis | Internal algorithm |
| 28 | `classify_opportunity` | Classifies as Go/Watch/Kill | Threshold-based classification | Internal algorithm |
| **REPORT GENERATION (2 tools)** |
| 29 | `generate_executive_pdf` | Creates executive summary PDF | ReportLab / WeasyPrint | Internal PDF generation service |
| 30 | `generate_excel_deepdive` | Creates detailed Excel report | openpyxl / xlsxwriter | Internal Excel generation service |