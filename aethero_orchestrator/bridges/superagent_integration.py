# AETH-INTEGRATION-001 :: ROLE: Multi-ministerial :: GOAL: Superagent Integration
# Minister: All ministers (Superagent integration)
# Purpose: Integrate AetheroOS ministerial cabinet with Superagent FastAPI application

"""
AetheroOS Superagent Integration

Extends Superagent's FastAPI application with AetheroOS ministerial cabinet
functionality, providing seamless integration between the two systems while
maintaining constitutional compliance.

Integration Points:
- FastAPI application extension
- Database schema extension
- WebSocket endpoint registration
- Middleware integration
- Startup/shutdown coordination
"""

import asyncio
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI

# Import AetheroOS bridge coordinator
from aethero_orchestrator.bridges import get_coordinator, get_all_bridges

logger = logging.getLogger("aethero.integration.superagent")

class AetheroSuperagentIntegrator:
    """
    Integrates AetheroOS with Superagent infrastructure
    
    Provides:
    - FastAPI application enhancement
    - Database integration
    - Websocket coordination
    - Constitutional compliance overlay
    """
    
    def __init__(self):
        self.bridge_coordinator = get_coordinator()
        self.is_integrated = False
        self.superagent_app: Optional[FastAPI] = None
        
        logger.info("[AETHERO-INTEGRATION] Superagent integrator initialized")
    
    async def integrate_with_superagent_app(self, app: FastAPI) -> bool:
        """
        Integrate AetheroOS with existing Superagent FastAPI app
        
        Args:
            app: Superagent FastAPI application instance
            
        Returns:
            bool: Integration success status
        """
        try:
            self.superagent_app = app
            
            # Initialize bridge coordinator with Superagent configuration
            integration_config = {
                "fastapi_app": app,
                "vectordb": {
                    "type": "chroma",  # Default, will be detected from Superagent config
                    "connection_string": None
                },
                "database": {
                    "type": "postgresql",  # Superagent uses PostgreSQL with Prisma
                    "prisma_client": None  # Will be set from Superagent
                }
            }
            
            # Initialize all bridges
            success = await self.bridge_coordinator.initialize_all_bridges(integration_config)
            
            if success:
                # Add AetheroOS middleware
                await self._add_aethero_middleware(app)
                
                # Extend startup/shutdown events
                await self._extend_lifecycle_events(app)
                
                # Add constitutional compliance middleware
                await self._add_constitutional_middleware(app)
                
                self.is_integrated = True
                logger.info("[AETHERO-INTEGRATION] ✅ AetheroOS successfully integrated with Superagent")
                
                # Log integration status
                status = await self.bridge_coordinator.get_system_status()
                logger.info(f"[AETHERO-INTEGRATION] Bridge status: {status['active_bridges']}/{status['total_bridges']} active")
                
                return True
            else:
                logger.error("[AETHERO-INTEGRATION] ❌ Bridge initialization failed")
                return False
                
        except Exception as e:
            logger.error(f"[AETHERO-INTEGRATION-ERROR] Integration failed: {e}")
            return False
    
    async def _add_aethero_middleware(self, app: FastAPI):
        """Add AetheroOS-specific middleware"""
        
        @app.middleware("http")
        async def aethero_constitutional_middleware(request, call_next):
            """Middleware for constitutional compliance tracking"""
            
            # Add constitutional headers
            response = await call_next(request)
            response.headers["X-AetheroOS-Constitutional-Compliance"] = "AETH-CONST-2025-001"
            response.headers["X-AetheroOS-Ministers"] = "primus,lucius,archivus,frontinus"
            
            # Log request for constitutional audit
            if hasattr(request, "url") and "/aethero" in str(request.url):
                logger.info(f"[CONSTITUTIONAL-AUDIT] AetheroOS request: {request.method} {request.url}")
            
            return response
        
        logger.info("[AETHERO-INTEGRATION] Constitutional middleware added")
    
    async def _extend_lifecycle_events(self, app: FastAPI):
        """Extend Superagent's startup/shutdown events with AetheroOS"""
        
        # Store original event handlers if they exist
        original_startup = getattr(app, "_startup_handlers", [])
        original_shutdown = getattr(app, "_shutdown_handlers", [])
        
        @app.on_event("startup")
        async def aethero_startup():
            """AetheroOS startup integration"""
            logger.info("[AETHERO-STARTUP] Initializing AetheroOS ministerial cabinet")
            
            # Perform health check on all bridges
            health_status = await self.bridge_coordinator.health_check()
            
            if health_status:
                logger.info("[AETHERO-STARTUP] ✅ All ministerial bridges healthy")
            else:
                logger.warning("[AETHERO-STARTUP] ⚠️ Some ministerial bridges unhealthy")
            
            # Launch Gradio dashboard if configured
            bridges = get_all_bridges()
            if "gradio" in bridges and bridges["gradio"]:
                try:
                    gradio_bridge = bridges["gradio"]
                    dashboard_url = gradio_bridge.launch_dashboard(
                        port=7860,
                        share=False  # Set to True for public sharing
                    )
                    if dashboard_url:
                        logger.info(f"[AETHERO-STARTUP] 🎨 Ministerial dashboard available at: {dashboard_url}")
                except Exception as e:
                    logger.error(f"[AETHERO-STARTUP] Dashboard launch failed: {e}")
        
        @app.on_event("shutdown")
        async def aethero_shutdown():
            """AetheroOS shutdown integration"""
            logger.info("[AETHERO-SHUTDOWN] Shutting down AetheroOS ministerial cabinet")
            
            # Graceful bridge shutdown
            self.bridge_coordinator.shutdown()
            
            logger.info("[AETHERO-SHUTDOWN] ✅ AetheroOS shutdown complete")
        
        logger.info("[AETHERO-INTEGRATION] Lifecycle event handlers extended")
    
    async def _add_constitutional_middleware(self, app: FastAPI):
        """Add constitutional compliance middleware"""
        
        @app.middleware("http")
        async def constitutional_compliance_logger(request, call_next):
            """Log all requests for constitutional compliance"""
            
            start_time = asyncio.get_event_loop().time()
            
            # Process request
            response = await call_next(request)
            
            processing_time = asyncio.get_event_loop().time() - start_time
            
            # Log for constitutional audit
            compliance_record = {
                "timestamp": start_time,
                "method": request.method,
                "url": str(request.url),
                "processing_time": processing_time,
                "status_code": response.status_code,
                "constitutional_compliance": "AETH-CONST-2025-001"
            }
            
            # This would typically be sent to Archivus for storage
            logger.debug(f"[CONSTITUTIONAL-LOG] {compliance_record}")
            
            return response
        
        logger.info("[AETHERO-INTEGRATION] Constitutional compliance middleware added")
    
    async def get_integration_status(self) -> Dict[str, Any]:
        """Get integration status report"""
        
        if not self.is_integrated:
            return {
                "integrated": False,
                "error": "Not integrated with Superagent"
            }
        
        bridge_status = await self.bridge_coordinator.get_system_status()
        
        return {
            "integrated": True,
            "superagent_app": self.superagent_app is not None,
            "bridge_coordinator": bridge_status,
            "ministerial_cabinet": {
                "primus": "strategic_logic",
                "lucius": "execution",
                "archivus": "memory", 
                "frontinus": "interface"
            },
            "constitutional_compliance": "AETH-CONST-2025-001"
        }
    
    async def process_aethero_request_via_superagent(self, 
                                                   user_input: str,
                                                   session_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Process AetheroOS request through integrated Superagent infrastructure
        
        Args:
            user_input: User input (potentially with ASL syntax)
            session_id: Session identifier
            
        Returns:
            Dict containing processing result
        """
        if not self.is_integrated:
            return {"error": "AetheroOS not integrated with Superagent"}
        
        try:
            # Process through bridge coordinator
            result = await self.bridge_coordinator.process_aethero_request(
                user_input=user_input,
                session_id=session_id
            )
            
            # Add Superagent integration metadata
            result["superagent_integration"] = {
                "version": "0.2.39",  # From Superagent FastAPI app
                "integration_timestamp": asyncio.get_event_loop().time(),
                "constitutional_compliance": "AETH-CONST-2025-001"
            }
            
            return result
            
        except Exception as e:
            logger.error(f"[SUPERAGENT-PROCESS-ERROR] {e}")
            return {
                "success": False,
                "error": str(e),
                "constitutional_compliance": "AETH-CONST-2025-001"
            }

# Global integrator instance
aethero_superagent_integrator = AetheroSuperagentIntegrator()

# Integration helper function
async def integrate_aethero_with_superagent(app: FastAPI) -> bool:
    """
    Helper function to integrate AetheroOS with Superagent FastAPI app
    
    Args:
        app: Superagent FastAPI application
        
    Returns:
        bool: Integration success status
    """
    return await aethero_superagent_integrator.integrate_with_superagent_app(app)

# Export integration components
__all__ = [
    "AetheroSuperagentIntegrator",
    "aethero_superagent_integrator", 
    "integrate_aethero_with_superagent"
]
