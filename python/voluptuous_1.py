import voluptuous

schema = voluptuous.Schema({
    'q': str,
    'per_page': int,
    'page': int,
})

failure_data = { 
    "q": "hello world", 
    "per_page": 1,
    "page": 10
}

try:
    schema(failure_data)
    print("yes")
except voluptuous.MultipleInvalid as e:
    print(e.errors)