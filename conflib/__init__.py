#!/usr/bin/env python3

from .common import (
    KERNEL_TYPE,
    File,
    FileReader,
    FileJson,
    mkdir,
    get_user_home,
    get_abspath,
    BuilderUserDirs,
    BuilderAppDirs,
)

from .version import (
    __version__,
    __repo__,
)

if KERNEL_TYPE == 'Linux':
    from .common import (
        AppDirsLinux as AppDirs,
        UserDirsLinux as UserDirs,
    )
elif KERNEL_TYPE == 'Windows':
    from .common import (
        AppDirsWindows as AppDirs,
        UserDirsWindows as UserDirs,
    )
