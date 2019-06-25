# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

"""
Create command.
"""

from paconn import _CREATE
from paconn.common.util import display
from paconn.settings.util import load_settings_and_powerapps_rp
from paconn.operations.upsert import upsert


# pylint: disable=too-many-arguments
def create(
        environment,
        api_properties,
        api_definition,
        icon,
        powerapps_url,
        powerapps_version,
        client_secret,
        settings_file,
        overwrite_settings):
    """
    Create command.
    """
    settings, powerapps_rp, _ = load_settings_and_powerapps_rp(
        environment=environment,
        settings_file=settings_file,
        api_properties=api_properties,
        api_definition=api_definition,
        icon=icon,
        connector_id=None,
        powerapps_url=powerapps_url,
        powerapps_version=powerapps_version,
        command_context=_CREATE)

    connector_id = upsert(
        powerapps_rp=powerapps_rp,
        settings=settings,
        client_secret=client_secret,
        is_update=False,
        overwrite_settings=overwrite_settings)

    display('{} created successfully.'.format(connector_id))
