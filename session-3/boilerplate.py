import logging

log = logging.getLogger(__name__)


def main(args):
    log.info('Hello world!')
    log.debug('This will only show on debug levels...')
    log.error('Something went wrong!')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    # Add your own script parameters here...

    # Default parameters and parameter initialization
    parser.add_argument(
        '-L', '--log-level',
        help='set log level',
        default='INFO',
    )
    parser.add_argument(
        '--log-file',
        help='set log file',
    )
    args = parser.parse_args()

    # Configure logging
    log_params = {
        'filename': args.log_file,
        'level': getattr(logging, args.log_level.upper()),
        'format': (
            '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
        ),
    }
    logging.basicConfig(**log_params)

    # Run
    main(args)
