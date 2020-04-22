from flask import Blueprint, current_app
from flask_restplus import Api

from KMActf.api.v1.awards import awards_namespace
from KMActf.api.v1.challenges import challenges_namespace
from KMActf.api.v1.config import configs_namespace
from KMActf.api.v1.files import files_namespace
from KMActf.api.v1.flags import flags_namespace
from KMActf.api.v1.hints import hints_namespace
from KMActf.api.v1.notifications import notifications_namespace
from KMActf.api.v1.pages import pages_namespace
from KMActf.api.v1.scoreboard import scoreboard_namespace
from KMActf.api.v1.statistics import statistics_namespace
from KMActf.api.v1.submissions import submissions_namespace
from KMActf.api.v1.tags import tags_namespace
from KMActf.api.v1.teams import teams_namespace
from KMActf.api.v1.tokens import tokens_namespace
from KMActf.api.v1.unlocks import unlocks_namespace
from KMActf.api.v1.users import users_namespace

api = Blueprint("api", __name__, url_prefix="/api/v1")
KMActf_API_v1 = Api(api, version="v1", doc=current_app.config.get("SWAGGER_UI"))

KMActf_API_v1.add_namespace(challenges_namespace, "/challenges")
KMActf_API_v1.add_namespace(tags_namespace, "/tags")
KMActf_API_v1.add_namespace(awards_namespace, "/awards")
KMActf_API_v1.add_namespace(hints_namespace, "/hints")
KMActf_API_v1.add_namespace(flags_namespace, "/flags")
KMActf_API_v1.add_namespace(submissions_namespace, "/submissions")
KMActf_API_v1.add_namespace(scoreboard_namespace, "/scoreboard")
KMActf_API_v1.add_namespace(teams_namespace, "/teams")
KMActf_API_v1.add_namespace(users_namespace, "/users")
KMActf_API_v1.add_namespace(statistics_namespace, "/statistics")
KMActf_API_v1.add_namespace(files_namespace, "/files")
KMActf_API_v1.add_namespace(notifications_namespace, "/notifications")
KMActf_API_v1.add_namespace(configs_namespace, "/configs")
KMActf_API_v1.add_namespace(pages_namespace, "/pages")
KMActf_API_v1.add_namespace(unlocks_namespace, "/unlocks")
KMActf_API_v1.add_namespace(tokens_namespace, "/tokens")
