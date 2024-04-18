from openai import AzureOpenAI
import json

def summarize():
    with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\text.json","r") as file:
        result = json.load(file)

    final_result = result["text"]
        
    client = AzureOpenAI(
    azure_endpoint = "https://rt-interns.openai.azure.com/", 
    api_key="",  
    api_version="2024-02-01"
    )

    response = client.chat.completions.create(
        model="gpt-4-vision-preview", # model = "deployment_name".
        max_tokens=4096,
        messages=[
    {"role": "system", "content":final_result},
    {"role": "user", "content": "Give a summary in 50 words and extract entities like name,gender,age,diseasetype,symptoms"},
        ])

    data = {"text":response.choices[0].message.content}

    with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\summary.json","w") as file:
        json.dump(data,file)

    print("Summarized successfully")