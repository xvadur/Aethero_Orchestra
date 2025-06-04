# AETH-FRONTINUS-001 :: ROLE: Frontinus :: GOAL: UI/UX & Visualization Management Module
"""
AetheroOS Frontinus Module
Frontend interfaces, real-time visualizations, and user interaction orchestration
"""

from .interface_manager import FrontinusInterfaceManager
from .visualization_engine import VisualizationEngine
from .session_orchestrator import SessionOrchestrator

__all__ = [
    "FrontinusInterfaceManager",
    "VisualizationEngine",
    "SessionOrchestrator"
]

__version__ = "1.0.0-alpha"
__minister__ = "Frontinus"
__authority__ = "Presidential Directive AETH-ORCHESTRA-2025-001"
