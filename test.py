from handlers import llm, messages

messages.append(("human", "Бабушка, как приготовить макароны?"))
response = llm.invoke(messages)

if response and response.content.strip():
    print("Кибер-бабушка отвечает:", response.content)
else:
    print("Ошибка: модель вернула пустой ответ.")
