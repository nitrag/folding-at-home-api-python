import requests
import time
from random import random


class FAHClientAPI:
    _proto = 'http'
    _host = None
    _port = None
    _sid = None

    def __init__(self, host: str, port: int = 80, https=False):
        if not host:
            raise Exception('You must provide a Host/IP to connect to.')
        self._host = host
        self._port = port
        if https:
            self._proto = 'https'
            self._port = 443 if port == 80 else port
        self._sid = self._get_session()

    def _get_session(self) -> str:
        response = requests.put(f'{self._proto}://{self._host}:{self._port}/api/session?_={random()}')
        if response.status_code == 200:
            return response.text
        else:
            raise Exception('Could not get session')

    def pause(self, pause: bool = True) -> bool:
        val = 'true' if pause else 'false'
        url = f'{self._proto}://{self._host}:{self._port}/api/set?' \
              f'pause={val}' \
              f'&sid={self._sid}&_={time.time() * 1000}'
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            raise Exception('Error pausing/resuming')

    def resume(self) -> bool:
        return self.pause(False)

    def set_power(self, power_level: str) -> bool:
        url = f'{self._proto}://{self._host}:{self._port}/api/set?' \
              f'power={power_level}' \
              f'&sid={self._sid}&_={time.time() * 1000}'
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            raise Exception('Error setting power level')
