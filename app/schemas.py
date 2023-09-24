from app.resource_handler import ResourceHandler
from app.resource_type_handler import ResourceTypeHandler


handlers = {
    "/resource": {
        "class": ResourceHandler,
        "get_method": "get_all",
        "get_by_id_method": "get_by_id",
        "filter_type_method": "get_filter_type",
        "create_method": "create",
        "update_method": "update",
        "delete_method": "delete",
    },
    "/resource_type": {
        "class": ResourceTypeHandler,
        "get_method": "get_all",
        "get_by_id_method": "get_by_id",
        "create_method": "create",
        "update_method": "update",
        "delete_method": "delete",
    },
}
