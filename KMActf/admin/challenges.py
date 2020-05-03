import os

import six
from flask import current_app as app
from flask import render_template, render_template_string, url_for

from KMActf.admin import admin
from KMActf.models import Challenges, Flags, Solves
from KMActf.plugins.challenges import get_chal_class
from KMActf.utils import binary_type
from KMActf.utils.decorators import admins_only


@admin.route("/admin/challenges")
@admins_only
def challenges_listing():
    challenges = Challenges.query.all()
    return render_template("admin/challenges/challenges.html", challenges=challenges)


@admin.route("/admin/challenges/<int:challenge_id>")
@admins_only
def challenges_detail(challenge_id):
    challenges = dict(
        Challenges.query.with_entities(Challenges.id, Challenges.name).all()
    )
    challenge = Challenges.query.filter_by(id=challenge_id).first_or_404()
    solves = (
        Solves.query.filter_by(challenge_id=challenge.id)
        .order_by(Solves.date.asc())
        .all()
    )
    flags = Flags.query.filter_by(challenge_id=challenge.id).all()
    challenge_class = get_chal_class(challenge.type)

    with open(
        os.path.join(app.root_path, challenge_class.templates["update"].lstrip("/")),
        "rb",
    ) as update:
        tpl = update.read()
        if six.PY3 and isinstance(tpl, binary_type):
            tpl = tpl.decode("utf-8")
        update_j2 = render_template_string(tpl, challenge=challenge)

    update_script = url_for(
        "views.static_html", route=challenge_class.scripts["update"].lstrip("/")
    )
    return render_template(
        "admin/challenges/challenge.html",
        update_template=update_j2,
        update_script=update_script,
        challenge=challenge,
        challenges=challenges,
        solves=solves,
        flags=flags,
    )


@admin.route("/admin/challenges/new")
@admins_only
def challenges_new():
    return render_template("admin/challenges/new.html")
