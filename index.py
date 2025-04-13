data = [{
    "name": "Chicho",
    "age": 25
}, {
    "name": "Rayi",
    "age": 26
}, {
    "name": "Toshi",
    "age": 27
}]

# Lambda function example with age * 2
data = list(map(lambda x: {**x, "age": x["age"] * 2}, data))
print(data)


data.append("Perseo")
print(data)

