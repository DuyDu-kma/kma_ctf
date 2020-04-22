from flask import Blueprint, render_template

from KMActf.utils import config, get_config
from KMActf.utils.dates import ctf_ended, ctf_paused, view_after_ctf
from KMActf.utils.decorators import (
    during_ctf_time_only,
    require_team,
    require_verified_emails,
)
from KMActf.utils.decorators.visibility import check_challenge_visibility
from KMActf.utils.helpers import get_errors, get_infos

challenges = Blueprint("challenges", __name__)


@challenges.route("/challenges", methods=["GET"])
@during_ctf_time_only
@require_verified_emails
@check_challenge_visibility
@require_team
def listing():
    infos = get_infos()
    errors = get_errors()
    start = get_config("start") or 0
    end = get_config("end") or 0

    if ctf_paused():
        infos.append("{} is paused".format(config.ctf_name()))

    # CTF has ended but we want to allow view_after_ctf. Show error but let JS load challenges.
    if ctf_ended() and view_after_ctf():
        infos.append("{} has ended".format(config.ctf_name()))

    return render_template(
        "challenges.html", infos=infos, errors=errors, start=int(start), end=int(end)
    )
