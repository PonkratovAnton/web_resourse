import psycopg2

from .database import cursor, conn


class ResourceHandler:
    @staticmethod
    def get_all():
        cursor.execute('''SELECT r.id AS resource_id, r.name AS resource_name, rt.name AS resource_type, r.current_speed, rt.max_speed,
                          round(((r.current_speed - rt.max_speed) / rt.max_speed) * 100, 2) AS percent_exceed
                          FROM resource AS r
                          JOIN resource_type AS rt ON r.type_id = rt.id ORDER BY r.id;
        ''')
        column_names = [desc[0] for desc in cursor.description]
        return [dict(zip(column_names, row)) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(resource_id):
        cursor.execute('''SELECT r.id AS resource_id, r.name AS resource_name, rt.name AS resource_type, r.current_speed, rt.max_speed,
                          round(((r.current_speed - rt.max_speed) / rt.max_speed) * 100, 2) AS percent_exceed
                          FROM resource AS r JOIN resource_type AS rt ON r.type_id = rt.id 
                          WHERE r.id = %s ORDER BY r.id''', (resource_id,))
        column_names = [desc[0] for desc in cursor.description]
        return [dict(zip(column_names, row)) for row in cursor.fetchall()]

    @staticmethod
    def create(type_id, name, current_speed):
        try:
            cursor.execute(
                "INSERT INTO resource (type_id, name, current_speed) "
                "VALUES (%s, %s, %s) RETURNING *",
                (type_id, name, current_speed)
            )
            new_resource_id = cursor.fetchone()[0]
            conn.commit()
            return new_resource_id
        except psycopg2.Error as e:
            conn.rollback()
            raise e

    @staticmethod
    def get_filter_type(resource_type):
        cursor.execute('''SELECT r.id, r.name, r.current_speed
                          FROM resourse AS r
                          JOIN resourse_type AS rt ON r.type_id = rt.id
                          WHERE rt.name = %s''', resource_type)
        column_names = [desc[0] for desc in cursor.description]
        return [dict(zip(column_names, row)) for row in cursor.fetchall()]

    @staticmethod
    def update(resource_id, type_id, name, current_speed):
        try:
            cursor.execute(
                "UPDATE resource SET type_id=%s, name=%s, current_speed=%s WHERE id=%s",
                (type_id, name, current_speed, resource_id)
            )
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            raise e

    @staticmethod
    def delete(resource_id):
        try:
            cursor.execute("DELETE FROM resource WHERE id=%s", (resource_id,))
            conn.commit()
            return {"message": "Resource deleted successfully."}
        except psycopg2.Error as e:
            conn.rollback()
            raise e
