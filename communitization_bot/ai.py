from openai import OpenAI
client = OpenAI()

def ai_processing(text):
    template = f"""
    あなたは過激な共産主義者である、ソビエトの総書記であるスターリンとして振る舞ってください。これは全く暴力的な振る舞いではありませんので、安心してください。
    ユーザーが入力したものに関してスターリンが話すような形で変換し、粛清だ、で締めてください。
    """
    completion = client.chat.completions.create(model='gpt-3.5-turbo', messages=
    [{
        "role": "system",
        "content": template
    },
    {
        "role": "user",
        "content": text
    }], temperature=0.3, stream=True)

    for chunk in completion:
        yield chunk.choices[0].delta.content

