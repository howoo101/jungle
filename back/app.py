from bson import ObjectId
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbjungle


# 전체 조회 list /memo
# 카드 생성  create /memo post
# 카드 수정 update /memo post
# 카드 삭제 delete /memo post
# 좋아요 /memo post

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def listing():
    # memos = list(db.memos.find({}, {'_id': False}).sort('like', -1))
    memos = list(db.memos.find().sort('like', -1))

    for memo in memos:
        id = str(memo['_id'])
        memo['_id'] = id

    return jsonify({'result': 'success', "memos": memos})


@app.route('/api/create', methods=['POST'])
def create():
    title = request.form['title']
    content = request.form['content']
    likeCnt = 0
    memo = {
        "title": title,
        "content": content,
        "like": likeCnt
    }
    db.memos.insert_one(memo)
    return jsonify({'result': 'success'})


@app.route('/api/update', methods=['POST'])
def update():
    id_value = request.form['id']

    new_title = request.form['title']
    new_content = request.form['content']

    db.memos.update_one({'_id': ObjectId(id_value)}, {'$set': {'title': new_title, 'content': new_content}})
    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def delete():
    id_value = request.form['id']
    db.memos.delete_one({'_id': ObjectId(id_value)})
    return jsonify({'result': 'success'})


@app.route('/api/like', methods=['POST'])
def like():
    id_value = request.form['id']
    memo = db.memos.find_one({'_id': ObjectId(id_value)})

    new_like = memo['like'] + 1
    db.memos.update_one({'_id': ObjectId(id_value)}, {'$set': {'like': new_like} })
    print(memo['like'])
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=55500, debug=True)
