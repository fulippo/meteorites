import os
import json
from werkzeug.exceptions import HTTPException
from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE"),
        charset=os.environ.get("MYSQL_CHARSET", "utf8mb4"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/healthz")
def healthz():
    # Connect to the database
    connection = get_db_connection()
    return "OK"

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# Create
@app.route('/meteorites', methods=['POST'])
def create_meteorite():
    data = request.json
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO meteorites (name, nametype, recclass, gmass, fall, year, reclat, reclong, geoLocation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (data['name'], data['nametype'], data['recclass'], data.get('gmass'),
                             data['fall'], data.get('year'), data.get('reclat'), data.get('reclong'),
                             data.get('geoLocation')))
        connection.commit()
    connection.close()
    return jsonify({'message': 'Meteorite created successfully!'}), 201

# Read
@app.route('/meteorites', methods=['GET'])
def get_meteorites():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM meteorites ORDER BY id desc LIMIT 10")
        result = cursor.fetchall()
    connection.close()
    return jsonify(result), 200

@app.route('/meteorites/<int:id>', methods=['GET'])
def get_meteorite(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM meteorites WHERE id=%s", (id,))
        result = cursor.fetchone()
    connection.close()
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'message': 'Meteorite not found!'}), 404

# Update
@app.route('/meteorites/<int:id>', methods=['PUT'])
def update_meteorite(id):
    data = request.json
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = """
        UPDATE meteorites
        SET name=%s, nametype=%s, recclass=%s, gmass=%s, fall=%s, year=%s, reclat=%s, reclong=%s, geoLocation=%s
        WHERE id=%s
        """
        cursor.execute(sql, (data['name'], data['nametype'], data['recclass'], data.get('gmass'),
                             data['fall'], data.get('year'), data.get('reclat'), data.get('reclong'),
                             data.get('geoLocation'), id))
        connection.commit()
    connection.close()
    return jsonify({'message': 'Meteorite updated successfully!'}), 200

# Delete
@app.route('/meteorites/<int:id>', methods=['DELETE'])
def delete_meteorite(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM meteorites WHERE id=%s", (id,))
        connection.commit()
    connection.close()
    return jsonify({'message': 'Meteorite deleted successfully!'}), 200

if __name__ == "__main__":
    app.run(host=os.environ.get("SERVER_HOST", "0.0.0.0"), port=os.environ.get("SERVER_PORT", "8080"), debug=os.environ.get("DEBUG", False))