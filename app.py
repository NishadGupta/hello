from flask import Flask, render_template_string
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.getenv('IMDB_API_KEY', 'k_1234567890')
    url = f"https://imdb-api.com/en/API/MostPopularTVs/{api_key}"
    shows = []
    try:
        r = requests.get(url, timeout=5)
        if r.ok:
            data = r.json()
            for item in data.get('items', []):
                if 'Animation' in item.get('genres', ''):
                    shows.append(item.get('title'))
    except Exception:
        pass

    html = '<h1>Latest Anime Shows</h1>'
    if shows:
        html += '<ul>' + ''.join(f'<li>{s}</li>' for s in shows[:10]) + '</ul>'
    else:
        html += '<p>Unable to fetch data from IMDb.</p>'
    html += '<p><a href="/stopwatch">Stopwatch</a></p>'
    return render_template_string(html)

@app.route('/stopwatch')
def stopwatch():
    html = """
    <!doctype html>
    <title>Stopwatch</title>
    <h1>Stopwatch</h1>
    <div id='display'>00:00:00</div>
    <button onclick='start()'>Start</button>
    <button onclick='stop()'>Stop</button>
    <button onclick='reset()'>Reset</button>
    <script>
    let startTime, elapsed=0, timer;
    function format(ms){
        const total = Math.floor(ms/1000);
        const hrs = String(Math.floor(total/3600)).padStart(2,'0');
        const mins = String(Math.floor((total%3600)/60)).padStart(2,'0');
        const secs = String(total%60).padStart(2,'0');
        return `${hrs}:${mins}:${secs}`;
    }
    function update(){
        document.getElementById('display').textContent = format(elapsed + Date.now()-startTime);
    }
    function start(){
        if(!timer){
            startTime = Date.now();
            timer = setInterval(update,1000);
        }
    }
    function stop(){
        if(timer){
            clearInterval(timer);
            elapsed += Date.now()-startTime;
            timer = null;
        }
    }
    function reset(){
        stop();
        elapsed = 0;
        document.getElementById('display').textContent='00:00:00';
    }
    </script>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
