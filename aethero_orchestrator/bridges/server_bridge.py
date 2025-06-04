# AETH-BRIDGE-004 :: ROLE: Lucius :: GOAL: Server Integration Bridge
# Minister: Lucius (Execution and backend)
# Purpose: Bridge AetheroOS with Superagent's FastAPI server infrastructure

"""
Server Integration Bridge

Connects AetheroOS ministerial endpoints with Superagent's FastAPI server,
providing WebSocket coordination, API route integration, and real-time
communication between ministerial cabinet and client interfaces.

Server Integration Points:
- FastAPI route registration
- WebSocket connection management
- Middleware integration
- Authentication & authorization
- Real-time event streaming
"""

import asyncio
import json
import time
from typing import Dict, Any, List, Optional, Callable, Set
from dataclasses import dataclass, field
from datetime import datetime
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("aethero.bridges.server")

@dataclass
class WebSocketConnection:
    """WebSocket connection tracking"""
    websocket: WebSocket
    session_id: str
    user_id: Optional[str] = None
    ministerial_subscriptions: Set[str] = field(default_factory=set)
    connected_at: datetime = field(default_factory=datetime.now)
    last_activity: datetime = field(default_factory=datetime.now)

@dataclass
class ServerEvent:
    """Server event for broadcasting"""
    event_type: str
    minister: str
    data: Dict[str, Any]
    session_id: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": self.event_type,
            "minister": self.minister, 
            "data": self.data,
            "session_id": self.session_id,
            "timestamp": self.timestamp.isoformat()
        }

class LuciusServerBridge:
    """
    Server bridge for AetheroOS-Superagent integration
    
    Integrates with:
    - libs/superagent/app/main.py (FastAPI app)
    - libs/superagent/app/api/ (API routes)
    - libs/superagent/app/websockets/ (WebSocket handlers)
    """
    
    def __init__(self, app: Optional[FastAPI] = None):
        self.app = app
        self.websocket_connections: Dict[str, WebSocketConnection] = {}
        self.ministerial_endpoints: Dict[str, Callable] = {}
        self.event_subscribers: Dict[str, Set[str]] = {}  # minister -> session_ids
        self.middleware_handlers: List[Callable] = []
        
        if self.app:
            self._setup_cors()
            self._register_routes()
        
        logger.info("[SERVER-BRIDGE] Lucius Server Bridge initialized")
    
    def set_app(self, app: FastAPI):
        """Set FastAPI app instance (for delayed initialization)"""
        self.app = app
        self._setup_cors()
        self._register_routes()
        logger.info("[SERVER-BRIDGE] FastAPI app configured")
    
    def _setup_cors(self):
        """Configure CORS middleware for AetheroOS"""
        if self.app:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=["*"],  # Configure based on deployment
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
    
    def _register_routes(self):
        """Register AetheroOS API routes"""
        if not self.app:
            return
        
        # Ministerial status endpoint
        @self.app.get("/aethero/status")
        async def get_ministerial_status():
            """Get status of all AetheroOS ministers"""
            return {
                "status": "operational",
                "ministers": {
                    "primus": {"role": "strategic_logic", "status": "active"},
                    "lucius": {"role": "execution", "status": "active"},
                    "archivus": {"role": "memory", "status": "active"},
                    "frontinus": {"role": "interface", "status": "active"}
                },
                "active_connections": len(self.websocket_connections),
                "constitutional_compliance": "AETH-CONST-2025-001"
            }
        
        # ASL processing endpoint
        @self.app.post("/aethero/asl/process")
        async def process_asl_request(request: Dict[str, Any]):
            """Process ASL syntax request through ministerial cabinet"""
            try:
                session_id = request.get("session_id", f"asl_{int(time.time())}")
                user_input = request.get("input", "")
                
                if not user_input:
                    raise HTTPException(status_code=400, detail="Input required")
                
                # Process through cognitive bridge (will be integrated)
                result = await self._process_ministerial_request(session_id, user_input)
                
                return JSONResponse(content={
                    "success": True,
                    "session_id": session_id,
                    "result": result
                })
                
            except Exception as e:
                logger.error(f"[ASL-PROCESS-ERROR] {e}")
                raise HTTPException(status_code=500, detail=str(e))
        
        # Ministerial direct endpoint
        @self.app.post("/aethero/minister/{minister}")
        async def call_minister_directly(minister: str, request: Dict[str, Any]):
            """Direct communication with specific minister"""
            try:
                if minister not in ["primus", "lucius", "archivus", "frontinus"]:
                    raise HTTPException(status_code=404, detail="Minister not found")
                
                if minister in self.ministerial_endpoints:
                    result = await self.ministerial_endpoints[minister](request)
                    return JSONResponse(content={"success": True, "result": result})
                else:
                    raise HTTPException(status_code=503, detail=f"Minister {minister} not available")
                    
            except Exception as e:
                logger.error(f"[MINISTER-CALL-ERROR] {minister}: {e}")
                raise HTTPException(status_code=500, detail=str(e))
        
        # WebSocket endpoint for real-time communication
        @self.app.websocket("/aethero/ws/{session_id}")
        async def websocket_endpoint(websocket: WebSocket, session_id: str):
            await self._handle_websocket_connection(websocket, session_id)
    
    async def _handle_websocket_connection(self, websocket: WebSocket, session_id: str):
        """Handle WebSocket connection lifecycle"""
        await websocket.accept()
        
        connection = WebSocketConnection(
            websocket=websocket,
            session_id=session_id
        )
        
        self.websocket_connections[session_id] = connection
        logger.info(f"[WEBSOCKET-CONNECT] Session {session_id} connected")
        
        try:
            # Send welcome message
            await websocket.send_json({
                "type": "connection_established",
                "session_id": session_id,
                "ministerial_cabinet": "available",
                "timestamp": datetime.now().isoformat()
            })
            
            # Handle incoming messages
            while True:
                data = await websocket.receive_json()
                await self._handle_websocket_message(connection, data)
                
        except WebSocketDisconnect:
            logger.info(f"[WEBSOCKET-DISCONNECT] Session {session_id} disconnected")
        except Exception as e:
            logger.error(f"[WEBSOCKET-ERROR] Session {session_id}: {e}")
        finally:
            # Clean up connection
            if session_id in self.websocket_connections:
                del self.websocket_connections[session_id]
            
            # Remove from event subscriptions
            for minister_subs in self.event_subscribers.values():
                minister_subs.discard(session_id)
    
    async def _handle_websocket_message(self, connection: WebSocketConnection, data: Dict[str, Any]):
        """Handle incoming WebSocket message"""
        try:
            message_type = data.get("type")
            connection.last_activity = datetime.now()
            
            if message_type == "asl_process":
                # Process ASL request through ministerial cabinet
                user_input = data.get("input", "")
                result = await self._process_ministerial_request(connection.session_id, user_input)
                
                await connection.websocket.send_json({
                    "type": "asl_result",
                    "session_id": connection.session_id,
                    "result": result,
                    "timestamp": datetime.now().isoformat()
                })
            
            elif message_type == "subscribe_minister":
                # Subscribe to minister events
                minister = data.get("minister")
                if minister in ["primus", "lucius", "archivus", "frontinus"]:
                    connection.ministerial_subscriptions.add(minister)
                    
                    if minister not in self.event_subscribers:
                        self.event_subscribers[minister] = set()
                    self.event_subscribers[minister].add(connection.session_id)
                    
                    await connection.websocket.send_json({
                        "type": "subscription_confirmed",
                        "minister": minister,
                        "session_id": connection.session_id
                    })
            
            elif message_type == "minister_direct":
                # Direct minister communication
                minister = data.get("minister")
                request_data = data.get("data", {})
                
                if minister in self.ministerial_endpoints:
                    result = await self.ministerial_endpoints[minister](request_data)
                    await connection.websocket.send_json({
                        "type": "minister_response",
                        "minister": minister,
                        "result": result,
                        "session_id": connection.session_id
                    })
                    
        except Exception as e:
            logger.error(f"[WEBSOCKET-MESSAGE-ERROR] {e}")
            await connection.websocket.send_json({
                "type": "error",
                "message": str(e),
                "session_id": connection.session_id
            })
    
    async def _process_ministerial_request(self, session_id: str, user_input: str) -> Dict[str, Any]:
        """Process request through ministerial cabinet (placeholder for cognitive bridge integration)"""
        # This will integrate with cognitive_bridge once implemented
        return {
            "session_id": session_id,
            "input": user_input,
            "status": "processed",
            "ministerial_response": "Processed through AetheroOS cabinet",
            "timestamp": datetime.now().isoformat()
        }
    
    def register_ministerial_endpoint(self, minister: str, handler: Callable):
        """Register handler for ministerial endpoint"""
        self.ministerial_endpoints[minister] = handler
        logger.info(f"[MINISTER-ENDPOINT] {minister} endpoint registered")
    
    async def broadcast_ministerial_event(self, event: ServerEvent):
        """Broadcast event to subscribed connections"""
        if event.minister in self.event_subscribers:
            disconnected_sessions = []
            
            for session_id in self.event_subscribers[event.minister]:
                if session_id in self.websocket_connections:
                    try:
                        connection = self.websocket_connections[session_id]
                        await connection.websocket.send_json({
                            "type": "ministerial_event",
                            **event.to_dict()
                        })
                    except Exception as e:
                        logger.error(f"[BROADCAST-ERROR] Session {session_id}: {e}")
                        disconnected_sessions.append(session_id)
            
            # Clean up disconnected sessions
            for session_id in disconnected_sessions:
                self.event_subscribers[event.minister].discard(session_id)
                if session_id in self.websocket_connections:
                    del self.websocket_connections[session_id]
    
    async def get_server_metrics(self) -> Dict[str, Any]:
        """Get server performance metrics"""
        return {
            "active_connections": len(self.websocket_connections),
            "ministerial_endpoints": list(self.ministerial_endpoints.keys()),
            "event_subscribers": {
                minister: len(sessions) 
                for minister, sessions in self.event_subscribers.items()
            },
            "uptime": "operational",  # TODO: Calculate actual uptime
            "constitutional_compliance": "AETH-CONST-2025-001"
        }

# Bridge instance for registration
server_bridge = LuciusServerBridge()
