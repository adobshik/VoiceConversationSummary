import pandas as pd
import openai

class SummarizationInference:
    def __init__(self, args):
        openai.api_key = args['api_key']
    
    def summarize_to_soap(self, dialogue):
        # Concatenate dialogue into one string
        combined_dialogue = ' '.join(dialogue)
        
        # Create a prompt for the summarization
        prompt = (f"Summarize the following dialogue in SOAP format:\n"
                  f"{combined_dialogue}\n\n"
                  "SOAP Format:\n"
                  "Subjective: reason for appointment, chief complaint\n"
                  "Objective: findings from radiographs or any other tests, medical history updates\n"
                  "Assessment: summary of findings\n"
                  "Plan: completed treatment, home care instruction, and next steps")
        
        # Call the ChatGPT API to summarize the text
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()
    
    def predict(self, df_speech):
        # Combine the dialogue lines into a list
        dialogue = df_speech['text'].tolist()
        
        # Get the SOAP summary
        soap_summary = self.summarize_to_soap(dialogue)

        return soap_summary
