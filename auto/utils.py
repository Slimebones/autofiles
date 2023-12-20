from glob import glob
import os
from pathlib import Path
from pykit.cls import Static

from auto.file_extension import FileExtension, FileExtensionUtils


class AutoUtils(Static):
    @staticmethod
    def generate(
        *,
        name: str,
        extension: FileExtension,
        author: str,
        dir: Path,
        content: str
    ) -> None:
        if not dir.is_dir():
            raise ValueError(f"{dir} is not dir")

        res = ""
        res += FileExtensionUtils.get(extension, author)
        # an additional whiteline for the separation, although headers should
        # have a default one
        res += "\n"
        res += content

        target_path = Path(dir, f".auto_{name}")
        with target_path.open("w+") as f:
            f.write(res)

    @staticmethod
    def clean(dir: Path) -> None:
        """
        Removes all .auto_ prefixed files in the given dir and all subdirs.
        """
        if not dir.is_dir:
            raise ValueError(f"{dir} is not a directory")

        files = glob(
            ".auto_*", root_dir=dir, recursive=True, include_hidden=True
        )

        for f in files:
            os.remove(f)
