import psycopg2

from .database import cursor, conn


class ResourceTypeHandler:

    @staticmethod
    def get_all():
        cursor.execute("SELECT * FROM resource_type")
        column_names = [desc[0] for desc in cursor.description]
        return [dict(zip(column_names, row)) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(resource_id):
        cursor.execute("SELECT * FROM resource_type WHERE id = %s", (resource_id,))
        column_names = [desc[0] for desc in cursor.description]
        return [dict(zip(column_names, row)) for row in cursor.fetchall()]

    @staticmethod
    def create(name, max_speed):
        try:
            cursor.execute(
                "INSERT INTO resource_type (name, max_speed) VALUES (%s, %s) RETURNING *",
                (name, max_speed)
            )
            new_resource_type_id = cursor.fetchone()[0]
            conn.commit()
            return new_resource_type_id
        except psycopg2.Error as e:
            conn.rollback()
            raise e

    @staticmethod
    def update(resource_type_id, name, max_speed):
        try:
            cursor.execute(
                "UPDATE resource_type SET name=%s, max_speed=%s WHERE id=%s",
                (name, max_speed, resource_type_id)
            )
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            raise e

    @staticmethod
    def delete(resource_type_id):
        try:
            cursor.execute("DELETE FROM resource_type WHERE id=%s", (resource_type_id,))
            conn.commit()
            return {"message": "Resource Type deleted successfully."}
        except psycopg2.Error as e:
            conn.rollback()
            raise e
