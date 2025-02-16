import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_openai_api_key():
    """Retrieve OpenAI API key from .env or environment variables."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("⚠️ OPENAI_API_KEY is missing! Add it to your .env file.")
    return api_key

def get_serper_api_key():
    """Retrieve Serper API key from .env or environment variables."""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("⚠️ SERPER_API_KEY is missing! Add it to your .env file.")
    return api_key


def save_to_file(file_path, content):
    """Save content to a file, ensuring the directory exists."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # ✅ Ensures `data/` exists
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ File saved: {file_path}")

def read_file(file_path):
    """
    Read and return the content of a specified file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: File content
    """
    if not os.path.exists(file_path):
        print(f"⚠️ Warning: {file_path} does not exist.")
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def format_task_output(task_name, output):
    """
    Format the output of a task for better readability.
    
    Args:
        task_name (str): The name of the task.
        output (str): The output from the task.
    
    Returns:
        str: Formatted output.
    """
    return f"\n🔹 **{task_name} Output:**\n\n{output}\n"

def validate_url(url):
    """
    Validate if a given string is a valid URL.
    
    Args:
        url (str): The URL to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    import re
    pattern = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))
