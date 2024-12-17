import requests
import os

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

def filter_images_by_metadata(search_results, query):
    print("altered query: ", )
    """
    Filters images based on metadata containing the query string (celebrity name)
    and excludes suspicious entries based on specific keywords.
    """
    filtered_results = []
    query_lower = query[:-17].lower()

    for img in search_results.get("value", []):
        # Extract metadata
        name = img.get("name", "").lower()
        description = img.get("hostPageDisplayUrl", "").lower()
        encoding_format = img.get("encodingFormat", "").lower()
        host_page_url = img.get("hostPageUrl", "").lower()

        """""
        # Print out the full metadata for debugging
        print("Image Metadata:")
        print(f"Name: {name}")
        print(f"Description: {description}")
        print(f"Encoding Format: {encoding_format}")
        print(f"Host Page URL: {host_page_url}")
        print("-" * 50)
        """""

        # Check if the celebrity's name is in any part of the metadata
        if query_lower not in name and query_lower not in description and query_lower not in host_page_url:
            continue  # Skip if the celebrity's name is not in the metadata

        # Exclude images with suspicious keywords (e.g., AI-generated or art-based)
        suspicious_keywords = ["ai-generated", "render", "art", "illustration"]
        if any(keyword in name or keyword in description for keyword in suspicious_keywords):
            continue  # Skip if any suspicious keyword is found

        filtered_results.append(img["contentUrl"])

    print(f"Filtered {len(filtered_results)} images matching metadata criteria.")
    return filtered_results


def search_images(query, count=8):
    """
    Searches for images using Bing Image Search API and filters by metadata.
    """
    api_key = "f99bf0f7b11d46d3854af837d50d5895"
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": count}
    
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    
    search_results = response.json()
    #print(f"API returned {len(search_results.get('value', []))} images.")
    return filter_images_by_metadata(search_results, query)

def download_image(url, save_path):
    """
    Downloads an image from a given URL and saves it locally.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        #print(f"Image downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")



def clear_data_directory(directory):
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
        print(f"Directory {directory} cleared successfully.")
    except Exception as e:
        print(f"Error clearing directory {directory}: {e}")

allowed_domains = [
    "gettyimages.com",       # Professional photo repository
    "shutterstock.com",      # Stock image platform
    "istockphoto.com",       # Stock image platform (owned by Getty Images)
    "bbc.com",               # Trusted news outlet
    "cnn.com",               # Trusted news outlet
    "reuters.com",           # Global news agency
    "apnews.com",            # Associated Press
    "nytimes.com",           # The New York Times
    "washingtonpost.com",    # The Washington Post
    "forbes.com",            # Business and celebrity news
    "time.com",              # TIME Magazine
    "theguardian.com",       # The Guardian
    "bloomberg.com",         # Bloomberg News
    "usatoday.com",          # USA Today
    "npr.org",               # National Public Radio
    "abcnews.go.com",        # ABC News
    "cbsnews.com",           # CBS News
    "nbcnews.com",           # NBC News
    "foxnews.com",           # Fox News
    "huffpost.com",          # Huffington Post
    "people.com",            # Celebrity news
    "eonline.com",           # Entertainment news
    "tmz.com",               # Entertainment news
    "rollingstone.com",      # Music and entertainment news
    "vanityfair.com",        # Celebrity and cultural news
    "vogue.com",             # Celebrity and fashion
    "hollywoodreporter.com", # Entertainment industry news
    "variety.com",           # Entertainment industry news
    "yahoo.com",             # Yahoo News
    "msn.com",               # MSN News
    "nbc.com",               # NBC
]