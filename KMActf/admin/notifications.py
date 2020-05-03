from flask import render_template

from KMActf.admin import admin
from KMActf.models import Notifications
from KMActf.utils.decorators import admins_only


@admin.route("/admin/notifications")
@admins_only
def notifications():
    notifs = Notifications.query.order_by(Notifications.id.desc()).all()
    return render_template("admin/notifications.html", notifications=notifs)
