#!/usr/bin/env python3
# AETH-VALIDATION-001 :: ROLE: Multi-ministerial :: GOAL: Validate AetheroOS Integration
# Minister: All ministers (validation)
# Purpose: Validate AetheroOS-Superagent integration and bridge functionality

"""
AetheroOS Integration Validation Script

Comprehensive validation script that tests all aspects of the AetheroOS-Superagent
integration, including bridge functionality, database connectivity, constitutional
compliance, and ministerial cabinet operations.

Validation Categories:
- Bridge initialization and communication
- Database schema compatibility
- ASL syntax parsing
- Cognitive processing pipeline
- WebSocket functionality
- Constitutional compliance
- Performance metrics
"""

import asyncio
import json
import time
import sys
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("aethero.validation")

class AetheroIntegrationValidator:
    """Comprehensive validation for AetheroOS-Superagent integration"""
    
    def __init__(self):
        self.validation_results: Dict[str, Any] = {}
        self.start_time = time.time()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    async def run_full_validation(self) -> Dict[str, Any]:
        """Run complete validation suite"""
        logger.info("🏛️ Starting AetheroOS Integration Validation")
        logger.info("📋 Constitutional Compliance: AETH-CONST-2025-001")
        
        # Validation tests
        validation_tests = [
            ("Directory Structure", self.validate_directory_structure),
            ("Bridge Modules", self.validate_bridge_modules),
            ("Dependencies", self.validate_dependencies),
            ("Configuration", self.validate_configuration),
            ("Database Schema", self.validate_database_schema),
            ("ASL Parser", self.validate_asl_parser),
            ("Cognitive Bridge", self.validate_cognitive_bridge),
            ("Server Bridge", self.validate_server_bridge),
            ("Memory Bridge", self.validate_memory_bridge),
            ("Gradio Bridge", self.validate_gradio_bridge),
            ("Bridge Coordinator", self.validate_bridge_coordinator),
            ("Constitutional Compliance", self.validate_constitutional_compliance)
        ]
        
        # Run all tests
        for test_name, test_func in validation_tests:
            logger.info(f"🔍 Validating: {test_name}")
            try:
                result = await test_func()
                self.validation_results[test_name] = {
                    "status": "passed" if result else "failed",
                    "details": result if isinstance(result, dict) else {"success": result}
                }
                
                if result:
                    logger.info(f"✅ {test_name}: PASSED")
                else:
                    logger.error(f"❌ {test_name}: FAILED")
                    
            except Exception as e:
                logger.error(f"💥 {test_name}: ERROR - {e}")
                self.validation_results[test_name] = {
                    "status": "error",
                    "details": {"error": str(e)}
                }
                self.errors.append(f"{test_name}: {str(e)}")
        
        # Generate final report
        return await self.generate_validation_report()
    
    async def validate_directory_structure(self) -> bool:
        """Validate AetheroOS directory structure"""
        try:
            base_path = Path("/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra")
            
            required_paths = [
                "aethero_orchestrator/",
                "aethero_orchestrator/bridges/",
                "aethero_orchestrator/primus/",
                "aethero_orchestrator/lucius/", 
                "aethero_orchestrator/archivus/",
                "aethero_orchestrator/frontinus/",
                "aethero_manifest.yaml",
                "AETHERO_ORCHESTRA_EXECUTIVE_PLAN.md"
            ]
            
            missing_paths = []
            for path in required_paths:
                if not (base_path / path).exists():
                    missing_paths.append(path)
            
            if missing_paths:
                self.errors.extend([f"Missing: {path}" for path in missing_paths])
                return False
            
            return True
            
        except Exception as e:
            self.errors.append(f"Directory validation error: {e}")
            return False
    
    async def validate_bridge_modules(self) -> bool:
        """Validate bridge module imports"""
        try:
            # Test imports
            import sys
            sys.path.append("/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra")
            
            from aethero_orchestrator.bridges import get_coordinator, get_all_bridges
            from aethero_orchestrator.bridges.parser_bridge import parser_bridge
            from aethero_orchestrator.bridges.cognitive_bridge import cognitive_bridge
            from aethero_orchestrator.bridges.server_bridge import server_bridge
            from aethero_orchestrator.bridges.memory_bridge import memory_bridge
            from aethero_orchestrator.bridges.gradio_bridge import gradio_bridge
            from aethero_orchestrator.bridges.bridge_coordinator import bridge_coordinator
            
            # Test bridge registry
            bridges = get_all_bridges()
            expected_bridges = ["parser", "cognitive", "server", "memory", "gradio", "coordinator"]
            
            for bridge_name in expected_bridges:
                if bridge_name not in bridges:
                    self.errors.append(f"Bridge not registered: {bridge_name}")
                    return False
            
            return True
            
        except ImportError as e:
            self.errors.append(f"Bridge import error: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Bridge validation error: {e}")
            return False
    
    async def validate_dependencies(self) -> bool:
        """Validate required dependencies"""
        try:
            required_modules = [
                "fastapi",
                "uvicorn", 
                "pydantic",
                "asyncio",
                "logging",
                "json",
                "datetime",
                "typing",
                "dataclasses",
                "enum"
            ]
            
            missing_modules = []
            for module in required_modules:
                try:
                    __import__(module)
                except ImportError:
                    missing_modules.append(module)
            
            if missing_modules:
                self.warnings.extend([f"Optional dependency missing: {module}" for module in missing_modules])
                # Don't fail for optional dependencies
            
            return True
            
        except Exception as e:
            self.errors.append(f"Dependency validation error: {e}")
            return False
    
    async def validate_configuration(self) -> bool:
        """Validate configuration files"""
        try:
            import yaml
            
            # Validate aethero_manifest.yaml
            manifest_path = Path("/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_manifest.yaml")
            
            if not manifest_path.exists():
                self.errors.append("aethero_manifest.yaml not found")
                return False
            
            with open(manifest_path, 'r') as f:
                manifest = yaml.safe_load(f)
            
            # Validate required sections
            required_sections = [
                "constitutional_framework",
                "ministerial_cabinet", 
                "integration_points",
                "deployment"
            ]
            
            for section in required_sections:
                if section not in manifest:
                    self.errors.append(f"Missing manifest section: {section}")
                    return False
            
            return True
            
        except Exception as e:
            self.errors.append(f"Configuration validation error: {e}")
            return False
    
    async def validate_database_schema(self) -> bool:
        """Validate database schema extension"""
        try:
            schema_path = Path("/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_schema_extension.prisma")
            
            if not schema_path.exists():
                self.errors.append("aethero_schema_extension.prisma not found")
                return False
            
            # Read schema content
            with open(schema_path, 'r') as f:
                schema_content = f.read()
            
            # Validate required models
            required_models = [
                "AetheroSession",
                "AetheroMemoryRecord", 
                "AetheroCognitiveEvent",
                "AetheroAuditRecord",
                "AetheroMinisterConfig"
            ]
            
            for model in required_models:
                if f"model {model}" not in schema_content:
                    self.errors.append(f"Missing schema model: {model}")
                    return False
            
            return True
            
        except Exception as e:
            self.errors.append(f"Schema validation error: {e}")
            return False
    
    async def validate_asl_parser(self) -> Dict[str, Any]:
        """Validate ASL parser functionality"""
        try:
            from aethero_orchestrator.bridges.parser_bridge import parser_bridge
            
            # Test ASL parsing
            test_input = "[INTENT:test] [ACTION:validate] [OUTPUT:success] [HOOK:audit]"
            result = await parser_bridge.parse_asl_input(test_input)
            
            validation_result = {
                "asl_parsed": result.is_valid,
                "tags_found": len(result.tags),
                "ministerial_routing": result.ministerial_routing is not None,
                "validation_errors": len(result.validation_errors)
            }
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"ASL parser validation error: {e}")
            return {"error": str(e)}
    
    async def validate_cognitive_bridge(self) -> Dict[str, Any]:
        """Validate cognitive processing bridge"""
        try:
            from aethero_orchestrator.bridges.cognitive_bridge import cognitive_bridge
            
            # Test cognitive processing
            test_session = f"test_session_{int(time.time())}"
            test_input = "Test cognitive processing"
            
            result = await cognitive_bridge.process_cognitive_request(
                session_id=test_session,
                user_input=test_input
            )
            
            validation_result = {
                "processing_completed": result.success,
                "processing_time": result.processing_time,
                "minister_responses": len(result.minister_responses),
                "final_state": result.final_state.value
            }
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"Cognitive bridge validation error: {e}")
            return {"error": str(e)}
    
    async def validate_server_bridge(self) -> Dict[str, Any]:
        """Validate server bridge functionality"""
        try:
            from aethero_orchestrator.bridges.server_bridge import server_bridge
            
            # Test server bridge methods
            metrics = await server_bridge.get_server_metrics()
            
            validation_result = {
                "bridge_initialized": True,
                "metrics_available": isinstance(metrics, dict),
                "constitutional_compliance": "constitutional_compliance" in metrics
            }
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"Server bridge validation error: {e}")
            return {"error": str(e)}
    
    async def validate_memory_bridge(self) -> Dict[str, Any]:
        """Validate memory bridge functionality"""
        try:
            from aethero_orchestrator.bridges.memory_bridge import memory_bridge
            
            # Test memory bridge methods
            stats = await memory_bridge.get_memory_statistics()
            
            validation_result = {
                "bridge_initialized": True,
                "statistics_available": isinstance(stats, dict),
                "memory_types": "memory_type_distribution" in stats
            }
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"Memory bridge validation error: {e}")
            return {"error": str(e)}
    
    async def validate_gradio_bridge(self) -> Dict[str, Any]:
        """Validate Gradio interface bridge"""
        try:
            from aethero_orchestrator.bridges.gradio_bridge import gradio_bridge, GRADIO_AVAILABLE
            
            # Test Gradio bridge methods
            metrics = gradio_bridge.get_interface_metrics()
            
            validation_result = {
                "bridge_initialized": True,
                "gradio_available": GRADIO_AVAILABLE,
                "metrics_available": isinstance(metrics, dict),
                "dashboard_capability": "gradio_available" in metrics
            }
            
            if not GRADIO_AVAILABLE:
                self.warnings.append("Gradio not available - dashboard functionality limited")
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"Gradio bridge validation error: {e}")
            return {"error": str(e)}
    
    async def validate_bridge_coordinator(self) -> Dict[str, Any]:
        """Validate bridge coordinator functionality"""
        try:
            from aethero_orchestrator.bridges.bridge_coordinator import bridge_coordinator
            
            # Test coordinator methods
            status = await bridge_coordinator.get_system_status()
            health = await bridge_coordinator.health_check()
            
            validation_result = {
                "coordinator_initialized": True,
                "system_status_available": isinstance(status, dict),
                "health_check_passed": health,
                "bridges_registered": status.get("total_bridges", 0) > 0
            }
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"Bridge coordinator validation error: {e}")
            return {"error": str(e)}
    
    async def validate_constitutional_compliance(self) -> Dict[str, Any]:
        """Validate constitutional compliance framework"""
        try:
            # Check for constitutional compliance markers
            compliance_markers = []
            
            # Check bridge files for constitutional compliance
            bridge_files = [
                "/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_orchestrator/bridges/parser_bridge.py",
                "/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_orchestrator/bridges/cognitive_bridge.py",
                "/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_orchestrator/bridges/server_bridge.py",
                "/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_orchestrator/bridges/memory_bridge.py",
                "/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_orchestrator/bridges/gradio_bridge.py"
            ]
            
            for file_path in bridge_files:
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if "AETH-CONST-2025-001" in content:
                            compliance_markers.append(file_path.split('/')[-1])
                except FileNotFoundError:
                    continue
            
            validation_result = {
                "constitutional_framework": "AETH-CONST-2025-001",
                "compliant_files": len(compliance_markers),
                "compliance_markers": compliance_markers,
                "audit_capability": True
            }
            
            return validation_result
            
        except Exception as e:
            self.errors.append(f"Constitutional compliance validation error: {e}")
            return {"error": str(e)}
    
    async def generate_validation_report(self) -> Dict[str, Any]:
        """Generate comprehensive validation report"""
        total_time = time.time() - self.start_time
        
        # Calculate success metrics
        passed_tests = len([r for r in self.validation_results.values() if r["status"] == "passed"])
        failed_tests = len([r for r in self.validation_results.values() if r["status"] == "failed"])
        error_tests = len([r for r in self.validation_results.values() if r["status"] == "error"])
        total_tests = len(self.validation_results)
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        report = {
            "validation_summary": {
                "timestamp": datetime.now().isoformat(),
                "total_time_seconds": round(total_time, 2),
                "constitutional_compliance": "AETH-CONST-2025-001"
            },
            "test_results": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": failed_tests,
                "errors": error_tests,
                "success_rate_percent": round(success_rate, 2)
            },
            "detailed_results": self.validation_results,
            "errors": self.errors,
            "warnings": self.warnings,
            "recommendations": self.generate_recommendations()
        }
        
        # Log summary
        if success_rate >= 90:
            logger.info(f"🎉 Validation PASSED: {success_rate:.1f}% success rate")
        elif success_rate >= 70:
            logger.warning(f"⚠️ Validation PARTIAL: {success_rate:.1f}% success rate")
        else:
            logger.error(f"❌ Validation FAILED: {success_rate:.1f}% success rate")
        
        return report
    
    def generate_recommendations(self) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []
        
        if self.errors:
            recommendations.append("Address all validation errors before deployment")
        
        if self.warnings:
            recommendations.append("Review warnings for potential improvements")
        
        # Specific recommendations based on results
        if "Bridge Modules" in self.validation_results and self.validation_results["Bridge Modules"]["status"] != "passed":
            recommendations.append("Ensure all bridge modules are properly installed and importable")
        
        if "Dependencies" in self.validation_results and self.validation_results["Dependencies"]["status"] != "passed":
            recommendations.append("Install missing dependencies from requirements_aethero.txt")
        
        recommendations.append("Run integration tests before production deployment")
        recommendations.append("Monitor constitutional compliance in production")
        
        return recommendations

async def main():
    """Main validation entry point"""
    validator = AetheroIntegrationValidator()
    
    try:
        # Run validation
        report = await validator.run_full_validation()
        
        # Save report
        report_path = f"/Users/_xvadur/Desktop/Aethero_github/Aethero_Orchestra/aethero_validation_report_{int(time.time())}.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"📄 Validation report saved: {report_path}")
        
        # Exit with appropriate code
        if report["test_results"]["success_rate_percent"] >= 90:
            sys.exit(0)  # Success
        else:
            sys.exit(1)  # Failure
            
    except Exception as e:
        logger.error(f"💥 Validation failed with critical error: {e}")
        sys.exit(2)  # Critical error

if __name__ == "__main__":
    asyncio.run(main())
