SECURITY_HEADERS_RULES = {
    "Content-Security-Policy": {
        "severity": "HIGH",
        "description": "Prevents XSS and injection attacks"
    },
    "X-Frame-Options": {
        "severity": "MEDIUM",
        "description": "Prevents clickjacking attacks"
    },
    "X-XSS-Protection": {
        "severity": "LOW",
        "description": "Legacy XSS protection header"
    },
    "Strict-Transport-Security": {
        "severity": "HIGH",
        "description": "Forces HTTPS usage"
    }
}
