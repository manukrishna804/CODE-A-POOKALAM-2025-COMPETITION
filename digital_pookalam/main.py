from .pookalam import DigitalPookalam
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a Digital Pookalam")
    parser.add_argument('--save', help='Filename to save Pookalam image', default=None)
    args = parser.parse_args()

    p = DigitalPookalam()
    if args.save:
        p.save(args.save)
    else:
        p.show()

if __name__ == "__main__":
    main()
