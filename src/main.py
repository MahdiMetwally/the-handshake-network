from image_processing.handshake_detection import detect_handshake
from database.database_manager import create_network, add_handshake, get_network
from visualization.graph_visualizer import visualize_network
from utils.image_fetcher import search_images,download_image,clear_data_directory # Uncommented to use image fetcher

def main():
    # Step 1: Input celebrity's name
    celebrity_name = input("Enter the celebrity's name: ")
    
    # Step 2: Search for handshake-related images
    try:
        image_urls = search_images(f"{celebrity_name} shaking hands")
        if not image_urls:
            print("No images found for the search term.")
            return
    except Exception as e:
        print(f"Error during image search: {e}")
        return
    
    # Step 3: Create an empty network graph
    graph = create_network()
    
    # Step 4: Download and process images
    for i, url in enumerate(image_urls):
        image_path = f"data/celebrity_image_{i}.jpg"
        try:
            # Download the image
            download_image(url, image_path)
            
            # Detect handshake in the image
            if detect_handshake(image_path):
                print(f"Handshake detected in image {image_path}")
                # Add an edge to the graph (e.g., between the celebrity and an unnamed person)
                add_handshake(graph, celebrity_name, f"Person {i + 1}")
        except Exception as e:
            print(f"Error processing image {url}: {e}")
    
    # Step 5: Visualize the handshake network
    print("Handshake network visualization:")
    visualize_network(graph)
    
    # Display the graph structure
    network_data = get_network(graph)
    print("Handshake network nodes and edges:", network_data)

clear_data_directory("data/")

if __name__ == "__main__":
    main()

