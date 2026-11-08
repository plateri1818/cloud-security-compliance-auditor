# Cloud Security & Compliance Auditor

## Professional Summary
An automated security auditing utility developed in **Python and SQL** to evaluate cloud infrastructure configurations against compliance benchmarks, identify high-risk misconfigurations (such as public S3 buckets and un-secured IAM roles), and automatically generate executive markdown audit reports. This project demonstrates backend data automation, risk scoring, and clear reporting workflows.

## Features
* **Automated Parsing:** Ingests JSON-based cloud asset configurations (S3 buckets, IAM users, RDS instances).
* **In-Memory SQL Evaluation:** Utilizes SQLite to query and filter assets violating security best practices.
* **Automated Reporting:** Generates structured compliance summary reports in Markdown format for stakeholders.

## Project Structure
```text
cloud-security-compliance-auditor/
├── data/
│   └── sample_configs.json       # Mock cloud infrastructure configurations
├── scripts/
│   └── audit_engine.py           # Core Python script for database ingestion and risk analysis
├── reports/
│   └── compliance_summary.md     # Auto-generated security audit output
├── requirements.txt              # Project dependencies
└── README.md
## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/plateri1818/cloud-security-compliance-auditor.git](https://github.com/plateri1818/cloud-security-compliance-auditor.git)
   