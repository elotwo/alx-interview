#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line, computes metrics,
and prints statistics every 10 lines or upon termination.
"""

import sys


def print_stats(total_size, status_counts):
    """
    Print the current statistics of the log.
    Args:
        total_size (int): The accumulated file size.
        status_counts (dict): Dictionary with status code counts.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.strip().split()
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (IndexError, ValueError):
                continue

            if count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
