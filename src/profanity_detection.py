import json
import re
import os

def load_profanity_list():
    """Load a predefined set of profane words."""
    return {"hell", "damn", "shit", "ass"}  # Expand as needed

def detect_profanity_from_folder(folder_path):
    """Detect profanity usage by agents and borrowers across multiple JSON files."""
    agent_calls = set()
    borrower_calls = set()
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    profane_words = load_profanity_list()
                    
                    call_id = None  # Initialize call ID
                    for entry in data:
                        text = entry.get("text", "").lower()
                        speaker = entry.get("speaker", "").strip().lower()
                        call_id = entry.get("call_id", file_name)  # Fallback to file_name if call_id is missing
                        
                        # Detect profanity using regex for full word matching
                        if any(re.search(rf"\b{word}\b", text, re.IGNORECASE) for word in profane_words):
                            if speaker == "agent":
                                agent_calls.add(call_id)
                            elif speaker == "customer":  # Adjusted to match JSON speaker format
                                borrower_calls.add(call_id)

            except json.JSONDecodeError:
                print(f"Skipping corrupted file: {file_name}")
    
    return len(agent_calls), len(borrower_calls)

if __name__ == "__main__":
    folder_path = "E:\Website\debt-collection-analysis\data"  # Update with your actual JSON folder path
    agent_count, borrower_count = detect_profanity_from_folder(folder_path)
    
    print("Number of calls where agents used profane language:", agent_count)
    print("Number of calls where borrowers used profane language:", borrower_count)
