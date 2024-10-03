# Importing Libraries
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["api_keys"]["OPENAI_API_KEY"])

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
vector_store_id = os.getenv("VECTOR_STORE_ID")
file_ids = [
    os.getenv("FILE_ID1"),
    os.getenv("FILE_ID2"),
    os.getenv("FILE_ID3"),
    os.getenv("FILE_ID4"),
    os.getenv("FILE_ID5")
]

# Ensure all file IDs are retrieved correctly
if None in file_ids:
    raise ValueError("One or more file IDs are missing in the environment variables")

# List vector stores
vector_stores = client.beta.vector_stores.list()

print(vector_stores)

my_assistants = client.beta.assistants.list(
    order="desc",
    limit="20",
)
print(my_assistants.data)

# Print environment variables to verify
print(f"API Key: {OpenAI.api_key}")
print(f"Vector Store ID: {vector_store_id}")
print(f"File IDs: {file_ids}")

# Create a vector store file batch (Adjust the method as per OpenAI API documentation)
vector_store_file_batch = client.beta.vector_stores.file_batches.create(
    vector_store_id=vector_store_id,
    file_ids=file_ids
)

print(vector_store_file_batch)
