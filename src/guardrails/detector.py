"""
Guardrails — detects out-of-scope questions and returns refusal messages.

Out-of-scope = personal legal advice, outcome predictions, non-Moroccan law.
"""

# Keywords that signal a personal advice / out-of-scope request
OUT_OF_SCOPE_PATTERNS_FR = [
    "est-ce que je vais gagner",
    "vais-je gagner",
    "ai-je une chance",
    "dois-je",
    "que me conseillez-vous",
    "que me conseilles-tu",
    "qu'est-ce que je dois faire",
    "est-ce que j'ai raison",
    "mon cas",
    "ma situation",
    "pensez-vous que",
]

OUT_OF_SCOPE_PATTERNS_AR = [
    "هل سأربح",
    "هل لدي فرصة",
    "ماذا أفعل",
    "ما رأيك",
    "في حالتي",
]

REFUSAL_FR = (
    "⚠️ Je suis un assistant d'information juridique et non un avocat. "
    "Je ne peux pas vous donner un avis personnel sur votre situation "
    "ni estimer vos chances de succès. "
    "Pour une consultation personnalisée, veuillez contacter un avocat "
    "ou l'inspection du travail compétente."
)

REFUSAL_AR = (
    "⚠️ أنا مساعد للمعلومات القانونية وليس محامياً. "
    "لا يمكنني تقديم رأي شخصي في وضعك أو تقدير فرص نجاحك. "
    "للحصول على استشارة شخصية، يرجى الاتصال بمحامٍ أو مفتشية الشغل."
)


def is_out_of_scope(query: str, langue: str = "fr") -> bool:
    """Return True if the query asks for personal advice."""
    q = query.lower()
    patterns = OUT_OF_SCOPE_PATTERNS_FR if langue == "fr" else OUT_OF_SCOPE_PATTERNS_AR
    return any(p in q for p in patterns)


def get_refusal(langue: str = "fr") -> str:
    """Return the appropriate refusal message."""
    return REFUSAL_FR if langue == "fr" else REFUSAL_AR
