def foo(bar):

    result = str(bar) + " is "
    if bar:
        result += str(True)
    else:
        result += str(False)

    return result


try:
    import io
except Exception as e: # pragma: no cover
    print("io not available, importing StringIO")
    import StringIO as io


def main():
    s = io.StringIO()
    print s


if __name__ == '__main__':
    main()
