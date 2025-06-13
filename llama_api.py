import subprocess

def query_llama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "chat", "llama2", "--prompt", prompt],
            capture_output=True,
            text=True,
            timeout=20
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Fehler beim Modellaufruf: {e}"