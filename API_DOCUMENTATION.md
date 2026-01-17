# API Documentation - TF-IDF Keyword Extraction

## Base URL

```
http://localhost:5000
```

## API Endpoints

### 1. Health Check

Check if the API is running and healthy.

**Endpoint**: `GET /api/health`

**Request**:

```http
GET http://localhost:5000/api/health
```

**Response** (200 OK):

```json
{
  "status": "healthy",
  "message": "TF-IDF Keyword Extraction API is running"
}
```

**Response Fields**:

- `status` (string): Status of the API ("healthy")
- `message` (string): Descriptive message

---

### 2. Extract Keywords

Extract keywords from input text using TF-IDF algorithm.

**Endpoint**: `POST /api/extract-keywords`

**Request Headers**:

```http
Content-Type: application/json
```

**Request Body**:

```json
{
  "text": "Your input text here for keyword extraction",
  "top_n": 10
}
```

**Request Parameters**:

- `text` (string, required): Input text for keyword extraction
- `top_n` (integer, optional): Number of top keywords to extract (default: 10, range: 1-50)

**Example Request**:

```bash
curl -X POST http://localhost:5000/api/extract-keywords \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Machine learning is a subset of artificial intelligence",
    "top_n": 5
  }'
```

**Response** (200 OK):

```json
{
  "keywords": [
    {
      "keyword": "machine",
      "score": 0.523456
    },
    {
      "keyword": "learning",
      "score": 0.489123
    },
    {
      "keyword": "artificial",
      "score": 0.412345
    },
    {
      "keyword": "intelligence",
      "score": 0.398765
    },
    {
      "keyword": "subset",
      "score": 0.345678
    }
  ],
  "count": 5,
  "extraction_time": 0.0234,
  "status": "success"
}
```

**Response Fields**:

- `keywords` (array): List of extracted keywords with scores
  - `keyword` (string): The extracted keyword
  - `score` (float): TF-IDF score (0.0 to 1.0, higher is better)
- `count` (integer): Number of keywords extracted
- `extraction_time` (float): Time taken for extraction in seconds
- `status` (string): Status of the operation ("success")

**Error Response** (400 Bad Request):

```json
{
  "error": "Text input is empty",
  "status": "error"
}
```

**Error Response** (500 Internal Server Error):

```json
{
  "error": "Error message describing what went wrong",
  "status": "error"
}
```

---

## Error Codes

| Status Code | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| 200         | Success - Request processed successfully                     |
| 400         | Bad Request - Invalid input (empty text, invalid parameters) |
| 500         | Internal Server Error - Server-side error during processing  |

---

## Request/Response Examples

### Example 1: Basic Keyword Extraction

**Request**:

```json
{
  "text": "Natural language processing enables computers to understand human language",
  "top_n": 10
}
```

**Response**:

```json
{
  "keywords": [
    { "keyword": "natural", "score": 0.456789 },
    { "keyword": "language", "score": 0.423456 },
    { "keyword": "processing", "score": 0.412345 },
    { "keyword": "computers", "score": 0.389012 },
    { "keyword": "understand", "score": 0.36789 },
    { "keyword": "human", "score": 0.345678 }
  ],
  "count": 6,
  "extraction_time": 0.0189,
  "status": "success"
}
```

### Example 2: Long Text Extraction

**Request**:

```json
{
  "text": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to learn representations of data. It has revolutionized fields such as computer vision, natural language processing, and speech recognition.",
  "top_n": 15
}
```

**Response**:

```json
{
  "keywords": [
    { "keyword": "learning", "score": 0.512345 },
    { "keyword": "neural", "score": 0.489012 },
    { "keyword": "networks", "score": 0.46789 },
    { "keyword": "processing", "score": 0.445678 },
    { "keyword": "recognition", "score": 0.423456 },
    { "keyword": "vision", "score": 0.401234 },
    { "keyword": "revolutionized", "score": 0.378901 },
    { "keyword": "representations", "score": 0.356789 },
    { "keyword": "layers", "score": 0.334567 },
    { "keyword": "subset", "score": 0.312345 }
  ],
  "count": 10,
  "extraction_time": 0.0256,
  "status": "success"
}
```

---

## Rate Limiting

Currently, there is no rate limiting implemented. For production use, consider implementing rate limiting to prevent abuse.

---

## Data Processing

### Preprocessing Steps

The API performs the following preprocessing steps on input text:

1. **Lowercasing**: All text is converted to lowercase
2. **Tokenization**: Text is split into individual words/tokens
3. **Stopword Removal**: Common English stopwords are removed
4. **Lemmatization**: Words are converted to their base/root form

### TF-IDF Calculation

The API uses scikit-learn's `TfidfVectorizer` with the following parameters:

- `max_features`: 1000 (maximum vocabulary size)
- `min_df`: 1 (minimum document frequency)
- `max_df`: 0.95 (maximum document frequency)
- `ngram_range`: (1, 1) (only unigrams/single words)
- `smooth_idf`: True (smooth IDF weights)

---

## Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:5000/api/health

# Extract keywords
curl -X POST http://localhost:5000/api/extract-keywords \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text here", "top_n": 10}'
```

### Using Python

```python
import requests

# Health check
response = requests.get('http://localhost:5000/api/health')
print(response.json())

# Extract keywords
url = 'http://localhost:5000/api/extract-keywords'
data = {
    'text': 'Your text here for keyword extraction',
    'top_n': 10
}
response = requests.post(url, json=data)
print(response.json())
```

### Using JavaScript (Fetch API)

```javascript
// Health check
fetch("http://localhost:5000/api/health")
  .then((response) => response.json())
  .then((data) => console.log(data));

// Extract keywords
fetch("http://localhost:5000/api/extract-keywords", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    text: "Your text here for keyword extraction",
    top_n: 10,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

---

## Notes

- The API accepts text of any length, but very long texts may take longer to process
- The `top_n` parameter is limited to a maximum of 50 keywords
- Keywords are returned in descending order of TF-IDF scores
- All keywords are lowercase and lemmatized
- Stopwords are automatically removed from results

