import shutil
from pathlib import Path

from auto.file_extension import FileExtension
from auto.utils import AutoUtils


def test_generate():
    AutoUtils.generate(
        name="testing",
        extension=FileExtension.Python,
        author="testco",
        dir=Path(Path.cwd(), "var"),
        content="print(1 + 1)\n",
    )

    target = Path(Path.cwd(), "var/.auto_testing.py")

    try:
        with target.open("r") as f:
            assert f.read() == \
                """\"""
Do not modify, auto-generated by testco
\"""

print(1 + 1)

"""
    finally:
        target.unlink()


def test_clean():
    vardir = Path(Path.cwd(), "var")

    for path in [
        Path(vardir, ".auto_test1.js"),
        Path(vardir, ".auto_test2.py"),
        Path(vardir, ".auto_test3.ts"),
    ]:
        with path.open("w+") as f:
            f.write("whocares")

    try:
        AutoUtils.clean(vardir)
    finally:
        shutil.rmtree(vardir)
