import requests
import os


# Ensure the data directory exists
os.makedirs("data", exist_ok=True)


def search_images(query, count=10):
    # Bing Image Search API implementation
    api_key = "f99bf0f7b11d46d3854af837d50d5895"
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": count}
    
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    
    search_results = response.json()
    return [img["contentUrl"] for img in search_results.get("value", [])]

def download_image(url, save_path):
    # Downloads an image from a given URL and saves it locally
    try:
        response = requests.get(url, stream=True)  # Stream the content for large files
        response.raise_for_status()
        
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):  # Write in chunks to avoid memory issues
                file.write(chunk)
        #print(f"Image downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def clear_data_directory(directory):
    # Deletes all files and subdirectories in the specified directory
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Removes subdirectories
            else:
                os.remove(file_path)  # Removes files
        print(f"Directory {directory} cleared successfully.")
    except Exception as e:
        print(f"Error clearing directory {directory}: {e}")