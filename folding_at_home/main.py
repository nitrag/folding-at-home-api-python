import argparse
from folding_at_home.api import FAHClientAPI


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Hostname or IP Address', type=str)
    parser.add_argument('--port', help='TCP Port', type=int, default=80)
    parser.add_argument('--https', help='Use HTTPS', action='store_true')
    parser.add_argument('--resume', help='Resume Folding', action='store_true')
    parser.add_argument('--pause', help='Pause Folding', action='store_true')
    parser.add_argument('--power', help='Set power level (LIGHT, MEDIUM, FULL)', type=str, default=None)
    args = parser.parse_args()

    if not args.host:
        parser.print_help()
        exit(1)

    try:
        client = FAHClientAPI(host=args.host, port=args.port, https=args.https)
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
