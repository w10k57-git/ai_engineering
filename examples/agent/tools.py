import logging
import os

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for the TRIZ Contradictions MCP server."""
    mcp = FastMCP(
        "TRIZ Contradictions MCP Server",
        host="127.0.0.1",
        port=int(os.getenv("MCP_PORT", 8021)),
        stateless_http=True,
    )

    @mcp.tool()
    async def calculate_rpm(angular_velocity: float) -> str:
        # RPM = (rad/s) * (60 seconds/minute) / (2π radians/revolution)
        rpm = (angular_velocity * 60) / (2 * 3.14159265359)

        return f"RPM: {rpm:.2f} (Angular velocity: {angular_velocity} rad/s)"

    @mcp.tool()
    async def calculate_stress(force: float, area: float) -> str:
        if area <= 0:
            return "Error: Area must be greater than zero"

        # Stress = Force / Area (in Pascals)
        stress_pa = force / area

        # Convert Pascals to MegaPascals (1 MPa = 1,000,000 Pa)
        stress_mpa = stress_pa / 1_000_000

        return f"Stress: {stress_mpa:.4f} MPa (Force: {force} N, Area: {area} m²)"

    # Run the server
    logger.info("🚀 Starting traicon MCP Server...")
    try:
        mcp.run(transport="streamable-http")
    except KeyboardInterrupt:
        logger.info("🛑 Engineering Tools Server shutting down...")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
    finally:
        logger.info("✅ Engineering Tools Server exited. Thanks for using Engineering Tools!")


if __name__ == "__main__":
    main()
