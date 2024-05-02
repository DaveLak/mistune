import atheris
import sys

with atheris.instrument_imports():
    import mistune


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    mistune.html(fdp.ConsumeUnicode(fdp.remaining_bytes()))


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
