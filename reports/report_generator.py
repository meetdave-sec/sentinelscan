import json
import os
from datetime import datetime

REPORT_DIR = "reports"

def save_report(target, open_ports, web_findings):
    """
    Saves scan results into a structured JSON report.
    """

    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        
    report = {
        "target": target,
        "timestamp": str(datetime.now()),
        "open_ports": open_ports,
        "web_findings": web_findings
    }    

    filename = f"{REPORT_DIR}/report_{target.replace('.', '_')}.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)


    print(f"\n[+] Report saved: {filename}")    