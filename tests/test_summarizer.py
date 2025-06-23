from app.services.summarizer import summarize_text

def test_summarize_text_short():
    result = summarize_text("Hola")
    assert result == "Texto demasiado corto para resumir."

def test_summarize_text_long():
    long_text = "Esto es un texto muy largo " * 100
    summary = summarize_text(long_text)
    assert isinstance(summary, str)
    assert len(summary) > 0
