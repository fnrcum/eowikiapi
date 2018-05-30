def check_url_params_set(params) -> bool:
    for key, value in params.items():
        if value is not None:
            return True
    return False


def str2bool(v):
  return v in ["yes", "true", "t", "1", "True", "true"]