from image_processing.handshake_detection import detect_handshake
from database.database_manager import create_network, add_handshake, get_network
from visualization.graph_visualizer import visualize_network
#from utils.image_fetcher import search_images, download_image

# Function to handle the entire process
def main():
    celebrity_name = input("Enter the celebrity's name: ")
    image_urls = search_images(f"{celebrity_name} shaking hands")
    
    graph = create_network()
    
    # Download and process images
    #for i, url in enumerate(image_urls):
     #   image_path = f"data/celebrity_image_{i}.jpg"
      #  download_image(url, image_path)
        
        # Detect handshake
       # if detect_handshake(image_path):
        #    print(f"Handshake detected in image {image_path}")
            # Add edges to the graph (placeholder logic)
         #   add_handshake(graph, celebrity_name, f"Person {i}")
    
    # Visualize the network
   # print("Network created:")
    #visualize_network(graph)
    #print("Handshake network nodes:", get_network(graph))

if __name__ == "__main__":
    main()
