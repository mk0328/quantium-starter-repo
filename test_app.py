import pytest
from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Visualiser", timeout=10)
    assert dash_duo.find_element("h1") is not None

def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart") is not None

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=10)
    assert dash_duo.find_element("#region-radio") is not None