from __future__ import annotations

import os
from typing import Optional

from openai import OpenAI


class OpenAIService:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.enabled = bool(self.api_key)
        self.client = OpenAI(api_key=self.api_key) if self.enabled else None

    async def summarize(self, text: str, system_prompt: Optional[str] = None) -> str:
        if not self.enabled or self.client is None:
            return text[:800]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt or "You are a concise operational assistant for a Whatnot business."},
                {"role": "user", "content": text},
            ],
            temperature=0.2,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
