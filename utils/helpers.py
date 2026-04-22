def print_result(level, message):
    """
    Standardized output formatter for scanner results.
    """

    levels = {
        "INFO": "[INFO]",
        "LOW": "[LOW]",
        "MEDIUM": "[MEDIUM]",
        "HIGH": "[HIGH]",
        "OK": "[OK]"
    }

    prefix = levels.get(level, "[INFO]")
    print(f"{prefix} {message}")
