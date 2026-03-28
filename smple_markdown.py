import streamlit as st

# ───────────────────────────────────────────────
# 마크다운 내용
# ───────────────────────────────────────────────
MARKDOWN_CONTENT = """
4월 5일(일요일)은 2026년 서울 벚꽃이 **개화 후 절정(70~80% 이상)**으로 치닫는 시기입니다. 주최자로서 제안하신 **오전 7:30 모임**은 인파를 따돌리고 여유를 확보할 수 있는 신의 한 수와 같은 결정입니다. 

이를 바탕으로 한 벚꽃 시즌 최적화 일정표와 비용표를 정리해 드립니다.

---

### 🌸 [4월 5일] 여의도 벚꽃 나들이 일정표 (오전 7:30 시작)

| 시간 | 일정 | 상세 내용 및 주최자 팁 |
| :--- | :--- | :--- |
| **07:30** | **여의도 집결 및 주차** | **제2주차장** 이용. 이 시간에는 입구 대기 없이 가장 좋은 자리에 주차가 가능합니다. |
| **07:45 ~ 09:00** | **얼리버드 리버뷰 커피** | **스타벅스 여의도한강공원점**. 오전 7시 오픈이므로 창가 명당 자리를 1순위로 차지할 수 있습니다. |
| **09:00 ~ 10:00** | **상쾌한 자전거 라이딩** | 인파가 몰리기 전, 한강 바람을 맞으며 2인용 자전거로 여의도 한 바퀴를 돕니다. |
| **10:00 ~ 11:15** | **벚꽃길 산책 & 사진** | 자전거 반납 후, 만개한 벚꽃 아래에서 부부 동반 '인생샷'을 남기는 시간입니다. |
| **11:15 ~ 11:30** | **식당으로 이동** | 인파가 쏟아져 들어오는 시간대이므로, 반대 방향으로 여유 있게 식당으로 이동합니다. |
| **11:30 ~ 12:45** | **든든한 점심 식사** | **고봉삼계탕**. 오픈 직후 시간이라 예약 시 가장 쾌적하게 식사할 수 있습니다. |
| **13:00 ~ 13:30** | **마지막 '인생라떼'** | **커스텀커피** 등 맛집에서 테이크아웃 후, 정체가 시작되기 전 여의도를 빠져나갑니다. |

---

### 💰 예상 비용표 (부부 2인 기준)

| 항목 | 상세 내용 | 예상 금액 | 비고 |
| :--- | :--- | :---: | :--- |
| **주차비** | 한강공원(약 4시간) | **약 12,000원** | 시즌 할증 및 시간당 요금 적용 |
| **커피(1차)** | 스타벅스 음료 2잔 | **약 13,000원** | 한강 특화 매장 메뉴 기준 |
| **자전거** | 2인용 자전거 (1시간) | **6,600원** | 1시간 대여 기준 |
| **점심 식사** | 상황삼계탕 2그릇 | **40,000원** | 주류 미포함 시 |
| **커피(2차)** | 테이크아웃 2잔 | **약 11,000원** | 라떼류 기준 |
| **총계** | | **약 82,600원** | |

---

### 💡 7:30 모임을 위한 주최자 가이드

1.  **"조기 퇴근"의 매력:** 오후 1~2시에 일정을 마치고 귀가하면, 남들이 주차장에 들어가려고 줄을 서 있을 때 시원하게 여의도를 빠져나오는 쾌감을 느끼실 수 있습니다.
2.  **의상 조언:** 4월 초 오전 7시 반의 한강은 생각보다 쌀쌀할 수 있습니다. 부부들에게 **가벼운 겉옷이나 경량 패딩**을 챙겨오라고 미리 안내하시면 훨씬 센스 있는 주최자가 됩니다.
3.  **자전거 대여소:** 여의나루역 인근 대여소는 오전 9시부터 운영하는 경우가 많으므로, 선착장 근처나 공원 내 일찍 문을 여는 대여소 위치를 미리 체크해두시는 것이 좋습니다. (보통 9시 이전에는 따릉이 이용이 가장 확실합니다.)
4.  **따릉이도 이용가능:** 주차장 인근 인도에는 따릉이 대여소도 있습니다. 

오전 7:30분 모임은 조금 피곤할 수 있지만, **벚꽃 절정기의 여의도를 가장 우아하게 즐길 수 있는 유일한 방법**입니다. 성공적인 모임 되시길 바랍니다!

혹시 부부들에게 보낼 **초대 문구**나 **식당 예약 시 필요한 팁**이 더 필요하신가요?

"""

# ───────────────────────────────────────────────
# 전체화면 스타일 CSS
# ───────────────────────────────────────────────
FULLSCREEN_CSS = """
<style>
/* 전체 배경 */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #f5f5f5;
    color: #1a1a1a;
}

/* 사이드바 및 헤더 숨기기 */
[data-testid="stSidebar"],
[data-testid="stHeader"],
footer {
    display: none !important;
}

/* 메인 컨테이너 전체 너비 */
[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    padding: 0 !important;
}
[data-testid="stMain"] {
    padding: 0 !important;
}

/* 마크다운 래퍼 */
.markdown-wrapper {
    max-width: 860px;
    margin: 0 auto;
    padding: 60px 40px 100px 40px;
    font-family: 'Georgia', serif;
    line-height: 1.9;
    color: #1a1a1a;
    background-color: #ffffff;
    box-shadow: 0 2px 24px rgba(0,0,0,0.08);
    border-radius: 12px;
    margin-top: 40px;
    margin-bottom: 40px;
}

.markdown-wrapper h1 {
    font-size: 2.6rem;
    color: #1e3a5f;
    border-bottom: 2px solid #d0dce8;
    padding-bottom: 12px;
    margin-bottom: 28px;
}

.markdown-wrapper h2 {
    font-size: 1.7rem;
    color: #2563a8;
    margin-top: 48px;
    margin-bottom: 16px;
}

.markdown-wrapper h3 {
    font-size: 1.2rem;
    color: #1e3a5f;
}

.markdown-wrapper hr {
    border: none;
    border-top: 1px solid #e0e7ef;
    margin: 36px 0;
}

.markdown-wrapper blockquote {
    border-left: 4px solid #2563a8;
    background: #f0f5fb;
    padding: 16px 24px;
    border-radius: 0 8px 8px 0;
    color: #2a4a6b;
    font-style: italic;
    margin: 24px 0;
}

.markdown-wrapper code {
    background: #f0f4f8;
    color: #c0392b;
    padding: 2px 7px;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
    font-size: 0.9em;
    border: 1px solid #dce3ea;
}

.markdown-wrapper pre {
    background: #f7f9fb;
    border: 1px solid #dce3ea;
    border-radius: 10px;
    padding: 20px;
    overflow-x: auto;
}

.markdown-wrapper pre code {
    background: none;
    color: #2d3748;
    padding: 0;
    border: none;
}

.markdown-wrapper table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.markdown-wrapper th {
    background: #e8f0f8;
    color: #1e3a5f;
    padding: 12px 16px;
    text-align: left;
    border-bottom: 2px solid #c5d5e8;
}

.markdown-wrapper td {
    padding: 10px 16px;
    border-bottom: 1px solid #e8edf3;
}

.markdown-wrapper tr:hover td {
    background: #f5f8fc;
}

.markdown-wrapper a {
    color: #2563a8;
    text-decoration: underline;
}
</style>
"""

# ───────────────────────────────────────────────
# CSS 주입 및 마크다운 렌더링
# ───────────────────────────────────────────────
st.markdown(FULLSCREEN_CSS, unsafe_allow_html=True)

st.markdown(
    f'<div class="markdown-wrapper">{MARKDOWN_CONTENT}</div>',
    unsafe_allow_html=True
)
