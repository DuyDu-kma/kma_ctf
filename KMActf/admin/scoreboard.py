from flask import render_template

from KMActf.admin import admin
from KMActf.scoreboard import get_standings
from KMActf.utils.decorators import admins_only


@admin.route("/admin/scoreboard")
@admins_only
def scoreboard_listing():
    standings = get_standings(admin=True)
    return render_template("admin/scoreboard.html", standings=standings)
