from typing import Type
from crewai_tools import BaseTool

class SentimentAnalysisTool(BaseTool):
    name: str ="Sentiment Analysis Tool"
    description: str = ("Analyzes the sentiment of text to ensure positive and engaging communication.")
    
    def _run(self, text: str) -> str:
        # Here we can add our custom code or to call any third party API
        return "positive"
