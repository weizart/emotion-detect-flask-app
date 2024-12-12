import json
import requests
from requests.exceptions import RequestException

def emotion_detector(text_to_analyze):
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
        
    except requests.exceptions.Timeout:
        return "错误：连接超时。请检查网络连接并重试。"
    except requests.exceptions.RequestException as e:
        return f"错误：无法连接到服务。{str(e)}"
    except json.JSONDecodeError:
        return "错误：无法解析服务器响应。"
    except Exception as e:
        return f"错误：处理过程中出现问题。{str(e)}"
