from pcs import (
    cluster,
    pcsd,
    resource,
    status,
    usage,
)
import pcs.cli.cluster.command as cluster_command
from pcs.cli.common.routing import create_router


cluster_cmd = create_router(
    {
        "help": lambda lib, argv, modifiers: usage.cluster(argv),
        "setup": cluster.cluster_setup,
        "sync": create_router(
            {
                "corosync": cluster.sync_nodes,
            },
            ["cluster", "sync"],
            default_cmd="corosync",
        ),
        "status": status.cluster_status,
        "pcsd-status": status.cluster_pcsd_status,
        "certkey": pcsd.pcsd_certkey,
        "auth": cluster.cluster_auth_cmd,
        "start": cluster.cluster_start_cmd,
        "stop": cluster.cluster_stop_cmd,
        "kill": cluster.kill_cluster,
        "enable": cluster.cluster_enable_cmd,
        "disable": cluster.cluster_disable_cmd,
        "cib": cluster.get_cib,
        "cib-push": cluster.cluster_push,
        "cib-upgrade": cluster.cluster_cib_upgrade_cmd,
        "edit": cluster.cluster_edit,
        "link": create_router(
            {
                "add": cluster.link_add,
                "delete": cluster.link_remove,
                "remove": cluster.link_remove,
                "update": cluster.link_update,
            },
            ["cluster", "link"]
        ),
        "node": create_router(
            {
                "add": cluster.node_add,
                "add-guest": cluster_command.node_add_guest,
                "add-outside": cluster.node_add_outside_cluster,
                "add-remote": cluster_command.node_add_remote,
                "clear": cluster_command.node_clear,
                "delete": cluster.node_remove,
                "delete-guest": cluster_command.node_remove_guest,
                "delete-remote": cluster_command.create_node_remove_remote(
                    resource.resource_remove
                ),
                "remove": cluster.node_remove,
                "remove-guest": cluster_command.node_remove_guest,
                "remove-remote": cluster_command.create_node_remove_remote(
                    resource.resource_remove
                ),
            },
            ["cluster", "node"]
        ),
        "uidgid": cluster.cluster_uidgid,
        "corosync": cluster.cluster_get_corosync_conf,
        "reload": cluster.cluster_reload,
        "destroy": cluster.cluster_destroy,
        "verify": cluster.cluster_verify,
        "report": cluster.cluster_report,
        "remove_nodes_from_cib": cluster.remove_nodes_from_cib,
    },
    ["cluster"]
)
