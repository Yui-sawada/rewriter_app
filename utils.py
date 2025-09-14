"""
■utils.pyの構成
LLMとのやりとりや処理を担当。
llm_client
	•	OpenAI APIや他のLLMとの接続部分
	•	入力テキスト＋スタイル指定を投げて、変換結果を返す
	•	（将来的にキャッシュ・リトライ処理もここに入れる）
text_diff
	•	元文と変換後文を比較し、差分をハイライト用に加工する関数
feedback_handler
	•	👍👎やコメントを保存するロジック
	•	保存先はDBやログファイルを想定
validators
	•	入力チェック（空文字、文字数制限など）
"""

import openai
import constant

# メール文書変換
def rewrite_email_openai(text: str, style: str) -> str:
    prompt = f"次の文章を「{style}」スタイルで自然に書き換えてください：\n{text}"
    
    response = openai.ChatCompletion.create(
        model=constant.MODEL,
        messages=[
            {"role": "system", "content": "あなたは丁寧な文章変換アシスタントです。"},
            {"role": "user", "content": prompt}
        ],
        temperature=constant.TEMPERATURE
    )
    rewritten_text = response.choices[0].message.content()
    return rewritten_text