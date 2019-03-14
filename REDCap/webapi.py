import config

user_cfg = config.USER_CFG

def _build_payloader(config):
    def payloader(**kwargs):
        payload = {
            'token': config.token,
            'format': config.,
        }
        payload.update(kwargs)
        return payload
    return payloader


def send_request(**kwargs):
    payload = _build_payload(**kwargs)
    response = requests.post(_URL, payload)
    if not response.ok:
        msg = (
            "Couldn't complete request. Code "
            f"{response.status_code}: {response.reason}."
        )
        raise RedcapError(msg)
    else:
        return response.json()


class RedcapRequest:
    def __init__(self, cfg):
        self._config = cfg
        self._payloader = self._build_payloader(cfg)

    def _build_payloader(self, cfg):
