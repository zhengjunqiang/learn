from voluptuous import Required,Schema,MultipleInvalid

schema = Schema({
      'q': str,
      Required('per_page'): int,
      'page': int,
})

data = { 
 "q": "hello world", 
 "per_page":1,
 "page": 10
}

try:
    schema(data)
    print("yes")
except MultipleInvalid as e:
    print(e.errors)