import json
from label import get_sentiment
from visualize import make_plot

def run(file_path: str) -> list:
    """
    This function runs the entire pipeline: loading the review data from the JSON file,
    calling the get_sentiment function to analyze sentiments, and optionally generating
    sentiment distribution visualizations.

    Parameters:
        file_path (str): The path to the JSON file containing the reviews.

    Returns:
        list: A list of sentiment labels (e.g., ["positive", "negative", "neutral", ...]).
    """
    # Step 1: Load the JSON file containing reviews
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load the JSON data
            reviews = data.get("results", []) 
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {file_path}.")
        return []
    
    # Step 2: Get sentiment analysis results using the get_sentiment function
    sentiments = get_sentiment(reviews)

    # Step 3: Optionally, generate sentiment distribution visualization (save to 'images/' folder)
    if sentiments and isinstance(sentiments, list):
        make_plot(sentiments)  # You can choose to skip this if you don't want to plot
    else:
        print("No valid sentiments generated. Skipping plot creation.")

    # Step 4: Return the sentiment labels
    return sentiments
