def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)

    except FileNotFoundError:
        print(f'Error: {filename} does not exist!')

    except Exception as e:
        print(f'Unexpected error while reading: {e}')

    finally:
        print(f'Attempted to read: {filename}')


def write_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text + '\n')
        print('Written successfully!')

    except PermissionError:
        print('Error: Permission denied.')

    except Exception as e:
        print(f'Could not write: {e}')

    finally:
        print('Write attempt complete.')


# Test both functions:
write_file('log.txt', 'Entry 1: Program started')
write_file('log.txt', 'Entry 2: Processing...')

read_file('log.txt')         # should print both entries
read_file('missing.txt')     # should show error