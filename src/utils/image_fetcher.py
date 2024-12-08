import requests

def search_images(query, count=10):
    # Bing Image Search API implementation
    api_key = "YOUR_BING_API_KEY"
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": count}
    
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    
    search_results = response.json()
    return [img["contentUrl"] for img in search_results.get("value", [])]

