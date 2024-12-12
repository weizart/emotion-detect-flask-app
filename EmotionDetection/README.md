# EmotionDetection

这个Python包提供了使用Watson NLP服务进行文本情感分析的功能。

## 安装

```bash
pip install EmotionDetection
```

## 使用方法

```python
from EmotionDetection import emotion_detector

# 分析文本情感
result = emotion_detector("我喜欢这项新技术")
print(result)
```

## 返回结果

函数返回一个包含以下情感得分的字典：
- anger (愤怒)
- disgust (厌恶)
- fear (恐惧)
- joy (喜悦)
- sadness (悲伤)
- dominant_emotion (主导情感)

## 依赖

- Python >= 3.6
- requests >= 2.31.0 