# AETH-MAIN-001 :: Enhanced Superagent Main with AetheroOS Integration
# Original Superagent main.py enhanced with AetheroOS ministerial cabinet

import logging
import time
import sys
import os

# Add the libs/superagent path to sys.path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'libs', 'superagent'))

import colorlog
from decouple import config
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

try:
    from app.routers import router
    from app.utils.prisma import prisma
except ImportError:
    # Fallback for development
    router = None
    prisma = None

# AetheroOS Integration
from aethero_orchestrator.bridges.superagent_integration import integrate_aethero_with_superagent

# Create a color formatter
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s:  %(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
    secondary_log_colors={},
    style="%",
)  # Create a console handler and set the formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    handlers=[console_handler],
    force=True,
)

app = FastAPI(
    title="Superagent + AetheroOS",  # Enhanced title
    docs_url="/",
    description="🥷 Run AI-agents with an API | 🏛️ Enhanced with AetheroOS Ministerial Cabinet",
    version="0.2.39-AETHERO",  # Version with AetheroOS
    servers=[{"url": config("SUPERAGENT_API_URL", default="http://localhost:8000")}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Total request time: {process_time} secs")
    return response


@app.on_event("startup")
async def startup():
    """Enhanced startup with AetheroOS integration"""
    
    # Original Superagent startup
    if prisma is not None:
        await prisma.connect()
        logging.info("🥷 Superagent database connected")
    else:
        logging.warning("🥷 Superagent database not available - running in standalone mode")
    
    # AetheroOS Integration
    try:
        aethero_integrated = await integrate_aethero_with_superagent(app)
        
        if aethero_integrated:
            logging.info("🏛️ AetheroOS Ministerial Cabinet integrated successfully!")
            logging.info("📋 Constitutional Compliance: AETH-CONST-2025-001")
        else:
            logging.warning("⚠️ AetheroOS integration failed, running Superagent only")
            
    except Exception as e:
        logging.error(f"❌ AetheroOS integration error: {e}")
        logging.info("🥷 Continuing with Superagent only...")


@app.on_event("shutdown")
async def shutdown():
    """Enhanced shutdown with AetheroOS cleanup"""
    
    # AetheroOS cleanup happens automatically via integration middleware
    logging.info("🏛️ AetheroOS shutdown initiated")
    
    # Original Superagent shutdown
    if prisma is not None:
        await prisma.disconnect()
        logging.info("🥷 Superagent database disconnected")


# Include original Superagent routes if available
if router is not None:
    app.include_router(router)
else:
    logging.info("🥷 Superagent routes not available - AetheroOS standalone mode")

# AetheroOS Status Endpoint
@app.get("/aethero/integration/status")
async def get_aethero_integration_status():
    """Get AetheroOS integration status"""
    try:
        from aethero_orchestrator.bridges.superagent_integration import aethero_superagent_integrator
        
        status = await aethero_superagent_integrator.get_integration_status()
        return {
            "superagent_version": "0.2.39",
            "aethero_integration": status,
            "constitutional_compliance": "AETH-CONST-2025-001"
        }
    except Exception as e:
        return {
            "superagent_version": "0.2.39",
            "aethero_integration": {"error": str(e)},
            "constitutional_compliance": "AETH-CONST-2025-001"
        }

# Enhanced documentation endpoint
@app.get("/aethero/docs")
async def get_aethero_documentation():
    """Get AetheroOS integration documentation"""
    return {
        "title": "AetheroOS + Superagent Integration",
        "description": "AI agent orchestration with constitutional ministerial cabinet",
        "ministers": {
            "primus": {
                "role": "Strategic Logic & ASL Parsing",
                "endpoints": ["/aethero/asl/process"],
                "description": "Handles strategic analysis and ASL syntax processing"
            },
            "lucius": {
                "role": "Backend Execution",
                "endpoints": ["/aethero/minister/lucius", "/aethero/ws/{session_id}"],
                "description": "Manages task execution and server operations"
            },
            "archivus": {
                "role": "Memory & Constitutional Audit",
                "endpoints": ["/aethero/minister/archivus"],
                "description": "Handles memory storage and constitutional compliance"
            },
            "frontinus": {
                "role": "Interface & Visualization",
                "endpoints": ["/aethero/minister/frontinus"],
                "description": "Manages UI/UX and real-time visualizations"
            }
        },
        "asl_syntax": {
            "description": "Aethero Syntax Language for structured interactions",
            "tags": ["[INTENT:goal]", "[ACTION:task]", "[OUTPUT:result]", "[HOOK:logging]"],
            "example": "[INTENT:analyze_data] [ACTION:process_dataset] [OUTPUT:insights] [HOOK:archivus_audit]"
        },
        "constitutional_compliance": "AETH-CONST-2025-001",
        "dashboard": "Available at port 7860 (if Gradio enabled)"
    }

if __name__ == "__main__":
    import uvicorn
    
    logging.info("🚀 Starting Superagent + AetheroOS...")
    
    uvicorn.run(
        "aethero_main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info"
    )
