import sys
# import os

# from sqlalchemy import create_engine

# from dotenv import load_dotenv

from alembic import command
from alembic.config import CommandLine, Config

from db_conf import ENGINE
# load_dotenv(".env")
# DATABASE_URL = os.environ["DATABASE_URL"]

# def pg_db_connection_factory():
#     return create_engine(DATABASE_URL)


def create_migration(args: list[str] = sys.argv):
    if len(args) != 2:
        print("specify the migration message as the second arg")
        return

    # the first argument (index 0) is function name.
    msg = args[1]

    alembic_cfg = Config("alembic.ini")

    with ENGINE.connect() as connection:
        alembic_cfg.attributes["connection"] = connection
        command.revision(
            config=alembic_cfg,
            message=msg,
            autogenerate=False,
        )

    ENGINE.dispose()


def generate_migrations(args: list[str] = sys.argv):
    if len(args) != 2:
        print("specify the migration message as the second arg")
        return

    # the first argument (index 0) is function name.
    msg = args[1]

    namespace = CommandLine().parser.parse_args(["revision", "--autogenerate"])
    alembic_cfg = Config("alembic.ini", cmd_opts=namespace)

    with ENGINE.connect() as connection:
        alembic_cfg.attributes["connection"] = connection
        command.revision(
            config=alembic_cfg,
            message=msg,
            autogenerate=True,
        )

    ENGINE.dispose()


def downgrade_migration(args: list[str] = sys.argv):
    if len(args) != 2:
        print("specify the revision target as the second arg")
        return

    # the first argument (index 0) is function name.
    revision = args[1]

    alembic_cfg = Config("alembic.ini")

    with ENGINE.connect() as connection:
        alembic_cfg.attributes["connection"] = connection
        command.downgrade(alembic_cfg, revision)

    ENGINE.dispose()


def upgrade_migration(args: list[str] = sys.argv):
    arg_length = len(args)

    if arg_length > 2 or arg_length < 1:
        print("specify the revision target as the second arg")
        return

    # the first argument (index 0) is function name.
    revision = "head" if arg_length == 1 else args[2]

    alembic_cfg = Config("alembic.ini")

    with ENGINE.connect() as connection:
        alembic_cfg.attributes["connection"] = connection
        command.upgrade(alembic_cfg, revision)

    ENGINE.dispose()