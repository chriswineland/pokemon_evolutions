import json

def safe_get(data: json, key: str):
    return None if not key in data else data[key]