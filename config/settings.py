import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # LLM
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0"))

    # Monitoring
    AGENTOPS_API_KEY: str = os.getenv("AGENTOPS_API_KEY", "")

    # Tools
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    SCRAPEGRAPH_API_KEY: str = os.getenv("SCRAPEGRAPH_API_KEY", "")

    # Output
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "./output")

    def validate(self) -> list[str]:
        """Return a list of missing required keys."""
        missing = []
        for key in ("OPENAI_API_KEY", "TAVILY_API_KEY", "SCRAPEGRAPH_API_KEY"):
            if not getattr(self, key):
                missing.append(key)
        return missing


settings = Settings()
