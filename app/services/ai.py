import os
import httpx

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "allenai/molmo-2-8b:free")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "allenai/molmo-2-8b")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_APP_NAME = os.getenv("OPENROUTER_APP_NAME", "CvSummarizerApp")
OPENROUTER_SITE_URL = os.getenv("OPENROUTER_SITE_URL", "http://localhost:8000")

async def generate_cv_resume(filename: str, contenttype: str, location: str) -> str:
    prompt = f"Resume moi le cv {filename} de type {contenttype} qui se trouve à cette endroit en {location}."
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    json_data = {
        "model": OPENROUTER_MODEL,
        "input": prompt,
        "max_output_tokens": 150
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{OPENROUTER_BASE_URL}/responses", headers=headers, json=json_data)
        response.raise_for_status()
        data = response.json()
        return data.get("output_text", "Pas de résumé généré")
