from flask import jsonify, make_response

def succes( predict, message ):
    res = {
        'predict': predict,
        'message': message
    }

    return make_response(jsonify(res)), 200

def badRequest():
    res = {
        'predict': 'none',
        'message': 'Silahkan Masukan Data Anda Kembali'
    }

    return make_response(jsonify(res)), 400