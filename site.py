import click

import yaml
@click.command()
@click.argument('NAME', default='World')
def main(name):
    print(f"Hello {name}!!")


if __name__ == '__main__':
    main()
