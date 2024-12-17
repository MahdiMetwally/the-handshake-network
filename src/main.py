from image_processing.handshake_detection import detect_handshake, recognize_celebrities #, analyze_image_with_Gvision
from database.database_manager import create_network, add_handshake, get_network
from visualization.graph_visualizer import visualize_network
from utils.image_fetcher import search_images, download_image, clear_data_directory

added_celebs = []  # list to store added celebrities

def main():
    # Step 1: Input the initial celebrity's name
    celebrity_name = input("Enter the celebrity's name: ")
    
    # Step 2: Create an empty network graph
    graph = create_network()
    
    # Add the first celebrity to the set and the graph
    added_celebs.append(celebrity_name)
    
    # Function to process handshake-related images for a celebrity
    def process_images_for_celebrity(celebrity):
        print("searching links for: ", celebrity)
        try:
            # Search for handshake-related images
            image_urls = search_images(f"{celebrity} shaking hands")
            if not image_urls:
                print(f"No images found for {celebrity}.")
                return
        except Exception as e:
            print(f"Error during image search for {celebrity}: {e}")
            return
        
        # Download and paddrocess images
        for i, url in enumerate(image_urls):
            image_path = f"data/celebrity_image_{i}.jpg"
            try:
                # Download the image
                download_image(url, image_path)
                
                # Detect handshake and recognize other celebrities
                other_celeb = recognize_celebrities(image_path, celebrity)
                if other_celeb and other_celeb not in added_celebs:
                    print(f"Detected new celebrity: {other_celeb} in image {image_path}")
                    added_celebs.append(other_celeb)
                    add_handshake(graph, celebrity, other_celeb)  # Add an edge between the celebrity and detected celeb
                
            except Exception as e:
                print(f"Error processing image {url}: {e}")
    
    # Step 3: Process images for the initial celebrity
    process_images_for_celebrity(celebrity_name)

    # Step 4: Repeat the process for all detected celebrities in added_celebs (without modifying the set during iteration)
    celebrities_to_process = added_celebs  # Make a list of celebrities to iterate over
    for celeb in celebrities_to_process:
        process_images_for_celebrity(celeb)
        if(len(celebrities_to_process) > 30):
            break

    # Step 5: Visualize the handshake network
    print("Handshake network visualization:")
    visualize_network(graph)  # Pass the root celebrity as the root node

    # Display the graph structure
    network_data = get_network(graph)
    print("Handshake network nodes and edges:", network_data)

    # Clear the data directory to clean up
    clear_data_directory("data/")

if __name__ == "__main__":
    main()
