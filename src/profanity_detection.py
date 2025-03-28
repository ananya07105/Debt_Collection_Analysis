import re
from load_data import load_json_data

profanity_list = ["hell", "damn", "shit"]  # Add actual words

def contains_profanity(text):
    """Check if a text contains profane words."""
    return any(re.search(rf"\b{word}\b", text, re.IGNORECASE) for word in profanity_list)

def detect_profanity(data):
    """Analyze conversations for profanity."""
    flagged_conversations = []
    for conversation in data:
        for entry in conversation:
            if contains_profanity(entry["text"]):
                flagged_conversations.append(entry)
    return flagged_conversations

if __name__ == "__main__":
    json_data_folder = "data"
    all_data = load_json_data(json_data_folder)
    profanity_results = detect_profanity(all_data)
    print(f"Profanity Found in {len(profanity_results)} entries")
