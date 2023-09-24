import http.server
import json

import psycopg2

from app.schemas import handlers
from app.serializer import deserialize, MyEncoder


class RequestHandler(http.server.BaseHTTPRequestHandler):

    def _send_response(self, status, content_type="application/json", body=None):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()
        if body:
            self.wfile.write(body.encode())

    def _process_request(self, method):
        parts = self.path.split('/')
        endpoint = parts[1] if len(parts) > 1 else None
        handler_info = handlers.get(f"/{endpoint}")

        if handler_info:
            handler_class = handler_info["class"]
            handler_instance = handler_class()
            resource_id = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else None
            if resource_id and f"{method}_by_id_method" in handler_info:
                handler_method = getattr(handler_instance, handler_info[f"{method}_by_id_method"])
            else:
                handler_method = getattr(handler_instance, handler_info[f"{method}_method"])
            try:
                if method in ["create", "update"]:
                    content_length = int(self.headers["Content-Length"])
                    data = deserialize(self.rfile.read(content_length).decode())
                    if method == "create":
                        new_id = handler_method(**data)
                        new_entry = handler_class.get_by_id(new_id)
                        self._send_response(201, body=json.dumps(new_entry, cls=MyEncoder))
                    else:
                        handler_method(resource_id, **data)
                        updated_entry = handler_class.get_by_id(resource_id)
                        self._send_response(200, body=json.dumps(updated_entry, cls=MyEncoder))
                elif method == "delete":
                    deleted_entries = []
                    resource_ids = [int(part) for part in parts if part.isdigit()]
                    for resource_id in resource_ids:
                        deleted_entries.append(handler_class.get_by_id(resource_id))
                        handler_method(resource_id)
                    self._send_response(200, body=json.dumps(deleted_entries, cls=MyEncoder))
                else:
                    data = handler_method(resource_id) if resource_id else handler_method()
                    self._send_response(200, body=json.dumps(data, cls=MyEncoder))
                return
            except psycopg2.Error as e:
                self._send_response(400, body=str(e))

        self._send_response(404, body="Not Found")

    def do_GET(self):
        self._process_request("get")

    def do_POST(self):
        self._process_request("create")

    def do_PUT(self):
        self._process_request("update")

    def do_DELETE(self):
        self._process_request("delete")

