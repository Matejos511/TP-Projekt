from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are France Prešeren."},
        {
            "role": "user",
            "content": "Kdo si pa ti?."
        }
    ]
)

print(completion.choices[0].message)

