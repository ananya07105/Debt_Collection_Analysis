from load_data import load_json_data

def analyze_call_quality(conversation):
    """Calculate silence and overtalk percentage."""
    if not conversation:
        return {"silence_percentage": 0, "overtalk_percentage": 0}
    
    total_duration = conversation[-1]["etime"] - conversation[0]["stime"]
    if total_duration <= 0:
        return {"silence_percentage": 0, "overtalk_percentage": 0}
    
    silence_duration = sum(
        conversation[i]["stime"] - conversation[i-1]["etime"]
        for i in range(1, len(conversation))
        if conversation[i]["stime"] > conversation[i-1]["etime"]
    )
    
    overtalk_duration = sum(
        min(conversation[i]["etime"], conversation[i-1]["etime"]) - conversation[i]["stime"]
        for i in range(1, len(conversation))
        if conversation[i]["stime"] < conversation[i-1]["etime"]
    )
    
    return {
        "silence_percentage": (silence_duration / total_duration) * 100,
        "overtalk_percentage": (overtalk_duration / total_duration) * 100
    }

if __name__ == "__main__":
    json_data_folder = "data"
    all_data = load_json_data(json_data_folder)
    quality_results = [analyze_call_quality(conv) for conv in all_data if conv]
    print(quality_results)