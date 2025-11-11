import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# Initialize the FastAPI app
app = FastAPI()

# Initialize the OpenAI client
# It will automatically pick up the OPENAI_API_KEY environment variable
# OPENAI_API_KEY="paste-your-api-key-here"

try:
    client = OpenAI(api_key=OPENAI_API_KEY)
except ImportError:
    print("OpenAI library not found. Please install with 'pip install openai'")
    exit()
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    # You might want to exit or handle this error differently
    # For now, we'll let it proceed but API calls will fail.
    client = None

# Define the request model using Pydantic
# This ensures the incoming data has a 'prompt' field as a string
class ChatRequest(BaseModel):
    prompt: str

# Define the response model using Pydantic
class ChatResponse(BaseModel):
    response: str

# Define the '/chat' endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat_with_llm(request_body: ChatRequest):
    """
    Receives a user prompt, sends it to the OpenAI API,
    and returns the model's response.
    """
    if not client:
        return {"response": "OpenAI client not initialized."}
        
    try:
        # Create the chat completion request
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # A popular and capable model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request_body.prompt}
            ]
        )
        
        # Extract the response text
        response_text = completion.choices[0].message.content
        
        # Return the response in the specified format
        return ChatResponse(response=response_text)
        
    except Exception as e:
        # Handle potential errors (e.g., API downtime, invalid key)
        return ChatResponse(response=f"An error occurred: {str(e)}")

# Define a simple root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "LLM Chatbot API is running!"}