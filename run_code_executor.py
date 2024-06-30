import requests

# Setup a new environment
response = requests.post("http://localhost:8085/setup")
env_id = response.json()["env_id"]
print(f"Environment created with ID: {env_id}")

# Execute code in the environment
code = """
a = 10
b = 20
c = a + b
print(f"The sum of {a} and {b} is {c}")
"""
payload = {"env_id": env_id, "code": code}
response = requests.post("http://localhost:8085/execute", json=payload)
output = response.json()["output"]
print(f"Code execution output:\n{output}")

# Get code history
response = requests.get(f"http://localhost:8085/code_history/{env_id}")
code_history = response.json()["code_history"]
print(f"Code history:\n{code_history}")

# Execute another code snippet
code = """
def multiply(x, y):
    return x * y

result = multiply(5, c)
print(f"The result of multiplication 5 * {c} is {result}")
"""
payload = {"env_id": env_id, "code": code}
response = requests.post("http://localhost:8085/execute", json=payload)
output = response.json()["output"]
print(f"Code execution output:\n{output}")

# Shutdown the environment
payload = {"env_id": env_id}
response = requests.post("http://localhost:8085/shutdown", json=payload)
message = response.json()["message"]
print(message)