# AETH-BRIDGE-001 :: AetheroOS Integration Bridges
# Minister: Multi-ministerial coordination bridge
# Goal: Connect AetheroOS ministers with Superagent framework

"""
AetheroOS Integration Bridges Module

This module provides the bridge layer between AetheroOS ministerial cabinet
and the underlying Superagent framework infrastructure.

Bridge Components:
- parser_bridge: ASL syntax parsing integration  
- cognitive_bridge: Cognitive processing pipeline
- server_bridge: FastAPI/WebSocket server integration
- memory_bridge: Vector storage and retrieval
- gradio_bridge: Frontend interface coordination

Constitutional Framework: Each bridge operates under AetheroOS protocols
while maintaining compatibility with Superagent's infrastructure.
"""

from typing import Dict, Any, Optional
import logging

# Configure bridge logging
logger = logging.getLogger("aethero.bridges")

__version__ = "1.0.0"
__author__ = "AetheroOS Cabinet"
__constitutional_compliance__ = "AETH-CONST-2025-001"

# Import all bridge instances
from .parser_bridge import parser_bridge
from .cognitive_bridge import cognitive_bridge  
from .server_bridge import server_bridge
from .memory_bridge import memory_bridge
from .gradio_bridge import gradio_bridge
from .bridge_coordinator import bridge_coordinator

# Bridge registry for ministerial coordination
BRIDGE_REGISTRY: Dict[str, Any] = {
    "parser": parser_bridge,
    "cognitive": cognitive_bridge, 
    "server": server_bridge,
    "memory": memory_bridge,
    "gradio": gradio_bridge,
    "coordinator": bridge_coordinator
}

def register_bridge(bridge_name: str, bridge_instance: Any) -> bool:
    """Register a bridge instance in the AetheroOS bridge registry"""
    try:
        BRIDGE_REGISTRY[bridge_name] = bridge_instance
        logger.info(f"[BRIDGE-REGISTER] {bridge_name} bridge registered successfully")
        return True
    except Exception as e:
        logger.error(f"[BRIDGE-ERROR] Failed to register {bridge_name}: {e}")
        return False

def get_bridge(bridge_name: str) -> Optional[Any]:
    """Retrieve a registered bridge instance"""
    return BRIDGE_REGISTRY.get(bridge_name)

def get_all_bridges() -> Dict[str, Any]:
    """Get all registered bridge instances"""
    return BRIDGE_REGISTRY.copy()

def get_coordinator():
    """Get the bridge coordinator instance"""
    return bridge_coordinator

# Auto-register all bridges on import
def _auto_register_bridges():
    """Automatically register all bridge instances"""
    bridges_to_register = [
        ("parser", parser_bridge),
        ("cognitive", cognitive_bridge),
        ("server", server_bridge), 
        ("memory", memory_bridge),
        ("gradio", gradio_bridge),
        ("coordinator", bridge_coordinator)
    ]
    
    for bridge_name, bridge_instance in bridges_to_register:
        if bridge_name not in BRIDGE_REGISTRY or BRIDGE_REGISTRY[bridge_name] is None:
            register_bridge(bridge_name, bridge_instance)
    
    logger.info("[BRIDGE-AUTO-REGISTER] All bridges auto-registered")

# Auto-register on module import
_auto_register_bridges()
