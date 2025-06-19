# 🧠 Text Summarization Tool

This is a simple Python-based **text summarization tool** that uses **Natural Language Processing (NLP)** techniques to shorten lengthy articles while preserving their key meaning. It was developed as part of **CODTECH Internship Task-1**.

---

## 📌 Overview

The tool takes long paragraphs or articles as input and returns a concise summary using extractive text summarization methods. It’s a command-line Python script — easy to use, lightweight, and great for educational or demo purposes.

---

## 🚀 Features

- ✂️ Summarizes large bodies of text
- 🧠 Uses NLP techniques for extractive summarization
- 📄 Reads input from a `.txt` file
- 💬 Outputs original and summarized content in the terminal
- ⚙️ Minimal setup required

---

## 🛠️ Tech Stack

- **Language**: Python
- **Library**: `gensim==3.8.3` (for summarization) or alternative like `sumy`
- **Input Format**: Plain text (`.txt`)
- **Output**: Console-based display of original and summarized text

---

## 📁 Project Structure

```

text\_summarizer/
├── summarizer.py          # Main script
├── input.txt              # Sample input article
└── requirements.txt       # Dependency list

````

---

## 🧪 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text_summarizer.git
   cd text_summarizer
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your article in `input.txt`.

4. Run the script:

   ```bash
   python summarizer.py
   ```

---

## 📝 Sample Output

```
Original Text:
Artificial Intelligence (AI) is the simulation of human intelligence processes...

Summary:
AI is the simulation of human intelligence. It helps in diagnosing diseases, fraud detection, self-driving vehicles...
```

---

## 📦 Requirements

* Python 3.6–3.10
* Recommended libraries:

  * `gensim==3.8.3` (only if compatible)
  * or use `sumy` as an alternative
