import os
import json

def load_json_data(folder_path):
    """Load all JSON files from a folder into a list."""
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                data.append(json.load(file))
    return data

if __name__ == "__main__":
    json_data_folder = "E:\Website\debt-collection-analysis\data"  # Update with your dataset folder path
    all_data = load_json_data(json_data_folder)
    print(f"Loaded {len(all_data)} JSON files.")
