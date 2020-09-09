import urllib3
import click
from vmanage.device import cli_device
from vmanage.template import cli_template
from vmanage.bfd import cli_bfd
from vmanage.sla import cli_sla
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.group()
def cli():
    """Command line tool for deploying templates to CISCO SDWAN.
    """
    pass


cli.add_command(cli_device)
cli.add_command(cli_template)
cli.add_command(cli_bfd)
cli.add_command(cli_sla)


if __name__ == "__main__":
    cli()
