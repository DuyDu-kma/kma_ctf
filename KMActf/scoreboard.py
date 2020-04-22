from flask import Blueprint, render_template

from KMActf.cache import cache, make_cache_key
from KMActf.utils import config
from KMActf.utils.decorators.visibility import check_score_visibility
from KMActf.utils.scores import get_standings

scoreboard = Blueprint("scoreboard", __name__)


@scoreboard.route("/scoreboard")
@check_score_visibility
@cache.cached(timeout=60, key_prefix=make_cache_key)
def listing():
    standings = get_standings()
    return render_template(
        "scoreboard.html",
        standings=standings,
        score_frozen=config.is_scoreboard_frozen(),
    )
