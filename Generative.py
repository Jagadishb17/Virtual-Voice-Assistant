import google.generativeai as genai
import os
import warnings

# Filter out all warnings
def GenAi(State):
    warnings.filterwarnings('ignore', category=PendingDeprecationWarning)
    api_key = "AIzaSyDbEuwbJHCqTPgDy27ZM1azCFuLtzfCmJM"

    os.environ['GOOGLE_API_KEY'] = "AIzaSyDbEuwbJHCqTPgDy27ZM1azCFuLtzfCmJM"
    genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

    llm = genai.GenerativeModel('gemini-pro')
    response = llm.generate_content(State)

    return response