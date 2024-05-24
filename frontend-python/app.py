from flask import Flask, render_template, request, redirect, url_for
import redis
import random

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

videos = [
    {"id": 1, "BMW": "Video 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "TOYOTA": "Video 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "NISSAN": "Video 3", "tags": ["tag1", "tag3"]},
    {"id": 4, "FORD": "Video 4", "tags": ["tag1", "tag2", "tag3"]},
    {"id": 5, "HONDA": "Video 5", "tags": ["tag1"]},
    {"id": 6, "CHEVROLET": "Video 6", "tags": ["tag2"]},
    {"id": 7, "VOLKSWAGEN": "Video 7", "tags": ["tag3"]},
    {"id": 8, "HYUNDAI": "Video 8", "tags": ["tag1", "tag2"]},
    # Agrega más metadatos de video aquí
]

@app.route('/')
def index():
    user_id = request.args.get('user_id', 'default_user')
    watched_videos = r.lrange(f'user:{user_id}:watched', 0, -1)
    
    if len(watched_videos) < 2:
        recommended_videos = random.sample(videos, 2)
    else:
        recommended_videos = get_personalized_recommendations(user_id)
    
    return render_template('index.html', videos=recommended_videos)

@app.route('/watch', methods=['POST'])
def watch():
    user_id = request.form['user_id']
    video_id = request.form['video_id']
    r.rpush(f'user:{user_id}:watched', video_id)
    r.publish('video_watched', f'{user_id},{video_id}')
    return redirect(url_for('index', user_id=user_id))

def get_personalized_recommendations(user_id):
# Lógica para obtener recomendaciones personalizadas
    # Por ahora, solo devuelve videos aleatorios

    return random.sample(videos, 2)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
