from typing import Dict


def site_settings(request) -> Dict[str, str]:
    """Provee configuraciones comunes a las plantillas.

    Actúa como un mesero que siempre entrega la misma jarra de agua en cada mesa,
    garantizando que todas las vistas tengan a mano el nombre del sitio.
    """

    return {"site_name": "CATT"}
