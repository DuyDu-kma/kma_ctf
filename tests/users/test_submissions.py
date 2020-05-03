#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tests.helpers import create_kmactf, destroy_kmactf, login_as_user, register_user


def test_user_get_private_solves():
    """Can a registered user load /api/v1/users/me/solves"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/api/v1/users/me/solves")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_public_solves():
    """Can a registered user load /api/v1/users/1/solves"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/api/v1/users/2/solves")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_another_public_solves():
    """Can a registered user load public solves page of another user"""
    app = create_kmactf()
    with app.app_context():
        register_user(app, name="user1", email="user1@kmactf.io")  # ID 2
        register_user(app, name="user2", email="user2@kmactf.io")  # ID 3
        client = login_as_user(app, name="user2")
        r = client.get("/api/v1/users/2/solves")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_private_fails():
    """Can a registered user load /api/v1/users/me/fails"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/api/v1/users/me/fails")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_public_fails():
    """Can a registered user load /api/v1/users/2/fails"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/api/v1/users/2/fails")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_another_public_fails():
    """Can a registered user load public fails page of another user"""
    app = create_kmactf()
    with app.app_context():
        register_user(app, name="user1", email="user1@kmactf.io")  # ID 2
        register_user(app, name="user2", email="user2@kmactf.io")  # ID 3
        client = login_as_user(app, name="user2")
        r = client.get("/api/v1/users/2/fails")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_public_team_page():
    """Can a registered user load their public profile (/profile)"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/profile")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_another_public_team_page():
    """Can a registered user load the public profile of another user (/users/1)"""
    app = create_kmactf()
    with app.app_context():
        register_user(app, name="user1", email="user1@kmactf.io")  # ID 2
        register_user(app, name="user2", email="user2@kmactf.io")  # ID 3
        client = login_as_user(app, name="user2")
        r = client.get("/users/2")
        assert r.status_code == 200
    destroy_kmactf(app)


def test_user_get_private_team_page():
    """Can a registered user load their private team page /user"""
    app = create_kmactf()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/user")
        assert r.status_code == 200
    destroy_kmactf(app)
