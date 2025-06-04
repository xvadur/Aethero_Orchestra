# AETH-ARCHIVUS-001 :: ROLE: Archivus :: GOAL: Memory Management & Introspection Module
"""
AetheroOS Archivus Module
Memory Management, Introspective Logging, and Historical Analysis
"""

from .memory_manager import ArchivusMemoryManager
from .introspection_logger import IntrospectionLogger
from .audit_processor import AuditProcessor

__all__ = [
    "ArchivusMemoryManager",
    "IntrospectionLogger", 
    "AuditProcessor"
]

__version__ = "1.0.0-alpha"
__minister__ = "Archivus"
__authority__ = "Presidential Directive AETH-ORCHESTRA-2025-001"
