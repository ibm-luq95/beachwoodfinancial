# -*- coding: utf-8 -*-#
import argparse
import configparser
from termcolor import colored, cprint
from pathlib import PosixPath


def run(args: argparse.Namespace) -> None:

    def create(args: argparse.Namespace, stage_env_file: PosixPath, force: bool) -> None:
        if force is True:
            cprint(
                colored(
                    f"########################### Replace {stage_file} ###########################",
                    "yellow",
                )
            )
            stage_file.unlink()
        stage_file.touch()
        config = configparser.ConfigParser()
        config.read(stage_env_file)
        stage_name = args.stage_name
        config.add_section("environment")
        config.set("environment", "STAGE_ENVIRONMENT", stage_name.upper())
        with open(stage_env_file, "w") as configfile:
            config.write(configfile)
        cprint(
            colored(f"Stage file created: {stage_env_file} successfully", "green"),
            attrs=["bold"],
        )

    cwd = PosixPath.cwd().parent
    src_folder: PosixPath = cwd / "src"
    env_folder: PosixPath = src_folder / ".env"
    stage_file: PosixPath = env_folder / ".current_stage"
    if args.delete_only is True:
        cprint(
            colored(
                f"########################### Deleting {stage_file.relative_to(cwd)} ###########################",
                "blue",
            ),
            # attrs=["blink"]
        )
        if stage_file.exists() is False:
            cprint(
                colored(f"Stage file not exists: {stage_file.relative_to(cwd)}", "yellow"),
                attrs=["bold", "underline"],
            )
            return
        stage_file.unlink()
        cprint(
            colored(f"Stage file deleted: {stage_file} successfully", "green"),
            attrs=["bold"],
        )
        return
    if stage_file.exists() is True:
        if args.force is True:

            create(args, stage_file, True)
        else:
            cprint(colored(f"Stage file already exists!!!", "yellow"))
            cprint(colored(stage_file, "cyan"), attrs=["bold", "underline"])
            return
    create(args, stage_file, False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create stage file")
    parser.add_argument(
        "-f",
        "--force",
        help="Force create stage file replace the existing stage file",
        action="store_true",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-d",
        "--delete-only",
        help="Only delete stage file",
        action="store_true",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-n",
        "--stage-name",
        help="Stage name for current environment",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    run(args)
