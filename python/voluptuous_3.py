from voluptuous import Url,Schema,MultipleInvalid
schema = Schema(Url())

try:
    schema('https://www.baidu.com/')
    #raise AssertionError('MultipleInvalid not raised')
except MultipleInvalid as e:
    print(e.errors)