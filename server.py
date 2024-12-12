from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    # 检查空白输入
    if not text_to_analyze or text_to_analyze.isspace():
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "response": "无效文本！请再试一次！"
        }), 400
    
    result = emotion_detector(text_to_analyze)
    
    if isinstance(result, dict):
        if result["dominant_emotion"] is None:
            return jsonify({
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
                "response": "无效文本！请再试一次！"
            }), 400
        
        # 构建响应文本
        response_text = (
            f"对于给定的语句，系统响应为 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} 和 'sadness': {result['sadness']}。"
            f"主导情感为 {result['dominant_emotion']}。"
        )
        
        return jsonify({
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion'],
            "response": response_text
        })
    else:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "response": "无效文本！请再试一次！"
        }), 400

if __name__ == "__main__":
    app.run(host="localhost", port=5000) 