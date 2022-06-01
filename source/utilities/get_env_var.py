from sys import exit
from os import environ


def get_env_var(variable_name: str, default: str = None) -> str:

  if not (variable := environ.get(variable_name)) and not default:
    exit(print('No Environment Variable:', variable_name))

  return variable or default
