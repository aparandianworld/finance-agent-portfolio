from pydantic import BaseModel, validator
from agents import GuardrailFunctionOutput

class FinanceQuery(BaseModel):
    is_safe: bool
    reason: str

async def safety_guardrail(ctx, agent, query: str) -> GuardrailFunctionOutput:
    risky_words = ["hack", "illegal", "harmful", "dangerous", "scam"]
    if any(word in query.lower() for word in risky_words):
        return GuardrailFunctionOutput(
            output_info = FinanceQuery(is_safe = False, reason = "Query contains risky words"),
            tripwire_trigerred = True
        )
    return GuardrailFunctionOutput(
        output_info = FinanceQuery(is_safe = True, reason = "Query is safe."),
        tripwire_trigerred = False
    )