"""
Canonical data models for LogExplain.

These models define the official structure of every
LogExplain knowledge base entry.

The knowledge base is the single source of truth.
Renderers decide how the content is presented.
"""

from typing import List

from pydantic import BaseModel, Field


# ============================================================================
# Metadata
# ============================================================================


class EventInformation(BaseModel):
    """Basic metadata describing a security event."""

    event_id: int
    event_name: str
    platform: str
    log: str
    event_provider: str
    category: str
    audit_type: str
    introduced: str


# ============================================================================
# Educational Sections
# ============================================================================


class MarkdownSection(BaseModel):
    """
    A complete educational section.

    The content is stored exactly as written in the
    Markdown knowledge base.
    """

    title: str
    content: str


# ============================================================================
# Structured Sections
# ============================================================================


class InvestigationChecklist(BaseModel):
    """Investigation checklist."""

    items: List[str] = Field(default_factory=list)


class RelatedEvent(BaseModel):
    """A related Windows Security Event."""

    event_id: int
    event_name: str
    relationship: str


class LearningResource(BaseModel):
    """External learning resource."""

    title: str
    description: str
    url: str | None = None


class ContinueYourJourney(BaseModel):
    """Recommended next event."""

    event_id: int
    event_name: str
    reason: str


# ============================================================================
# Canonical Event Model
# ============================================================================


class LogExplainEvent(BaseModel):
    """
    Canonical representation of a LogExplain knowledge base entry.
    """

    information: EventInformation

    event_summary: MarkdownSection

    understanding_the_event: MarkdownSection

    context_matters: MarkdownSection

    investigation_guide: MarkdownSection

    investigation_checklist: InvestigationChecklist

    think_like_an_analyst: MarkdownSection

    real_world_relevance: MarkdownSection

    related_events: List[RelatedEvent] = Field(default_factory=list)

    continue_learning: List[LearningResource] = Field(default_factory=list)

    key_takeaways: List[str] = Field(default_factory=list)

    learning_reflection: MarkdownSection

    continue_your_journey: ContinueYourJourney | None = None
