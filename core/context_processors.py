from typing import Dict

def site_settings(request) -> Dict[str, str]:
    """Provide common site settings to templates."""
    return {"site_name": "CATT"}
