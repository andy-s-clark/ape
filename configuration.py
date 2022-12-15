import json
from os import getenv


# Map of configuration names and their defaults.
# ex. config = Configuration({"my_setting": "My Default"})
# Will use "My Default" if "MY_SETTING" is not an environment variable.
# Attempts to decode JSON from the environment variable.
# Uses subscript-able references:
# ex. config["my_setting"]
class Configuration(dict):
    def __init__(self, env_config_defaults: dict) -> None:
        super().__init__()
        for name, default in env_config_defaults.items():
            self.__setitem__(name, self._get_configuration_item(name, default))

    @staticmethod
    def _get_configuration_item(name: str, default) -> any:
        env_value = getenv(name.upper())
        if env_value is None:
            return default
        else:
            try:
                return json.loads(env_value)
            except json.decoder.JSONDecodeError:
                return env_value

    def __getitem__(self, name) -> any:
        return super().__getitem__(name)

    def __setitem__(self, name, value) -> None:
        super().__setitem__(name, value)

    def __repr__(self) -> str:
        redacted = {}
        for name, value in super().items():
            if value is None:
                redacted[name] = "None"
            elif "secret" in name and len(value) > 0:
                redacted[name] = "********"
            else:
                redacted[name] = value
        return json.dumps(redacted)
