#!/usr/bin/env python
# -*- coding: utf-8 -*-

from KMActf.config import TestingConfig
from tests.helpers import create_kmactf, destroy_kmactf, login_as_user, register_user


def test_reverse_proxy_config():
    """Test that REVERSE_PROXY configuration behaves properly"""

    class ReverseProxyConfig(TestingConfig):
        REVERSE_PROXY = "1,2,3,4"

    app = create_kmactf(config=ReverseProxyConfig)
    with app.app_context():
        assert app.wsgi_app.x_for == 1
        assert app.wsgi_app.x_proto == 2
        assert app.wsgi_app.x_host == 3
        assert app.wsgi_app.x_port == 4
        assert app.wsgi_app.x_prefix == 0
    destroy_kmactf(app)

    class ReverseProxyConfig(TestingConfig):
        REVERSE_PROXY = "true"

    app = create_kmactf(config=ReverseProxyConfig)
    with app.app_context():
        assert app.wsgi_app.x_for == 1
        assert app.wsgi_app.x_proto == 1
        assert app.wsgi_app.x_host == 1
        assert app.wsgi_app.x_port == 1
        assert app.wsgi_app.x_prefix == 1
    destroy_kmactf(app)

    class ReverseProxyConfig(TestingConfig):
        REVERSE_PROXY = True

    app = create_kmactf(config=ReverseProxyConfig)
    with app.app_context():
        assert app.wsgi_app.x_for == 1
        assert app.wsgi_app.x_proto == 1
        assert app.wsgi_app.x_host == 1
        assert app.wsgi_app.x_port == 1
        assert app.wsgi_app.x_prefix == 1
    destroy_kmactf(app)


def test_server_sent_events_config():
    """Test that SERVER_SENT_EVENTS configuration behaves properly"""

    class ServerSentEventsConfig(TestingConfig):
        SERVER_SENT_EVENTS = False

    app = create_kmactf(config=ServerSentEventsConfig)
    with app.app_context():
        register_user(app)
        client = login_as_user(app)
        r = client.get("/events")
        assert r.status_code == 204
    destroy_kmactf(app)
