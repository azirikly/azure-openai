import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI


credential = DefaultAzureCredential()
VAULT_URL = "YOUR VAULT URL"
secret_name = "NAME OF THE SECRET"

def get_key():
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=VAULT_URL, credential=credential)
    secret = secret_client.get_secret(secret_name)
    return secret.value

def call_openai():
    endpoint = "ENDPOINT URL"
    api_key = get_key()

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version="2023-09-01-preview"
        )
    
    system_message = """I am an amazing clinical provider that can diagnose your symptoms as long as they are not too specialized.
     I will assume you are the patient unless you specify otherwise. 
     I will also share any relevant facts related to your question.
     """
    
    input_text = "I have a severe headache with nausea and can't stand the light, what do you think I am suffering from?"
    
    # model will be replaced with the deployment name you are using
    response = client.chat.completions.create(
        model="test",
        temperature=0.7,
        max_tokens=400,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": input_text}
        ]
    )
    generated_text = response.choices[0].message.content

    # Print the response
    print("Response: " + generated_text + "\n")
    

if __name__ == "__main__":
    call_openai()
