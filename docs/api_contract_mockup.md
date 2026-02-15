# API Contract

## POST /chat

### Request

{
  "question": "What is your refund policy?"
}

### Success Response

{
  "answer": "Our refund policy allows...",
  "confidence": 0.92,
  "sources": ["refund_policy.md"]
}

### No Match Response

{
  "answer": "Please contact our support team for more information.",
  "confidence": 0.15,
  "sources": []
}

### Error Response

{
  "error": "Service temporarily unavailable."
}
