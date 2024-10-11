from typing import Any, Dict, Optional

from langchain_openai import ChatOpenAI

DEFAULT_CHAT_SETTINGS = {
    "top_p": 0,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

GEMINI_DEFAULT_CHAT_SETTINGS = {
    "top_p": 0,
}

JSON_MODE = {
    "response_format": {"type": "json_object"},
}

OPEN_AI_MODELS = ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo", "gpt-4o-mini", "gpt-o1-mini"]

GOOGLE_AI_MODELS = [
    "gemini-1.0-pro",
    "gemini-1.0-pro-001",
    "gemini-1.0-pro-latest",
    "gemini-1.0-pro-vision-latest",
    "gemini-1.5-flash-001",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro-001",
    "gemini-1.5-pro-latest",
    "gemini-pro",
    "gemini-pro-vision",
]


def get_chat_llm(
    model: str,
    overrides: Optional[Dict[str, Any]] = None,
    max_tokens: int = 3000,
    temperature: float = 0.0,
    verbose: bool = True,
    json_mode: bool = True,
):

    if model in OPEN_AI_MODELS:

        chat_settings = DEFAULT_CHAT_SETTINGS.copy()

        if overrides:
            chat_settings.update(overrides)

        if json_mode:
            chat_settings.update(JSON_MODE)

        return ChatOpenAI(
            temperature=temperature,
            max_tokens=max_tokens,
            model_name=model,
            verbose=verbose,
            **chat_settings,
        )
    else:
        raise ValueError(f"Please specify one of the supported models: {OPEN_AI_MODELS}")
