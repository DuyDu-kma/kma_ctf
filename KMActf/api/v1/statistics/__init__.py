from flask_restplus import Namespace

statistics_namespace = Namespace(
    "statistics", description="Endpoint to retrieve Statistics"
)

from KMActf.api.v1.statistics import challenges  # noqa: F401
from KMActf.api.v1.statistics import submissions  # noqa: F401
from KMActf.api.v1.statistics import teams  # noqa: F401
from KMActf.api.v1.statistics import users  # noqa: F401
