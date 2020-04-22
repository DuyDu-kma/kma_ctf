#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.helpers import create_kmactf, destroy_kmactf, gen_user


def test_kmactf_setup_redirect():
    """Test that a fresh KMActf instance redirects to /setup"""
    app = create_kmactf(setup=False)
    with app.app_context():
        with app.test_client() as client:
            r = client.get("/users")
            assert r.status_code == 302
            assert r.location == "http://localhost/setup"

            # Files in /themes load properly
            r = client.get("/themes/core/static/css/main.dev.css")
            r = client.get("/themes/core/static/css/main.min.css")
            assert r.status_code == 200
    destroy_kmactf(app)


def test_kmactf_setup_verification():
    app = create_kmactf(setup=False)
    with app.app_context():
        with app.test_client() as client:
            r = client.get("/setup")
            assert r.status_code == 200

            with client.session_transaction() as sess:
                data = {
                    "ctf_name": "KMActf",
                    "ctf_description": "CTF description",
                    "name": "test",
                    "email": "test@kmactf.io",
                    "password": "",
                    "user_mode": "users",
                    "nonce": sess.get("nonce"),
                }
            r = client.post("/setup", data=data)
            assert "longer password" in r.get_data(as_text=True)

            gen_user(app.db, name="test", email="test@kmactf.io")

            data["password"] = "password"
            r = client.post("/setup", data=data)
            resp = r.get_data(as_text=True)
            assert "email has already been used" in resp
            assert "name is already taken" in resp

            data["name"] = "admin"
            data["email"] = "admin@kmactf.io"
            r = client.post("/setup", data=data)
            assert r.status_code == 302
            assert r.location == "http://localhost/"
    destroy_kmactf(app)
