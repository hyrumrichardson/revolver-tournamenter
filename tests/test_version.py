import packaging.version

import revolver


def test_version_is_valid() -> None:
    _ = packaging.version.parse(revolver.__version__)
