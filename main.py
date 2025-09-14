"""
■最終目標「メールリライター」
画面を左右2分割
	•	左：元文入力欄（ユーザー）
	•	右：変換結果表示欄
	•	上部にスタイル切替タブ
→ 「フォーマル」「カジュアル」「断り」などをタブで切り替えると、右側の出力が即座に変わる。
	•	差分強調表示（任意機能）
→ 変更された部分を色付きでハイライト表示。
	•	下部に「満足度ボタン」
→ 👍 / 👎 を押してフィードバック、精度向上につなげる。
"""

"""
■main.pyの構成
全体のレイアウトを記述
	•	左右2カラムに分割
	•	左：元文入力欄＋スタイル選択＋変換ボタン
	•	右：変換結果表示＋コピー機能
	•	下部にフィードバックエリアを配置  
"""

import streamlit as st
import constant,components,utils

# ページタイトル
st.title("メールリライター")
st.markdown("誰でも安心して効率よくコミュニケーションできる文面変換支援システム")

# 変換スタイル
selected_style=st.selectbox("変換スタイル",constant.styles)

# 画面２分割
col1,col2=st.columns(2)
with col1:
  user_text=st.text_area("変換したい文章を入力してください。")
  # 変換ボタン
  rewrite_btn=st.button("変換")
with col2:
  # 変換結果表示場所
  result_placeholder=st.empty()

# 「変換」ボタンを押した時の処理
if rewrite_btn and user_text.strip():
  # 文章変換処理
  rewriteen_text=utils.rewrite_email_openai(user_text,selected_style)
  # 変換文書を表示
  st.text(rewriteen_text)

components.feedback()