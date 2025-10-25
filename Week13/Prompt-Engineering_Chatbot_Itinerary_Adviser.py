from google import genai
from google.genai import types
import os

# Your Google Gemini API key
GEMINI_API_KEY = "AIzaSyCXFko0MdTkWGg-h8OkVx1k2S7mzR47bNM"

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot using Google Gemini."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    
    # Construct prompt
    prompt = f"""
You are a professional tourist recommender. Provide an itinerary recommendation based on user data.

User Details:
- days: {days} days
- destination: {location} city
- Age: {age} years

Based on this information, give a structured itinerary with:
- Name of the place
- Address
- Short description

Organize by day with a maximum of three activities per day.
"""
    
    try:
        # Initialize Gemini client
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Generate content using Gemini
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=1000,
            )
        )
        
        print("\n🌍 My Name is Hadi, your AI Itinerary expert:\n")
        print(response.text)
        
    except Exception as e:
        print(f"❌ Error communicating with Gemini API: {e}")

if __name__ == "__main__":
    instructor_chatbot()