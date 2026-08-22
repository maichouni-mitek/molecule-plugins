from types import SimpleNamespace

import pytest

from molecule import api
from molecule_plugins.ec2.driver import EC2


def test_ec2_driver_is_detected():
    assert "ec2" in [str(d) for d in api.drivers()]


@pytest.mark.parametrize("config_attribute", ["config", "config_data"])
def test_ec2_driver_supports_molecule_config_attributes(config_attribute):
    platforms = [{"name": "instance"}]
    driver = EC2(SimpleNamespace(**{config_attribute: {"platforms": platforms}}))

    assert driver.platforms == platforms
