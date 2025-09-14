"""
■components.pyの構成
input_area
  元文入力欄のコンポーネント
style_selector
  ドロップダウン
output_area
  変換結果の表示欄（追加機能：差分ハイライト）
feedback
  👍👎ボタンとコメント欄
"""

import streamlit as st

def feedback():
  st.divider()
  st.write("この変換結果は満足ですか？")
  col1,col2=st.columns(2)
  with col1:
    if st.button("👍"):
      st.success("👍フィードバックありがとうございます！")
      # test フィードバック結果を履歴に追加
  with col2:
    if st.button("👎"):
      st.warning("👎フィードバックありがとうございます。")