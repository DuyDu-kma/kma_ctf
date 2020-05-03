#!/usr/bin/env python
# -*- coding: utf-8 -*-

from KMActf.utils import get_config
from KMActf.utils.security.csrf import generate_nonce
from KMActf.utils.security.signing import serialize
from tests.helpers import create_kmactf, destroy_kmactf, login_as_user, register_user


def test_setup_integrations():
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        user = login_as_user(app)
        r = user.get("/setup/integrations")
        assert r.status_code == 403

        admin = login_as_user(app, "admin")
        r = admin.get("/setup/integrations")
        assert r.status_code == 403

        admin = login_as_user(app, "admin")

        url = "/setup/integrations?state={state}&mlc_client_id=client_id&mlc_client_secret=client_secret&name=mlc".format(
            state=serialize(generate_nonce())
        )
        r = admin.get(url)
        assert r.status_code == 200
        assert get_config("oauth_client_id") == "client_id"
        assert get_config("oauth_client_secret") == "client_secret"
    destroy_kmactf(app)
