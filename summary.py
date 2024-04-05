import json
# Use a pipeline as a high-level helper
from transformers import pipeline
from transformers import logging
logging.set_verbosity_error()

def summarize():
    # Open the JSON file in read mode
    with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\text.json", "r") as file:
        # Load the JSON data
        data = json.load(file)

    # # Access the data from the JSON file
    # print(data)
    final_text = data["text"]
    # print(result)


    pipe1 = pipeline("token-classification", model="dslim/bert-large-NER", aggregation_strategy='simple',)

    pipe2 = pipeline("token-classification", model="Clinical-AI-Apollo/Medical-NER", aggregation_strategy='simple')

    text = final_text

    result1 = pipe1(text)

    result2 = pipe2(text)

    result1.extend(result2)

    new_list = []
    for item in result1:
        dict1 = {item["entity_group"]:item["word"]}
        # print(dict1)
        new_list.append(dict1)

    with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\summary.json","w") as file:
        json.dump(new_list,file)

    print("Summarized")

summarize()
# column1 = []
# for row in result:
#     for i in row.keys():
#         column1.append(i)

# column2 = []
# for row1 in result:
#     for j in row1.values():
#         column2.append(j)

# for key,value in zip(column1,column2):
#     print(key," ",value)


