# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.

from . import ThreeMFReader
from . import ThreeMFWorkspaceReader
from UM.i18n import i18nCatalog
import UM.Platform
catalog = i18nCatalog("cura")


def getMetaData():
    # Workarround for osx not supporting double file extensions correclty.
    if UM.Platform.isOSX():
        workspace_extension = "3mf"
    else:
        workspace_extension = "curaproject.3mf"
    return {
        "plugin": {
            "name": catalog.i18nc("@label", "3MF Reader"),
            "author": "Ultimaker",
            "version": "1.0",
            "description": catalog.i18nc("@info:whatsthis", "Provides support for reading 3MF files."),
            "api": 3
        },
        "mesh_reader": [
            {
                "extension": "3mf",
                "description": catalog.i18nc("@item:inlistbox", "3MF File")
            }
        ],
        "workspace_reader":
        [
            {
                "extension": workspace_extension,
                "description": catalog.i18nc("@item:inlistbox", "3MF File")
            }
        ]
    }


def register(app):
    return {"mesh_reader": ThreeMFReader.ThreeMFReader(),
            "workspace_reader": ThreeMFWorkspaceReader.ThreeMFWorkspaceReader()}
