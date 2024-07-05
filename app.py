from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client['usersdb']
users_collection = db['users']


# Utility function to format user documents
def user_to_dict(user):
    return {
        'id': str(user['_id']),
        'name': user['name'],
        'email': user['email'],
        'password': user['password']
    }

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        '_id': ObjectId(data['id']) if 'id' in data else ObjectId(),
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    try:
        users_collection.insert_one(new_user)
        new_user['id'] = str(new_user['_id'])
        return jsonify(user_to_dict(new_user)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = users_collection.find()
    return jsonify([user_to_dict(user) for user in users])

# Get a single user
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify(user_to_dict(user))
    else:
        return jsonify({'error': 'User not found'}), 404

# Update a user 
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    updated_user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_user})
    if result.matched_count > 0:
        return jsonify(user_to_dict(users_collection.find_one({'_id': ObjectId(id)})))
    else:
        return jsonify({'error': 'User not found'}), 404

# Delete a user 
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted'})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
