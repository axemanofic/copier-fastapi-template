import subprocess
import click


@click.command()
@click.option("--host", "host", default="127.0.0.1", type=str)
@click.option("--port", "port", default="8000", type=str)
@click.option("--reload", "reload", default=True, type=str)
def run_dev(host: str, port: int, reload: bool):
    """
    This command starts the application in development mode
    """
    subprocess.run(
        [
            "uvicorn",
            "src.main:app",
            "--host",
            host,
            "--port",
            port,
            "--reload" if reload else "",
        ]
    )
