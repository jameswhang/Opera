from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/health')
def health():
    return 'Hello from Opera!'

@app.route('/count_push/<username>', methods=['GET'])
def count_user_push(username):
    """
    Given a username, count the public push count of that user
    :param str username
    :returns int
    """
    public_activities = json.loads(query_user_activities(username))
    push_count = 0
    for activity in public_activities:
        if activity['type'] == 'PushEvent':
            push_count += 1
    return 'Total push count: ' + str(push_count)

@app.route('/query_user/<username>', methods=['GET'])
def query_user_activities(username):
    """
    Given a username, query the GitHub API and retrieve the user's public activities
    :param str username
    :returns list
    """
    github_endpoint = 'https://api.github.com/users/{}/events/public'.format(username)
    return requests.get(url=github_endpoint).text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
