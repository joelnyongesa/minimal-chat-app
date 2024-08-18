# Minimal Chat Application

This is a simple Chat App API created on top of OPENAI API.

## How to get started

To contribute or have a local working version of this project, follow the steps below:

1. Fork and clone the project
2. Navigate to the project's directory using your terminal
3. Run `pipenv install && pipenv shell` at the root of the project directory to install the necessary libraries
4. Run `flask run` to have the app running on port 5000.

## API Endpoints Available

### 1. Chat

This is the endpoint for sending and receiving messages to and from the OPENAI API.

```http
POST /chat
```

| Parameters | Type | Description |
| :--- | :--- | :--- |
| `question` | `string` | *Required*: The question to be sent to the API |
| 404 | `NOT FOUND` |

### Responses

```javascript
{
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "created": 1677858242,
    "model": "gpt-3.5-turbo",
    "usage": {
        "prompt_tokens": 13,
        "completion_tokens": 7,
        "total_tokens": 20
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "\n\nThe response goes here."
            },
            "logprobs": null,
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
```

### Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 404 | `NOT FOUND` |


## Contributors

1. Joel Nyongesa