import openai


def ask_chatgpt(question: str) -> str:
    answers = []
    model = "gpt-3.5-turbo"
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": question }
        ])
    for answer in completion.choices:
        answers.append(answer["message"]["content"])

    return answers

def lambda_handler(event, context):
    name = event['name']
    event_holiday = event['event']
    language = ['language']

    question = create_question(name, event_holiday, language)
    answer = ask_chatgpt(question)
    return answer

def create_question(name:str, event:str, language:str) -> str:
    """
    Example holidays
    1. Birthdays
    2. Namedays
    3. Easter
    4. Christmas
    5. Women day
    6. Grandma day
    7. Mothers day
    8. Fathers day
    """
    question = f'Write 3 example {event} wishes for {name} in {language} language.'

    return question
