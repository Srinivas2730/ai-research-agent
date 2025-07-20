# agent_tools.py

from langchain.tools import tool

@tool
def search_web(query: str) -> str:
    """Pretend to search the web and return dummy content."""
    return f"Search results for '{query}' (placeholder)."

@tool
def read_pdf(file_path: str) -> str:
    """Read and return the text from a PDF file."""
    try:
        import PyPDF2
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    except Exception as e:
        return f"Failed to read PDF: {e}"

tool_executor = [search_web, read_pdf]
