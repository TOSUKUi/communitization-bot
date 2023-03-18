import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def ai_processing(text):
    template = f"You are very radical communist. Please convert this text \"{text}\" to what Stalin who is general secretary of soviet talking and translate to japanese. Finnaly you must put what stalin talking only."
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{
        "role": "system",
        "content": template
    }])
    return response['choices'][0]['message']['content']

