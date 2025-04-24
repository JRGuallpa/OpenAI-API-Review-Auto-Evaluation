import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> None:
    """
    Creates a bar chart showing the frequency of each sentiment label 
    in the given list of sentiments. The chart is saved as an image 
    file in the 'images/' directory.

    Parameters:
        sentiments (list): A list of sentiment strings. Expected values:
                           'positive', 'neutral', 'negative', 'irrelevant'.
    
    Returns:
        None
    """
    # Initialize counters for each sentiment type
    positive_count = 0
    neutral_count = 0
    negative_count = 0
    irrelevant_count = 0

    # Count the occurrences of each sentiment
    for sentiment in sentiments:
        if sentiment == "positive":
            positive_count += 1
        elif sentiment == "neutral":
            neutral_count += 1
        elif sentiment == "negative":
            negative_count += 1
        elif sentiment == "irrelevant":
            irrelevant_count += 1

    # Prepare the data for plotting
    categories = ["positive", "neutral", "negative", "irrelevant"]
    frequencies = [positive_count, neutral_count, negative_count, irrelevant_count]

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, frequencies, color=["green", "gray", "red", "blue"])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Frequency")

    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, int(yval), ha="center", va="bottom")

    # Save the plot in the 'images/' directory (manually ensure it exists beforehand)
    plt.savefig("images/sentiment_image.png")
    plt.close()
