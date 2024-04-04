def _reset_logging(cls):
	"""
	Reset
	"""
	print("\n[+] Reset logging")
	cls.logging = False
	cls.logging_dir = None
	cls.logging_files = None

@click.command(help="Start logging")
@click.option(
	"--logging-dir",
	type=click.Path(exists=True, dir_okay=False, file_okay=True, readable=True),
	required=True,
	help="Logging directory",
)
@click.option(
	"--logging-files",
	type=click.Path(exists=True, dir_okay=False, file_okay=True, readable=True),
	required=True,
	help="Logging files",
)
