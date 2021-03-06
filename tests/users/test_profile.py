#!/usr/bin/env python
# -*- coding: utf-8 -*-

from KMActf.models import Users
from KMActf.utils.crypto import verify_password
from tests.helpers import create_kmactf, destroy_kmactf, login_as_user, register_user


def test_email_cannot_be_changed_without_password():
    """Test that a user can't update their email address without current password"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)

        data = {"name": "user", "email": "user2@kmactf.io"}

        r = client.patch("/api/v1/users/me", json=data)
        assert r.status_code == 400
        user = Users.query.filter_by(id=2).first()
        assert user.email == "user@kmactf.io"

        data = {"name": "user", "email": "user2@kmactf.io", "confirm": "asdf"}

        r = client.patch("/api/v1/users/me", json=data)
        assert r.status_code == 400
        user = Users.query.filter_by(id=2).first()
        assert user.email == "user@kmactf.io"

        data = {"name": "user", "email": "user2@kmactf.io", "confirm": "password"}

        r = client.patch("/api/v1/users/me", json=data)
        assert r.status_code == 200
        user = Users.query.filter_by(id=2).first()
        assert user.email == "user2@kmactf.io"
        assert verify_password(plaintext="password", ciphertext=user.password)
    destroy_kmactf(app)
