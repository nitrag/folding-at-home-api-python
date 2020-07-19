
import argparse
import requests
import time
from random import random


class FAHClientAPI:
    _proto = 'https'
    _host = None
    _port = None
    _sid = None

    def __init__(self, host, port, http = False):
        if not host:
            raise Exception('You must provide a Host/IP to connect to.')
        if http:
            self._proto = 'http'
        self._host = host
        self._port = port
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

    def resume(self):
        self.pause(False)

    def set_power(self, power_level: str):
        url = f'{self._proto}://{self._host}:{self._port}/api/set?' \
              f'power={power_level}' \
              f'&sid={self._sid}&_={time.time() * 1000}'
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            raise Exception('Error setting power level')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Hostname or IP Address', type=str)
    parser.add_argument('--port', help='TCP Port', type=int, default=80)
    parser.add_argument('--http', help='Use HTTP instead of HTTPS', action='store_true')
    parser.add_argument('--resume', help='Resume Folding', action='store_true')
    parser.add_argument('--pause', help='Pause Folding', action='store_true')
    parser.add_argument('--power', help='Set power level (LIGHT, MEDIUM, FULL)', type=str, default=None)
    args = parser.parse_args()

    try:
        client = FAHClientAPI(host=args.host, port=args.port, http=args.http)
        if args.pause:
            client.pause()
            print('Folding Paused')
        elif args.resume:
            client.resume()
            print('Folding Resumed')
        elif args.power:
            power = args.power.upper()
            if power not in ['LIGHT', 'MEDIUM', 'FULL']:
                raise Exception('Invalid power level')
            client.set_power(power)
            print(f'Set power level to {power}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
