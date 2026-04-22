import os

REPORT_DIR = "reports"


def generate_html_report(target, open_ports, web_findings):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    filename = f"{REPORT_DIR}/report_{target.replace('.', '_')}.html"

    html = f"""
    <html>
    <head>
        <title>SentinelScan Report - {target}</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #111;
                color: #fff;
                padding: 20px;
            }}
            .box {{
                background: #222;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
            }}
            .high {{ color: red; }}
            .medium {{ color: orange; }}
            .low {{ color: yellow; }}
            .ok {{ color: lightgreen; }}
        </style>
    </head>

    <body>
        <h1>SentinelScan Security Report</h1>
        <h3>Target: {target}</h3>

        <div class="box">
            <h2>Open Ports</h2>
            {"".join([f"<p>{p[0]} ({p[1]})</p>" for p in open_ports])}
        </div>

        <div class="box">
            <h2>Web Vulnerabilities</h2>
            {"".join([
                f"<p class='{f['severity'].lower()}'>{f['issue']} - {f['severity']}</p>"
                for f in web_findings
            ])}
        </div>

    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html)

    print(f"\n[+] HTML Report generated: {filename}")
