from flask import Flask, request
import json
from readings.temperature_reading_manager import TemperatureReadingManager
from readings.pressure_reading_manager import PressureReadingManager
from readings.temperature_reading import TemperatureReading
from readings.pressure_reading import PressureReading
import datetime

app = Flask(__name__)

####ADD READING####
@app.route('/sensor/<sensor_type>/reading', methods=['POST'])
def add_sensor_reading(sensor_type):
    """App method to add sensor reading and assigning it a unique sequence number"""
    data = request.json

    try:

        if sensor_type == 'temperature':
            temperature_reading_manager = TemperatureReadingManager()
            temperature_reading_manager.add_log_message(model=data["model"],
                                                        min_reading=data["min_reading"],
                                                        avg_reading=data["avg_reading"],
                                                        max_reading=data["max_reading"],
                                                        status=data["status"])

        elif sensor_type == 'pressure':
            pressure_reading_manager = PressureReadingManager()
            pressure_reading_manager.add_log_message(model=data["model"],
                                                        min_reading=data["min_reading"],
                                                        avg_reading=data["avg_reading"],
                                                        max_reading=data["max_reading"],
                                                        status=data["status"])

        else:
            return app.response_class(
                status=400
            )

        response = app.response_class(
            status=200,
        )

        return response

    except:
        return app.response_class(
            status=400
        )

####UPDATE READING####
@app.route('/sensor/<sensor_type>/reading/<int:seq_num>', methods=['PUT'])
def update_sensor_reading(sensor_type, seq_num):
    """ App method to update reading object in list if there is a matching sequence num """
    data = request.json

    if sensor_type == 'temperature':
        sensor_manager = TemperatureReadingManager()

    elif sensor_type == 'pressure':
        sensor_manager = PressureReadingManager()

    else:
        return app.response_class(
            status=400,
        )

    sensor_manager.update_log_message(seq_num,
                                        data['model'],
                                        data['min_reading'],
                                        data['avg_reading'],
                                        data['max_reading'],
                                        data['status'])

    return app.response_class(
        status=200
    )

####DELETE READING####
@app.route('/sensor/<sensor_type>/reading/<int:seq_num>', methods=['DELETE'])
def delete_sensor_reading(sensor_type, seq_num):
   """" App method to delete a sensor reading by sequence number """

   if sensor_type == 'temperature':
       sensor_manager = TemperatureReadingManager()

   elif sensor_type == 'pressure':
       sensor_manager = PressureReadingManager()

   else:
       return app.response_class(
           status=400
       )

   delete_response = sensor_manager.delete_log_message(seq_num)
   if delete_response is True:
       response = app.response_class(
           status=200
       )

       return response

   else:
       return app.response_class(
           status=400
       )

####GET READING####
@app.route('/sensor/<sensor_type>/reading/<int:seq_num>', methods=['GET'])
def get_sensor_reading(sensor_type, seq_num):
    """App method to get a sensor reading by sequence number"""
    if sensor_type == 'temperature':
        sensor_manager = TemperatureReadingManager()

    elif sensor_type == 'pressure':
        sensor_manager = PressureReadingManager()

    else:
        return app.response_class(
            status=400
        )

    get_reading = sensor_manager.get_log_message(seq_num)

    if get_reading is not False:
        response = app.response_class(
            response=get_reading.to_json(),
            status=200,
            mimetype='application/json'
        )

        return response

    else:
        return app.response_class(
            status=400
        )


####GET ALL READINGS####
@app.route('/sensor/<sensor_type>/reading/all', methods=['GET'])
def get_all_sensor_readings(sensor_type):
    """App method to get all sensor readings """

    if sensor_type == 'temperature':
        sensor_manager = TemperatureReadingManager()

    elif sensor_type == 'pressure':
        sensor_manager = PressureReadingManager()

    else:
        return app.response_class(
            status=400
        )

    all_readings = sensor_manager.get_log_messages()

    json_list = []
    for reading in all_readings:
        json_list.append(reading.to_dict())

    response = app.response_class(
        response=json.dumps(json_list, indent=4),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.run()