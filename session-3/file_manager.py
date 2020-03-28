import logging

from pathlib import Path

log = logging.getLogger(__name__)


def get_files_in_dir(path):
    if path.is_dir():
        for p in path.iterdir():
            print(p)


def list_pattern(args):
    log.info('Running kung list pattern command...')
    list_path = Path().glob(args.path)
    for file in list_path:
        print(file)


def list_files(args):
    log.info('Running kung list files command...')
    logging.debug(f'args: {args.path}')
    list_path = Path(args.path).resolve()
    if list_path.is_dir():
        get_files_in_dir(list_path)
    elif list_path.is_file():
        print(list_path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Add sub command parsers and parameters here...
    parser_list_files = subparsers.add_parser('list')
    parser_list_files.add_argument('path', help='path to list files from.')

    parser_file_pattern = subparsers.add_parser('file_pattern')
    parser_file_pattern.add_argument('path', help='path to list files from.')

    # Set functions to run for each sub parser
    parser_list_files.set_defaults(func=list_files)
    parser_file_pattern.set_defaults(func=list_pattern)

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

    # Run sub command function
    args.func(args)
