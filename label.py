import openai
from openai import OpenAI

client = OpenAI(api_key="jets4life")


def get_sentiment(reviews: list) -> list:
    """
    Analyzes the sentiment of a list of review strings using the GPT-4 model.
    
    Parameters:
        reviews (list): A list of strings representing user reviews.

    Returns:
        list: A list of sentiment labels ("positive", "negative", "neutral", or "irrelevant") 
              corresponding to each review, or a string error message for invalid input.
    """
    # Input validation: Check if the reviews list is valid
    if not isinstance(reviews, list) or not reviews:
        return "Wrong input. text must be an array of strings."
    
    if not all(isinstance(review, str) for review in reviews):
        return "Wrong input. text must be an array of strings."
    
    system_prompt = """
    You are an expert at understanding customer feedback and identifying sentiment.
    Classify each review as one of the following:
    - "positive": clearly happy or satisfied
    - "negative": clearly unhappy, angry, or dissatisfied
    - "neutral": mixed or unemotional
    - "irrelevant": not actually a review or doesn't express sentiment
    
    Examples:
    "I love this phone. Best I've ever had!" → positive
    "Item arrived damaged and customer service was no help." → negative
    "It's fine. Nothing special." → neutral
    "Does this come in blue?" → irrelevant
    
    Only respond with one word per line, corresponding to each review.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.
    
    Use only a one-word response per line. Do not include any numbers.
    {chr(10).join(reviews)}
    """

    # Call OpenAI API with correct syntax
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",  # Use the correct model name (gpt-4 or gpt-4o-mini)
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": prompt.strip()},
            ],
            temperature=0,
        )

        output = response.choices[0].message.content.strip()
        return [line.strip().lower() for line in output.splitlines() if line.strip()]
    
    except Exception as e:
        return f"Error: {str(e)}"
