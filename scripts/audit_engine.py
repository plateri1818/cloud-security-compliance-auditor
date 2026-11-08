import sqlite3
import json
import os

def run_audit():
    print("Initializing Cloud Security Compliance Audit...")
    
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create table for assets
    cursor.execute('''
        CREATE TABLE assets (
            asset_id TEXT,
            type TEXT,
            public_access BOOLEAN,
            encryption_enabled BOOLEAN,
            mfa_enabled BOOLEAN,
            excessive_permissions BOOLEAN,
            environment TEXT
        )
    ''')
    
    # Load sample configurations
    config_path = os.path.join("data", "sample_configs.json")
    if not os.path.exists(config_path):
        print(f"Error: Could not find {config_path}")
        return

    with open(config_path, "r") as f:
        data = json.load(f)
        
    # Insert mock data into database
    for asset in data.get("cloud_assets", []):
        cursor.execute('''
            INSERT INTO assets VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            asset.get("asset_id"),
            asset.get("type"),
            asset.get("public_access", False),
            asset.get("encryption_enabled", True),
            asset.get("mfa_enabled", True),
            asset.get("excessive_permissions", False),
            asset.get("environment", "unknown")
        ))
        
    # Run security checks (Find misconfigurations)
    cursor.execute('''
        SELECT asset_id, type FROM assets 
        WHERE public_access = 1 OR mfa_enabled = 0 OR excessive_permissions = 1
    ''')
    violations = cursor.fetchall()
    
    # Generate Markdown Report
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "compliance_summary.md")
    
    report_content = "# Cloud Security Compliance Audit Report\n\n"
    report_content += "## Overview\nAutomated scan completed against cloud infrastructure assets.\n\n"
    report_content += f"**Total Violations Found:** {len(violations)}\n\n"
    report_content += "## Flagged Misconfigurations\n"
    report_content += "| Asset ID | Asset Type | Risk Status |\n|---|---|---|\n"
    
    for v in violations:
        report_content += f"| {v[0]} | {v[1]} | High Risk / Non-Compliant |\n"
        
    with open(report_path, "w") as r_file:
        r_file.write(report_content)
        
    print(f"Audit complete! Report successfully generated at: {report_path}")
    conn.close()

if __name__ == "__main__":
    run_audit()

    