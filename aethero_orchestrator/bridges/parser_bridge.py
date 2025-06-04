# AETH-BRIDGE-002 :: ROLE: Primus :: GOAL: ASL Parser Integration Bridge
# Minister: Primus (Strategic logic and parser)
# Purpose: Bridge ASL syntax parsing with Superagent's processing pipeline

"""
ASL Parser Integration Bridge

Connects AetheroOS ASL (Aethero Syntax Language) parsing capabilities
with Superagent's agent processing pipeline. Handles syntax validation,
intent extraction, and action routing.

ASL Tag Support:
- [INTENT:<úmysel>]: Parse user intentions
- [ACTION:<akcia>]: Define executable actions  
- [OUTPUT:<výsledok>]: Specify expected outputs
- [HOOK:<cieľ logovania>]: Logging integration points
"""

import asyncio
import json
import re
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger("aethero.bridges.parser")

class ASLTagType(Enum):
    """ASL tag types for parsing"""
    INTENT = "INTENT"
    ACTION = "ACTION" 
    OUTPUT = "OUTPUT"
    HOOK = "HOOK"

@dataclass
class ASLParseResult:
    """Result of ASL parsing operation"""
    tags: Dict[ASLTagType, str]
    raw_content: str
    is_valid: bool
    validation_errors: List[str]
    ministerial_routing: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "tags": {tag.value: value for tag, value in self.tags.items()},
            "raw_content": self.raw_content,
            "is_valid": self.is_valid,
            "validation_errors": self.validation_errors,
            "ministerial_routing": self.ministerial_routing
        }

class PrimusParserBridge:
    """
    Parser bridge connecting ASL syntax with Superagent processing
    
    Integrates with:
    - libs/superagent/app/api/workflow_configs/
    - libs/superagent/app/agents/
    - aethero_orchestrator/primus/orchestrator.py
    """
    
    def __init__(self):
        self.asl_pattern = re.compile(r'\[(\w+):([^\]]+)\]')
        self.ministerial_routes = {
            "strategic": "primus",
            "execution": "lucius", 
            "memory": "archivus",
            "interface": "frontinus"
        }
        logger.info("[PARSER-BRIDGE] Primus Parser Bridge initialized")
    
    async def parse_asl_input(self, input_text: str) -> ASLParseResult:
        """
        Parse ASL syntax from user input
        
        Args:
            input_text: Raw user input containing ASL tags
            
        Returns:
            ASLParseResult with parsed tags and validation status
        """
        try:
            # Extract ASL tags
            matches = self.asl_pattern.findall(input_text)
            tags = {}
            validation_errors = []
            
            for tag_name, tag_value in matches:
                try:
                    tag_type = ASLTagType(tag_name.upper())
                    tags[tag_type] = tag_value.strip()
                except ValueError:
                    validation_errors.append(f"Unknown ASL tag: {tag_name}")
            
            # Validate required tags
            if not tags:
                validation_errors.append("No valid ASL tags found")
            
            # Determine ministerial routing
            routing = self._determine_ministerial_routing(tags)
            
            result = ASLParseResult(
                tags=tags,
                raw_content=input_text,
                is_valid=len(validation_errors) == 0,
                validation_errors=validation_errors,
                ministerial_routing=routing
            )
            
            logger.info(f"[ASL-PARSE] Parsed {len(tags)} tags, routed to: {routing}")
            return result
            
        except Exception as e:
            logger.error(f"[ASL-PARSE-ERROR] Failed to parse ASL: {e}")
            return ASLParseResult(
                tags={},
                raw_content=input_text,
                is_valid=False,
                validation_errors=[f"Parse error: {str(e)}"]
            )
    
    def _determine_ministerial_routing(self, tags: Dict[ASLTagType, str]) -> str:
        """Determine which minister should handle the parsed request"""
        
        # Route based on tag content analysis
        if ASLTagType.ACTION in tags:
            action = tags[ASLTagType.ACTION].lower()
            if any(keyword in action for keyword in ["execute", "build", "deploy", "run"]):
                return "lucius"
            elif any(keyword in action for keyword in ["remember", "store", "log", "audit"]):
                return "archivus"
            elif any(keyword in action for keyword in ["display", "show", "visualize", "interface"]):
                return "frontinus"
        
        # Default to strategic routing (Primus)
        return "primus"
    
    async def integrate_with_superagent(self, parse_result: ASLParseResult) -> Dict[str, Any]:
        """
        Integrate parsed ASL with Superagent workflow
        
        Args:
            parse_result: Parsed ASL result
            
        Returns:
            Superagent-compatible workflow configuration
        """
        try:
            # Create Superagent workflow config
            workflow_config = {
                "id": f"aethero_asl_{hash(parse_result.raw_content)}",
                "name": f"AetheroOS ASL Workflow",
                "description": f"ASL-driven workflow routed to {parse_result.ministerial_routing}",
                "steps": [],
                "metadata": {
                    "asl_tags": parse_result.to_dict(),
                    "ministerial_routing": parse_result.ministerial_routing,
                    "constitutional_compliance": "AETH-CONST-2025-001"
                }
            }
            
            # Add workflow steps based on parsed tags
            if ASLTagType.INTENT in parse_result.tags:
                workflow_config["steps"].append({
                    "type": "intent_analysis",
                    "config": {
                        "intent": parse_result.tags[ASLTagType.INTENT],
                        "minister": parse_result.ministerial_routing
                    }
                })
            
            if ASLTagType.ACTION in parse_result.tags:
                workflow_config["steps"].append({
                    "type": "action_execution", 
                    "config": {
                        "action": parse_result.tags[ASLTagType.ACTION],
                        "minister": parse_result.ministerial_routing
                    }
                })
            
            if ASLTagType.OUTPUT in parse_result.tags:
                workflow_config["steps"].append({
                    "type": "output_formatting",
                    "config": {
                        "expected_output": parse_result.tags[ASLTagType.OUTPUT]
                    }
                })
            
            if ASLTagType.HOOK in parse_result.tags:
                workflow_config["steps"].append({
                    "type": "logging_hook",
                    "config": {
                        "hook_target": parse_result.tags[ASLTagType.HOOK],
                        "minister": "archivus"  # Logging always goes to Archivus
                    }
                })
            
            logger.info(f"[SUPERAGENT-INTEGRATION] Created workflow with {len(workflow_config['steps'])} steps")
            return workflow_config
            
        except Exception as e:
            logger.error(f"[INTEGRATION-ERROR] Failed to integrate with Superagent: {e}")
            return {}
    
    async def validate_asl_syntax(self, content: str) -> Tuple[bool, List[str]]:
        """Validate ASL syntax compliance"""
        errors = []
        
        # Check for balanced brackets
        if content.count('[') != content.count(']'):
            errors.append("Unbalanced ASL tag brackets")
        
        # Check for valid tag format
        matches = self.asl_pattern.findall(content)
        if not matches:
            errors.append("No valid ASL tags found")
        
        # Check for recognized tag types
        for tag_name, _ in matches:
            try:
                ASLTagType(tag_name.upper())
            except ValueError:
                errors.append(f"Unrecognized ASL tag: {tag_name}")
        
        return len(errors) == 0, errors

# Bridge instance for registration
parser_bridge = PrimusParserBridge()
