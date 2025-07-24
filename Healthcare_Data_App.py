# /app/main.py
from app.sparql_client import query_neptune
from app.llm_interface import translate_to_sparql

def main():
    nl_query = input("Enter a natural language query: ")
    sparql_query = translate_to_sparql(nl_query)
    print("Generated SPARQL query:")
    print(sparql_query)

    results = query_neptune(sparql_query)
    print("\nQuery Results:")
    print(results)

if __name__ == "__main__":
    main()


# /app/sparql_client.py
import requests

def query_neptune(sparql_query: str) -> dict:
    endpoint = "https://your-neptune-endpoint:8182/sparql"
    headers = {"Accept": "application/sparql-results+json"}
    params = {"query": sparql_query}

    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"SPARQL query failed: {response.status_code} {response.text}")
    return response.json()


# /app/llm_interface.py
import boto3

def translate_to_sparql(nl_query: str) -> str:
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    prompt = f"Convert this medical natural language query into SPARQL: {nl_query}"

    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        body={"prompt": prompt, "max_tokens_to_sample": 300},
        contentType="application/json",
        accept="application/json"
    )

    return response['body'].read().decode()


# /app/summarizer.py
# Future implementation placeholder
def summarize_notes(notes: str) -> str:
    return "(Summarization model not yet implemented)"


# /tests/test_sparql_client.py
def test_query_neptune():
    try:
        result = query_neptune("SELECT * WHERE {?s ?p ?o} LIMIT 1")
        assert "results" in result
    except Exception as e:
        assert False, f"Query failed: {e}"


# /tests/test_llm_interface.py
def test_translate_to_sparql():
    sparql = translate_to_sparql("Find patients with high blood pressure")
    assert "SELECT" in sparql or "CONSTRUCT" in sparql

