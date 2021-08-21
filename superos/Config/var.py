import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from superos.Config.legend_config import Config
else:
    if os.path.exists("config.py"):
        from superos.Config.Config import Development as Var
