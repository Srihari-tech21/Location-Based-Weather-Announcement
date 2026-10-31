from nlp_processor import process_query


print("======================================")
print("  NLP WEATHER QUERY TEST")
print("======================================")

query = input("\nEnter your weather question: ").strip()

if query:
    result = process_query(query)

    print("\nDetected words:", result["tokens"])
    print("Detected city:", result["city"])
    print("Detected intent:", result["intent"])
else:
    print("Please enter a question.")