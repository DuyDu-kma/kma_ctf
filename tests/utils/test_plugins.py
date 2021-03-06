from KMActf.plugins import register_plugin_script
from KMActf.utils.plugins import override_template
from tests.helpers import create_kmactf, destroy_kmactf, login_as_user


def test_override_template():
    """Does override_template work properly for regular themes"""
    app = create_kmactf()
    with app.app_context():
        override_template("login.html", "LOGIN OVERRIDE")
        with app.test_client() as client:
            r = client.get("/login")
            assert r.status_code == 200
            output = r.get_data(as_text=True)
            assert "LOGIN OVERRIDE" in output
    destroy_kmactf(app)


def test_admin_override_template():
    """Does override_template work properly for the admin panel"""
    app = create_kmactf()
    with app.app_context():
        override_template("admin/users/user.html", "ADMIN TEAM OVERRIDE")
        client = login_as_user(app, name="admin", password="password")
        r = client.get("/admin/users/1")
        assert r.status_code == 200
        output = r.get_data(as_text=True)
        assert "ADMIN TEAM OVERRIDE" in output
    destroy_kmactf(app)


def test_register_plugin_script():
    """Test that register_plugin_script adds script paths to the core theme"""
    app = create_kmactf()
    with app.app_context():
        register_plugin_script("/fake/script/path.js")
        register_plugin_script("http://kmactf.io/fake/script/path.js")
        with app.test_client() as client:
            r = client.get("/")
            output = r.get_data(as_text=True)
            assert "/fake/script/path.js" in output
            assert "http://kmactf.io/fake/script/path.js" in output
    destroy_kmactf(app)


def test_register_plugin_stylesheet():
    """Test that register_plugin_stylesheet adds stylesheet paths to the core theme"""
    app = create_kmactf()
    with app.app_context():
        register_plugin_script("/fake/stylesheet/path.css")
        register_plugin_script("http://kmactf.io/fake/stylesheet/path.css")
        with app.test_client() as client:
            r = client.get("/")
            output = r.get_data(as_text=True)
            assert "/fake/stylesheet/path.css" in output
            assert "http://kmactf.io/fake/stylesheet/path.css" in output
    destroy_kmactf(app)
