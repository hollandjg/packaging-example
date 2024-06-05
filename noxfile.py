# noxfile.py
import nox


@nox.session()
def tests(session: nox.Session) -> None:
    """
    Run our tests.
    """
    session.install(".[dev]")
    session.run("pytest", *session.posargs)
