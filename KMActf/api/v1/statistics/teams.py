from flask_restplus import Resource

from KMActf.api.v1.statistics import statistics_namespace
from KMActf.models import Teams
from KMActf.utils.decorators import admins_only


@statistics_namespace.route("/teams")
class TeamStatistics(Resource):
    @admins_only
    def get(self):
        registered = Teams.query.count()
        data = {"registered": registered}
        return {"success": True, "data": data}
