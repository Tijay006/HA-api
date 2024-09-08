from flask import Flask, jsonify, request  # 'request' hier importieren

app = Flask(__name__)

# Vordefinierte Variablen (Hardcoded)
variables = {
    'var1': 10,
    'var2': 'Hello',
    'var3': [1, 2, 3]
}

# Route zum Abrufen aller Variablen oder einer bestimmten Variable
@app.route('/get_variables', methods=['GET'])
def get_variables():
    # Überprüfen, ob eine bestimmte Variable abgefragt wird
    var_name = request.args.get('name')
    if var_name:
        if var_name in variables:
            return jsonify({var_name: variables[var_name]}), 200
        else:
            return jsonify({'error': f'Variable {var_name} nicht gefunden!'}), 404
    return jsonify(variables), 200  # Alle Variablen zurückgeben

if __name__ == '__main__':
    app.run(debug=True)
