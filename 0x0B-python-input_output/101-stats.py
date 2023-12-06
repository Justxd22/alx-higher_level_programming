#!/usr/bin/python3
"""Stats Script."""
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1

            if i % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")

        except (IndexError, ValueError):
            pass

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
