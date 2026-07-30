"""
Canonical data models for LogExplain.

These models define the official structure of every
LogExplain knowledge base entry.

Every event is validated against these models before it
can be rendered by the application.
"""

from typing import List

from pydantic import BaseModel, Field


# ============================================================================
# Metadata
# ============================================================================


class EventInformation(BaseModel):
    """Basic metadata describing a security event."""

    event_id: int
    title: str
    platform: str
    category: str
    event_source: str
    common_tags: List[str] = Field(default_factory=list)

    standard_version: str = "1.0"


# ============================================================================
# Educational Sections
# ============================================================================


class UnderstandingTheEvent(BaseModel):
    """Explain what happened and why."""

    what_happened: str

    why_it_happened: str

    common_legitimate_causes: List[str] = Field(default_factory=list)

    possible_security_related_causes: List[str] = Field(default_factory=list)


class ContextMatters(BaseModel):
    """Explain why context determines significance."""

    usually_expected_when: List[str] = Field(default_factory=list)

    worth_investigating_when: List[str] = Field(default_factory=list)

    important_reminder: str


class InvestigationGuide(BaseModel):
    """Describe how an analyst should investigate the event."""

    overview: str

    workflow: List[str] = Field(default_factory=list)


class InvestigationChecklist(BaseModel):
    """Questions an analyst should answer."""

    checklist: List[str] = Field(default_factory=list)


class AnalystMindset(BaseModel):
    """Questions that encourage analytical thinking."""

    questions: List[str] = Field(default_factory=list)


class RealWorldRelevance(BaseModel):
    """Where and why this event matters."""

    summary: str

    examples: List[str] = Field(default_factory=list)


# ============================================================================
# Relationships
# ============================================================================


class RelatedEvent(BaseModel):
    """A security event related to this event."""

    event_id: int

    title: str

    relationship: str


class LearningResource(BaseModel):
    """A recommended resource for continued learning."""

    title: str

    reason: str

    url: str | None = None


class ContinueYourJourney(BaseModel):
    """Recommended next event to study."""

    event_id: int

    title: str

    reason: str


# ============================================================================
# Canonical Knowledge Base Entry
# ============================================================================


class LogExplainEvent(BaseModel):
    """
    Canonical representation of a LogExplain knowledge base entry.

    Every Markdown knowledge base entry should be parsed,
    validated, and converted into this model.
    """

    information: EventInformation

    event_summary: str

    understanding: UnderstandingTheEvent

    context_matters: ContextMatters

    investigation_guide: InvestigationGuide

    investigation_checklist: InvestigationChecklist

    think_like_an_analyst: AnalystMindset

    real_world_relevance: RealWorldRelevance

    related_events: List[RelatedEvent] = Field(default_factory=list)

    continue_learning: List[LearningResource] = Field(default_factory=list)

    key_takeaways: List[str] = Field(default_factory=list)

    learning_reflection: str

    continue_your_journey: ContinueYourJourney | None = None
