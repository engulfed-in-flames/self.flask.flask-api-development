# Define general-purpose fixtures

import os
import pytest
from dotenv import load_dotenv
from app import create_app

env_file_name = ".env.test"
root_dir_path = os.path.dirname(__file__)
env_file_path = os.path.join(root_dir_path, env_file_name)
load_dotenv(env_file_path)
print(env_file_path)

# import requests
# @pytest.fixture(autouse=True)
# def disable_network_calls(monkeypatch) -> None:
#     def stunted_get():
#         raise RuntimeError("Network access not allowed during testing!")

#     monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())


@pytest.fixture()
def app():
    app = create_app()

    # Other setup

    yield app

    # Clean up


@pytest.fixture()
def client(app):
    return app.test_client()  # Extends Werkzeug's client.


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
