import pytest

@pytest.fixture
def app_settings(mocker):
    """Fixture to set config settings."""

    def factory(settings):
        """Fixture to set config settings.

        Args:
            settings (dict): Dictionary containing the app settings

        """
        mocker.patch.dict("os.environ", settings)

    return factory