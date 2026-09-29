from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = "/api/docs"
API_URL = "/static/masterblog.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Masterblog API"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Return all blog posts, optionally sorted by title or content."""
    sort_field = request.args.get('sort')
    direction = request.args.get('direction', 'asc')

    if sort_field and sort_field not in ('title', 'content'):
        return jsonify({"error": "Invalid sort field."}), 400

    if direction not in ('asc', 'desc'):
        return jsonify({"error": "Invalid sort direction."}), 400

    posts = POSTS.copy()

    if sort_field:
        posts.sort(
            key=lambda post: post[sort_field].lower(),
            reverse=direction == 'desc'
        )

    return jsonify(posts)


@app.route('/api/posts', methods=['POST'])
def add_post():
    """Create a new blog post."""
    data = request.get_json()

    missing_fields = []

    if not data or not data.get('title', '').strip():
        missing_fields.append('title')

    if not data or not data.get('content', '').strip():
        missing_fields.append('content')

    if missing_fields:
        return jsonify({
            "error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    new_id = max(post["id"] for post in POSTS) + 1

    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"]
    }

    POSTS.append(new_post)

    return jsonify(new_post), 201


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    """Search posts by title and/or content."""
    title_query = request.args.get('title', '').lower()
    content_query = request.args.get('content', '').lower()

    results = [
        post for post in POSTS
        if (not title_query or title_query in post["title"].lower())
        and (not content_query or content_query in post["content"].lower())
    ]

    return jsonify(results), 200


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Delete a blog post by ID."""
    post = next((post for post in POSTS if post["id"] == post_id), None)

    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    POSTS.remove(post)

    return jsonify({
        "message": f"Post with id {post_id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Update the title and/or content of a blog post by ID."""
    post = next((post for post in POSTS if post["id"] == post_id), None)

    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    data = request.get_json() or {}

    if 'title' in data:
        if not isinstance(data['title'], str) or not data['title'].strip():
            return jsonify({"error": "Title cannot be empty."}), 400
        post["title"] = data["title"]

    if 'content' in data:
        if not isinstance(data['content'], str) or not data['content'].strip():
            return jsonify({"error": "Content cannot be empty."}), 400
        post["content"] = data["content"]

    return jsonify(post), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
