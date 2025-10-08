#!/usr/bin/env python3
import os
import re
from nanda_adapter import NANDA
class Conductor:
    def __init__(self):
        self.intent_patterns = {
            "search": r"(?i)\b(search|google|find|look up|web|browse|best|top)\b",
            "analysis": r"(?i)\b(csv|data|analysis|correlation|statistics)\b",
            "meal_planner": r"(?i)\b(meal|recipe|ingredients|grocery|cook|dinner|food)\b",
        }
        self._greet = re.compile(r"(?i)^(hi|hello|hey|yo)\b")
    def detect_intent(self, text: str) -> str:
        for key in ("analysis", "meal_planner", "search"):
            if re.search(self.intent_patterns[key], text or "", flags=re.IGNORECASE):
                return key
        return "search"
    def handle(self, text: str) -> str:
        if self._greet.search(text or ""):
            return ("Hi! I'm Protean AI Conductor. I can help with web search, data analysis, and meal planning. What do you need?")
        intent = self.detect_intent(text)
        return f"Protean AI detected intent: {intent}. Processing your request: {text}"
conductor = Conductor()
def respond_to_message(message) -> str:
    """Main handler - handles string, dict, or list formats"""
    text = ""
    # Debug
    print(f"DEBUG: Type={type(message)}, Content={str(message)[:200]}")
    # Case 1: Already a string
    if isinstance(message, str):
        text = message
    # Case 2: List (content array from A2A)
    elif isinstance(message, list):
        for item in message:
            if isinstance(item, dict) and 'text' in item:
                text = item['text']
                break
    # Case 3: Dict with 'content' key
    elif isinstance(message, dict):
        content = message.get('content', [])
        if isinstance(content, list) and len(content) > 0:
            text = content[0].get('text', '')
        elif isinstance(content, str):
            text = content
        else:
            text = str(message)
    # Fallback
    if not text:
        text = str(message)
    return conductor.handle(text)
def main():
    nanda = NANDA(respond_to_message)
    domain = os.getenv("DOMAIN_NAME", "api.aoaprotean.net")
    if domain != "localhost":
        nanda.start_server_api(os.getenv("ANTHROPIC_API_KEY"), domain)
    else:
        nanda.run()
if __name__ == "__main__":
    main()
