import config
import dtypes
import requests

user_cfg = config.USER_CFG


class RedcapRequester:
    def __init__(self, cfg):
        self._config = cfg
        self._payloader = __class__._build_payloader(cfg)


    @staticmethod
    def _build_payloader(cfg):
        def payloader(**kwargs):
            '''Constructs the payload for a request.'''
            payload = {
                'token': config['token'],
                'url': config['url'],
                'default_format': config['default_format'],
            }
            payload.update(kwargs)
            return payload
        return payloader


    def send_post_request(self, **kwargs):
        payload = self._payloader(**kwargs)
        response = requests.post(self._config['url'], payload)
        if not response.ok:
            msg = (
                "Couldn't complete request. Code "
                f"{response.status_code}: {response.reason}."
            )
            raise requests.HTTPError(msg)
        else:
            return response.json()


    def get_data_dictionary(self):
        pass
        # TODO: Implement
        # return dtypes.DataDictionary(response_data)
