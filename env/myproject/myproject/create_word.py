import os
from openai import Client
# from openai import OpenAI

# client = Client(api_key=os.getenv('OPENAI_API_KEY'))
client = Client(api_key="sk-" )

def generate_related_words(course_name, lesson_name, grade):
    # Combine inputs into a prompt for the API
    prompt = f"The course is about {course_name}. The lesson is {lesson_name}. The grade is {grade}. Generate ten new single words with length not over 16 characters related to this context:"

    # Use the GPT model to generate text based on the prompt
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None
    )

    # Extract generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Extract words from the generated text
    words = generated_text.split()

    ten_words = [word for word in words if isinstance(word, str) and not any(char.isdigit() for char in word)]

    new_words = [word.upper() for word in ten_words]
    
    return new_words


