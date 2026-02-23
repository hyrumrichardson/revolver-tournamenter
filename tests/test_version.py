import packaging.version

import revolver-tournamenter


def test_version_is_valid() -> None:
    _ = packaging.version.parse(template_python.__version__)
