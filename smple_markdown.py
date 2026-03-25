import streamlit as st

# 1. 페이지 설정을 'wide'로 해서 화면을 넓게 사용합니다.
st.set_page_config(layout="wide")

def main():
    # 2. 읽어올 마크다운 파일 경로 (본인의 파일명으로 수정하세요)
    file_path = "markdown_doc.md"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()
        
        # 3. 마크다운 출력
        st.markdown(markdown_content)
        
    except FileNotFoundError:
        st.error(f"파일을 찾을 수 없습니다: {file_path}")

if __name__ == "__main__":
    main()
