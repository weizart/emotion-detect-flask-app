"""
这个模块实现了一个情感检测的Web服务器。
它使用Flask框架提供REST API，并集成了Watson情感分析服务。
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# 创建Flask应用实例
app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """渲染主页"""
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    处理情感检测请求的路由函数
    
    Returns:
        tuple: 包含JSON响应和HTTP状态码
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    # 检查空白输入
    if not text_to_analyze or text_to_analyze.isspace():
        return create_error_response()
    
    result = emotion_detector(text_to_analyze)
    
    if not isinstance(result, dict) or result.get("dominant_emotion") is None:
        return create_error_response()
    
    # 构建响应文本
    response_text = create_response_text(result)
    
    return jsonify({
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion'],
        "response": response_text
    })

def create_error_response():
    """
    创建错误响应
    
    Returns:
        tuple: 包含错误信息的JSON响应和400状态码
    """
    return jsonify({
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
        "response": "无效文本！请再试一次！"
    }), 400

def create_response_text(result):
    """
    根据情感分析结果创建响应文本
    
    Args:
        result (dict): 情感分析结果
        
    Returns:
        str: 格式化的响应文本
    """
    return (
        f"对于给定的语句，系统响应为 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} 和 'sadness': {result['sadness']}。"
        f"主导情感为 {result['dominant_emotion']}。"
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5000) 