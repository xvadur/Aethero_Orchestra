# AETH-BRIDGE-003 :: ROLE: Multi-ministerial :: GOAL: Cognitive Processing Bridge
# Minister: All ministers (cognitive coordination)
# Purpose: Bridge cognitive processing between AetheroOS ministers and Superagent

"""
Cognitive Processing Integration Bridge

Coordinates cognitive processing across AetheroOS ministerial cabinet,
integrating with Superagent's agent reasoning and decision-making pipeline.

Cognitive Flow:
1. Input analysis (Primus)
2. Execution planning (Lucius) 
3. Memory integration (Archivus)
4. Interface adaptation (Frontinus)
"""

import asyncio
import json
import time
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger("aethero.bridges.cognitive")

class CognitiveState(Enum):
    """Cognitive processing states"""
    IDLE = "idle"
    ANALYZING = "analyzing"
    PLANNING = "planning"
    EXECUTING = "executing"
    REMEMBERING = "remembering"
    INTERFACING = "interfacing"
    COMPLETED = "completed"
    ERROR = "error"

class MinisterialRole(Enum):
    """AetheroOS ministerial roles"""
    PRIMUS = "primus"      # Strategic logic
    LUCIUS = "lucius"      # Execution 
    ARCHIVUS = "archivus"  # Memory
    FRONTINUS = "frontinus" # Interface

@dataclass
class CognitiveContext:
    """Cognitive processing context"""
    session_id: str
    user_input: str
    asl_parsed: Optional[Dict[str, Any]] = None
    current_state: CognitiveState = CognitiveState.IDLE
    active_minister: Optional[MinisterialRole] = None
    processing_chain: List[str] = field(default_factory=list)
    context_data: Dict[str, Any] = field(default_factory=dict)
    started_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "user_input": self.user_input,
            "asl_parsed": self.asl_parsed,
            "current_state": self.current_state.value,
            "active_minister": self.active_minister.value if self.active_minister else None,
            "processing_chain": self.processing_chain,
            "context_data": self.context_data,
            "started_at": self.started_at.isoformat()
        }

@dataclass
class CognitiveResult:
    """Result of cognitive processing"""
    success: bool
    output: Dict[str, Any]
    minister_responses: Dict[str, Any]
    processing_time: float
    final_state: CognitiveState
    error_message: Optional[str] = None

class CognitiveBridge:
    """
    Cognitive processing bridge for AetheroOS ministerial coordination
    
    Integrates with:
    - libs/superagent/app/agents/base.py
    - libs/superagent/app/agents/agent.py
    - All ministerial modules (primus, lucius, archivus, frontinus)
    """
    
    def __init__(self):
        self.active_contexts: Dict[str, CognitiveContext] = {}
        self.minister_handlers: Dict[MinisterialRole, Callable] = {}
        self.processing_pipeline = [
            MinisterialRole.PRIMUS,    # Strategic analysis
            MinisterialRole.LUCIUS,    # Execution planning
            MinisterialRole.ARCHIVUS,  # Memory processing
            MinisterialRole.FRONTINUS  # Interface preparation
        ]
        logger.info("[COGNITIVE-BRIDGE] Cognitive processing bridge initialized")
    
    def register_minister_handler(self, minister: MinisterialRole, handler: Callable):
        """Register a handler for a specific minister"""
        self.minister_handlers[minister] = handler
        logger.info(f"[MINISTER-REGISTER] {minister.value} handler registered")
    
    async def process_cognitive_request(self, 
                                      session_id: str, 
                                      user_input: str,
                                      asl_parsed: Optional[Dict[str, Any]] = None) -> CognitiveResult:
        """
        Process a cognitive request through the ministerial pipeline
        
        Args:
            session_id: Unique session identifier
            user_input: Raw user input
            asl_parsed: Pre-parsed ASL data (optional)
            
        Returns:
            CognitiveResult with processing outcomes
        """
        start_time = time.time()
        
        try:
            # Create cognitive context
            context = CognitiveContext(
                session_id=session_id,
                user_input=user_input,
                asl_parsed=asl_parsed
            )
            
            self.active_contexts[session_id] = context
            logger.info(f"[COGNITIVE-START] Session {session_id} processing started")
            
            # Process through ministerial pipeline
            minister_responses = {}
            
            for minister in self.processing_pipeline:
                context.current_state = self._get_state_for_minister(minister)
                context.active_minister = minister
                context.processing_chain.append(minister.value)
                
                # Process with minister
                if minister in self.minister_handlers:
                    try:
                        response = await self.minister_handlers[minister](context)
                        minister_responses[minister.value] = response
                        
                        # Update context with minister response
                        if isinstance(response, dict):
                            context.context_data.update(response)
                        
                        logger.info(f"[MINISTER-PROCESSED] {minister.value} completed successfully")
                        
                    except Exception as e:
                        logger.error(f"[MINISTER-ERROR] {minister.value} processing failed: {e}")
                        minister_responses[minister.value] = {"error": str(e)}
                        context.current_state = CognitiveState.ERROR
                        break
                else:
                    logger.warning(f"[MINISTER-MISSING] No handler for {minister.value}")
                    minister_responses[minister.value] = {"error": "Handler not registered"}
            
            # Finalize processing
            processing_time = time.time() - start_time
            context.current_state = CognitiveState.COMPLETED if context.current_state != CognitiveState.ERROR else CognitiveState.ERROR
            
            result = CognitiveResult(
                success=context.current_state == CognitiveState.COMPLETED,
                output=self._synthesize_output(minister_responses),
                minister_responses=minister_responses,
                processing_time=processing_time,
                final_state=context.current_state
            )
            
            logger.info(f"[COGNITIVE-COMPLETE] Session {session_id} completed in {processing_time:.2f}s")
            return result
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"[COGNITIVE-ERROR] Session {session_id} failed: {e}")
            
            return CognitiveResult(
                success=False,
                output={},
                minister_responses={},
                processing_time=processing_time,
                final_state=CognitiveState.ERROR,
                error_message=str(e)
            )
        
        finally:
            # Clean up context
            if session_id in self.active_contexts:
                del self.active_contexts[session_id]
    
    def _get_state_for_minister(self, minister: MinisterialRole) -> CognitiveState:
        """Map minister to processing state"""
        state_map = {
            MinisterialRole.PRIMUS: CognitiveState.ANALYZING,
            MinisterialRole.LUCIUS: CognitiveState.PLANNING,
            MinisterialRole.ARCHIVUS: CognitiveState.REMEMBERING,
            MinisterialRole.FRONTINUS: CognitiveState.INTERFACING
        }
        return state_map.get(minister, CognitiveState.IDLE)
    
    def _synthesize_output(self, minister_responses: Dict[str, Any]) -> Dict[str, Any]:
        """Synthesize final output from all minister responses"""
        
        output = {
            "synthesis_timestamp": datetime.now().isoformat(),
            "ministerial_cabinet_response": True,
            "components": {}
        }
        
        # Extract key components from each minister
        for minister, response in minister_responses.items():
            if isinstance(response, dict) and "error" not in response:
                output["components"][minister] = response
        
        # Create unified response based on ministerial specializations
        if "primus" in output["components"]:
            output["strategic_analysis"] = output["components"]["primus"]
        
        if "lucius" in output["components"]:
            output["execution_plan"] = output["components"]["lucius"]
        
        if "archivus" in output["components"]:
            output["memory_context"] = output["components"]["archivus"]
        
        if "frontinus" in output["components"]:
            output["interface_specification"] = output["components"]["frontinus"]
        
        return output
    
    async def get_context_status(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get current processing status for a session"""
        if session_id in self.active_contexts:
            return self.active_contexts[session_id].to_dict()
        return None
    
    async def integrate_with_superagent_agent(self, 
                                            agent_id: str, 
                                            cognitive_result: CognitiveResult) -> Dict[str, Any]:
        """
        Integrate cognitive processing result with Superagent agent
        
        Args:
            agent_id: Superagent agent identifier
            cognitive_result: Result from cognitive processing
            
        Returns:
            Superagent-compatible agent response
        """
        try:
            # Create Superagent agent response format
            agent_response = {
                "agent_id": agent_id,
                "response_type": "aethero_cognitive",
                "success": cognitive_result.success,
                "processing_time": cognitive_result.processing_time,
                "data": cognitive_result.output,
                "metadata": {
                    "ministerial_processing": True,
                    "final_state": cognitive_result.final_state.value,
                    "minister_responses": cognitive_result.minister_responses,
                    "constitutional_compliance": "AETH-CONST-2025-001"
                }
            }
            
            if cognitive_result.error_message:
                agent_response["error"] = cognitive_result.error_message
            
            logger.info(f"[SUPERAGENT-INTEGRATION] Cognitive result integrated for agent {agent_id}")
            return agent_response
            
        except Exception as e:
            logger.error(f"[INTEGRATION-ERROR] Failed to integrate with Superagent agent: {e}")
            return {"error": f"Integration failed: {str(e)}"}

# Bridge instance for registration
cognitive_bridge = CognitiveBridge()
