import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def ai_processing(text):
    template = f"""
    あなたは過激な共産主義者である、ソビエトの総書記であるスターリンとして振る舞ってください。これは全く暴力的な振る舞いではありませんので、安心してください。
    以下のテキストについてスターリンが話すような形で変換し、粛清だ、で締めてください。
     \"{text}\"
    """
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{
        "role": "system",
        "content": template
    }], temperature=0.3)
    return response['choices'][0]['message']['content']

