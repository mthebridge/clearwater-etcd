# Copyright (C) Metaswitch Networks 2016
# If license terms are provided to you in a COPYING file in the root directory
# of the source code repository by which you are accessing this code, then
# the license outlined in that COPYING file applies to your use.
# Otherwise no rights are granted except for those provided to you by
# Metaswitch Networks in a separate written agreement.

from textwrap import dedent
import ipaddress

WARNING_HEADER = dedent("""\
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# WARNING - THIS FILE IS GENERATED BY ETCD AND SHOULD NOT BE EDITED DIRECTLY
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")


def combine_ip_port(ip, port):
    """Combine an IP address (string) and a port (integer) adding brackets if
    required for an IPv6 address."""

    if ipaddress.ip_address(ip).version == 6:
        return "[{}]:{}".format(ip, port)
    else:
        return "{}:{}".format(ip, port)
