import json
import requests

def emotion_detector(text_to_analyze):
    # 检查空白输入
    if not text_to_analyze or text_to_analyze.isspace():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 解析JSON响应
        response_dict = json.loads(response.text)
        
        # 提取情感分数
        emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        # 构建结果字典
        result = {
            'anger': emotions.get('anger', 0.0),
            'disgust': emotions.get('disgust', 0.0),
            'fear': emotions.get('fear', 0.0),
            'joy': emotions.get('joy', 0.0),
            'sadness': emotions.get('sadness', 0.0)
        }
        
        # 找出主导情感
        dominant_emotion = max(result.items(), key=lambda x: x[1])[0]
        result['dominant_emotion'] = dominant_emotion
        
        return result
        
    except requests.exceptions.RequestException as e:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
