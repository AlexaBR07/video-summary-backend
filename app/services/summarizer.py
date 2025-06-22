from transformers import pipeline

# Carga modelo una sola vez
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    if len(text) < 100:
        return "Texto demasiado corto para resumir."
    
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]["summary_text"] + " "
    return summary.strip()
