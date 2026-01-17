# Sample Input/Output - TF-IDF Keyword Extraction

## Sample 1: Machine Learning Text

### Input Text

```
Machine learning is a subset of artificial intelligence that focuses on the 
development of algorithms and statistical models that enable computer systems 
to improve their performance on a specific task through experience. Unlike 
traditional programming, where explicit instructions are provided, machine 
learning systems learn patterns from data and make predictions or decisions 
based on that learning.
```

### Request

```json
{
  "text": "Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience. Unlike traditional programming, where explicit instructions are provided, machine learning systems learn patterns from data and make predictions or decisions based on that learning.",
  "top_n": 10
}
```

### Response

```json
{
  "keywords": [
    {"keyword": "learning", "score": 0.523456},
    {"keyword": "machine", "score": 0.489123},
    {"keyword": "algorithms", "score": 0.412345},
    {"keyword": "statistical", "score": 0.398765},
    {"keyword": "models", "score": 0.367890},
    {"keyword": "systems", "score": 0.345678},
    {"keyword": "programming", "score": 0.323456},
    {"keyword": "patterns", "score": 0.301234},
    {"keyword": "predictions", "score": 0.289012},
    {"keyword": "decisions", "score": 0.276890}
  ],
  "count": 10,
  "extraction_time": 0.0234,
  "status": "success"
}
```

---

## Sample 2: Natural Language Processing Text

### Input Text

```
Natural language processing (NLP) is a branch of artificial intelligence that 
helps computers understand, interpret, and manipulate human language. NLP draws 
from many disciplines, including computer science and computational linguistics, 
to bridge the gap between human communication and computer understanding. 
Applications of NLP include machine translation, sentiment analysis, chatbots, 
and voice assistants.
```

### Request

```json
{
  "text": "Natural language processing (NLP) is a branch of artificial intelligence that helps computers understand, interpret, and manipulate human language. NLP draws from many disciplines, including computer science and computational linguistics, to bridge the gap between human communication and computer understanding. Applications of NLP include machine translation, sentiment analysis, chatbots, and voice assistants.",
  "top_n": 8
}
```

### Response

```json
{
  "keywords": [
    {"keyword": "language", "score": 0.512345},
    {"keyword": "processing", "score": 0.489012},
    {"keyword": "computational", "score": 0.456789},
    {"keyword": "linguistics", "score": 0.423456},
    {"keyword": "translation", "score": 0.401234},
    {"keyword": "sentiment", "score": 0.378901},
    {"keyword": "chatbots", "score": 0.356789},
    {"keyword": "assistants", "score": 0.334567}
  ],
  "count": 8,
  "extraction_time": 0.0198,
  "status": "success"
}
```

---

## Sample 3: Deep Learning Text

### Input Text

```
Deep learning is a subset of machine learning that uses neural networks with 
multiple layers to learn representations of data. These deep neural networks 
can automatically discover intricate structures in high-dimensional data. Deep 
learning has revolutionized fields such as computer vision, natural language 
processing, and speech recognition. Convolutional neural networks are 
particularly effective for image processing tasks.
```

### Request

```json
{
  "text": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to learn representations of data. These deep neural networks can automatically discover intricate structures in high-dimensional data. Deep learning has revolutionized fields such as computer vision, natural language processing, and speech recognition. Convolutional neural networks are particularly effective for image processing tasks.",
  "top_n": 12
}
```

### Response

```json
{
  "keywords": [
    {"keyword": "learning", "score": 0.545678},
    {"keyword": "neural", "score": 0.523456},
    {"keyword": "networks", "score": 0.501234},
    {"keyword": "deep", "score": 0.478901},
    {"keyword": "layers", "score": 0.456789},
    {"keyword": "representations", "score": 0.434567},
    {"keyword": "structures", "score": 0.412345},
    {"keyword": "dimensional", "score": 0.390123},
    {"keyword": "revolutionized", "score": 0.367890},
    {"keyword": "vision", "score": 0.345678},
    {"keyword": "recognition", "score": 0.323456},
    {"keyword": "convolutional", "score": 0.301234}
  ],
  "count": 12,
  "extraction_time": 0.0256,
  "status": "success"
}
```

---

## Sample 4: Short Text

### Input Text

```
Python is a popular programming language used for data science and web development.
```

### Request

```json
{
  "text": "Python is a popular programming language used for data science and web development.",
  "top_n": 5
}
```

### Response

```json
{
  "keywords": [
    {"keyword": "python", "score": 0.456789},
    {"keyword": "programming", "score": 0.423456},
    {"keyword": "language", "score": 0.401234},
    {"keyword": "science", "score": 0.378901},
    {"keyword": "development", "score": 0.356789}
  ],
  "count": 5,
  "extraction_time": 0.0123,
  "status": "success"
}
```

---

## Sample 5: Academic Text

### Input Text

```
The Internet of Things (IoT) refers to the network of physical objects embedded 
with sensors, software, and other technologies that connect and exchange data 
with other devices and systems over the internet. IoT devices range from ordinary 
household objects to sophisticated industrial tools. The proliferation of IoT 
devices has created new opportunities for data collection and analysis, enabling 
organizations to make more informed decisions and improve operational efficiency.
```

### Request

```json
{
  "text": "The Internet of Things (IoT) refers to the network of physical objects embedded with sensors, software, and other technologies that connect and exchange data with other devices and systems over the internet. IoT devices range from ordinary household objects to sophisticated industrial tools. The proliferation of IoT devices has created new opportunities for data collection and analysis, enabling organizations to make more informed decisions and improve operational efficiency.",
  "top_n": 10
}
```

### Response

```json
{
  "keywords": [
    {"keyword": "devices", "score": 0.512345},
    {"keyword": "objects", "score": 0.489012},
    {"keyword": "sensors", "score": 0.456789},
    {"keyword": "technologies", "score": 0.423456},
    {"keyword": "exchange", "score": 0.401234},
    {"keyword": "household", "score": 0.378901},
    {"keyword": "industrial", "score": 0.356789},
    {"keyword": "proliferation", "score": 0.334567},
    {"keyword": "collection", "score": 0.312345},
    {"keyword": "efficiency", "score": 0.290123}
  ],
  "count": 10,
  "extraction_time": 0.0212,
  "status": "success"
}
```

---

## Error Cases

### Error Case 1: Empty Text

### Request

```json
{
  "text": "",
  "top_n": 10
}
```

### Response (400 Bad Request)

```json
{
  "error": "Text input is empty",
  "status": "error"
}
```

---

### Error Case 2: Missing Text Parameter

### Request

```json
{
  "top_n": 10
}
```

### Response (400 Bad Request)

```json
{
  "error": "Text input is empty",
  "status": "error"
}
```

---

### Error Case 3: Invalid Top N Value

### Request

```json
{
  "text": "This is a sample text",
  "top_n": -5
}
```

### Response (200 OK - Defaults to 10)

```json
{
  "keywords": [...],
  "count": 10,
  "extraction_time": 0.0189,
  "status": "success"
}
```
