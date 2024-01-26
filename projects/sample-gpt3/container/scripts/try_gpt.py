from app import query_chatgpt

# Example usage
prompt = "Hello, who are you?"
api_key = "barabeem baraboom"  # Replace with your actual API key
response = query_chatgpt(prompt, api_key=api_key)

if __name__ == "__main__":
    print(response["choices"][0]["message"]["content"])
