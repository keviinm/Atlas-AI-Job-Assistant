import os

from crewai_tools import FileReadTool, ScrapeWebsiteTool, MDXSearchTool, SerperDevTool


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESUME_PATH = os.path.join(BASE_DIR, "data", "fake_resume.md")


# Debugging: Print the path to verify it's correct
print(f"🔍 Looking for resume at: {RESUME_PATH}")

if not os.path.exists(RESUME_PATH):
    raise FileNotFoundError(f"⚠️ The file {RESUME_PATH} was not found. Please check the path.")


class CrewTools:
    """Initializes CrewAI tools."""
    def __init__(self):
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        self.read_resume = FileReadTool(file_path=RESUME_PATH)
        self.semantic_search_resume = MDXSearchTool(mdx=RESUME_PATH)