from mcp.server.fastmcp import FastMCP

server = FastMCP("Engineering Calculator Server")


@server.tool()
async def calculate_stress(force: float, area: float) -> str:
    if area <= 0:
        return "Error: Area must be greater than zero"

    # Stress = Force / Area (in Pascals)
    stress_pa = force / area

    # Convert Pascals to MegaPascals (1 MPa = 1,000,000 Pa)
    stress_mpa = stress_pa / 1_000_000

    return f"Stress: {stress_mpa:.4f} MPa (Force: {force} N, Area: {area} m²)"


@server.tool()
async def calculate_rpm(angular_velocity: float) -> str:
    # RPM = (rad/s) * (60 seconds/minute) / (2π radians/revolution)
    rpm = (angular_velocity * 60) / (2 * 3.14159265359)

    return f"RPM: {rpm:.2f} (Angular velocity: {angular_velocity} rad/s)"


if __name__ == "__main__":
    print("Starting Engineering Calculator MCP Server...")
    print("Available tools:")
    print("  - calculate_stress: Calculate stress from force and area")
    print("  - calculate_rpm: Calculate RPM from angular velocity (rad/s)")
    server.run()
