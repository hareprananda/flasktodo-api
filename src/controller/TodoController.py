from flask import jsonify

class TodoController:
    def store(self):
        return jsonify({'test': 'Ini berhasil boss'}), 200

    def edit(self):
        return jsonify({"manusia": "percobaan"})


