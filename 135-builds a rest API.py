# REST API using Flask
from flask import Flask, jsonify, request
app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1", "price": 10.99},
    {"id": 2, "name": "Item 2", "price": 19.99},
    {"id": 3, "name": "Item 3", "price": 5.99}
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    items.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item
            return jsonify(updated_item)
    return jsonify({"error": "Item not found"}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
    