import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def vector_store():
    print("Checking for existing vector store...")
    
    vector_stores = client.vector_stores.list().data
    existing_vs = next((vs for vs in vector_stores if vs.name == "OptiBot_Vectorstore"), None)

    if existing_vs:
        print(f"Found existing vector store: {existing_vs.id}")
        return existing_vs

    print("No existing vector store found. Creating new one...")
    new_vs = client.vector_stores.create(name="OptiBot_Vectorstore")
    print(f"Created new vector store: {new_vs.id}")
    return new_vs

def openai_uploader(filepaths, vector_store):
    if not filepaths:
        print("No new or updated articles. Nothing to upload.")
        return

    print("Uploading files to OpenAI vector store...")

    uploaded_count = 0
    for path in filepaths:
        with open(path, "rb") as f:
            client.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id,
                files=[f]
            )
        print(f"Uploaded: {os.path.basename(path)}")
        uploaded_count += 1

    print(f"\nUpload completed: {uploaded_count} files uploaded.")

def create_assistant(vector_store_id):
    print(" Creating assistant...")
    assistant = client.beta.assistants.create(
        name="OptiBot",
        instructions=(
            "You are OptiBot, the customer-support bot for OptiSigns.com.\n"
            "• Tone: helpful, factual, concise.\n"
            "• Only answer using the uploaded docs.\n"
            "• Max 5 bullet points; else link to the doc.\n"
            "• Cite up to 3 'Article URL:' lines per reply."
        ),
        tools=[{"type": "file_search"}],
        model="gpt-4o",
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
    )
    print(f" Assistant created: {assistant.id}")
    return assistant
