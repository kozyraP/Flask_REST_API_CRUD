import sqlite3
import jsonpickle

from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from Employee import Employee

app = Flask(__name__)


@app.route('/api/employee', methods=['GET'])
def get_method():
    employees = []
    query = 'SELECT rowid, birth_day, email, name, phone_number FROM employee;'
    connection = sqlite3.connect('company.db')
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        employees.append(Employee(row[0], row[1], row[2], row[3], row[4]))
    connection.close()
    return Response(jsonpickle.encode(employees, unpicklable=False), mimetype='application/json')


@app.route('/api/employee', methods=['POST'])
def post_method():
    request_data = request.get_json()
    try:
        connection = sqlite3.connect('company.db')
        name = request_data.get('name')
        birth_day = request_data.get('birth_day')
        email = request_data.get('email')
        phone_number = request_data.get('phone_number')
        cursor = connection.cursor()
        query = f'''INSERT INTO employee (name,birth_day,email,phone_number)
                VALUES('{name}', '{birth_day}', '{email}', '{phone_number}');'''
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as err:
        print(str(err))
        return jsonify(details=str(err)), 400
    finally:
        connection.close()
    return request_data, 201


@app.route('/api/employee/<employee_id>', methods=['PUT'])
def put_method(employee_id):
    request_data = request.get_json()
    try:
        connection = sqlite3.connect('company.db')
        name = request_data.get('name')
        birth_day = request_data.get('birth_day')
        email = request_data.get('email')
        phone_number = request_data.get('phone_number')
        cursor = connection.cursor()
        query = f'''UPDATE 
                        employee 
                    SET 
                        name='{name}',
                        birth_day='{birth_day}',
                        email='{email}',
                        phone_number='{phone_number}'
                    WHERE
                        rowid={employee_id};'''
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as err:
        print(str(err))
        return jsonify(details=str(err)), 400
    finally:
        connection.close()
    return request_data


@app.route('/api/employee/<employee_id>', methods=['DELETE'])
def delete_method(employee_id):
    request_data = request.get_json()
    try:
        connection = sqlite3.connect('company.db')
        cursor = connection.cursor()
        query = f'''DELETE FROM 
                        employee 
                    WHERE
                        rowid={employee_id};'''
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as err:
        print(str(err))
        return jsonify(details=str(err)), 400
    finally:
        connection.close()
    return jsonify(message=f'user with rowid: {employee_id} not exist')


if __name__ == '__main__':
    app.run(debug=True)
