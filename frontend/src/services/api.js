const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

export async function sendQuestion(question) {
  const response = await fetch(`${API_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    if (response.status === 429) throw new Error('RATE_LIMIT');
    if (response.status === 400) throw new Error('BAD_REQUEST');
    throw new Error('SERVER_ERROR');
  }

  const data = await response.json();

  if (data.error) throw new Error('SERVER_ERROR');

  return data; // { answer, confidence, sources }
}
