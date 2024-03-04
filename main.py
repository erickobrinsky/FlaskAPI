from flask import Flask, jsonify, request
app= Flask(__name__)

@app.route("/")
def root():
    return "Home"

'''
GET -> obtain information
POST -> create information
PUT -> update information
DELETE -> remove information
'''

@app.route("/users/<user_id>")
def get_users(user_id):
    user = {'id':user_id,'name':"test", "tel":"999-666-000"}
    #/users/2564?query=query_test
    query = request.args.get('query')
    if query:
        user[query] = query
    return jsonify(user), 200




@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    data['status'] = 'user created'
    return jsonify(data),201


if __name__ == "__main__":
    app.run(debug=True)