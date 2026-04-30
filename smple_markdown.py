import streamlit as st

# ───────────────────────────────────────────────
# 마크다운 내용
# ───────────────────────────────────────────────
MARKDOWN_CONTENT = """
푸꾸옥은 베트남의 **"진주섬"**으로 불리는 최고의 휴양지입니다! 🌴

---

## 🏝️ 푸꾸옥 (Phú Quốc) 기본 정보

- **위치**: 베트남 최남단, 캄보디아 국경 근처 타이만(Gulf of Thailand)
- **면적**: 약 574km² — 베트남에서 가장 큰 섬
- **행정**: 끼엔장(Kiên Giang)성 소속, **섬 전체가 하나의 시(市)**로 승격 (2021년)
- **인구**: 약 18만 명
- **별명**: 진주섬 (Đảo Ngọc)

---

## 🌤️ 날씨 & 여행 적기| 시기 | 날씨 |
|------|------|
| **11월 ~ 4월** | ☀️ 건기 — 최고 여행 시즌, 맑고 파란 바다 |
| **5월 ~ 10월** | 🌧️ 우기 — 비가 잦지만 여행객 적고 숙박비 저렴 |

> 지금(4~5월)은 건기 막바지로 여행하기 좋은 시기입니다!

---

## 🏖️ 주요 해변

**롱비치 (Bãi Trường)** — 섬 서쪽의 가장 긴 해변(약 20km), 리조트 밀집 지역

**바이사오 (Bãi Sao)** — 새하얀 모래와 에메랄드빛 바다, 푸꾸옥에서 가장 아름다운 해변으로 꼽힘

**옹랑 비치 (Ông Lang)** — 조용하고 한적한 분위기, 배낭여행자에게 인기---

## 🎡 주요 관광지 & 액티비티

**빈원더스 & 빈펄 사파리** — 대규모 테마파크 + 오픈형 동물원. 가족 여행객에게 필수 코스

**푸꾸옥 케이블카** — 세계 최장 해상 케이블카 (약 8km), 안타오 섬까지 연결, 일몰 뷰가 압권

**즈엉동 야시장** — 해산물, 로컬 음식, 기념품이 가득한 활기찬 밤 시장

**빈팔 국립공원** — 섬 북부 원시 정글 트레킹 & 자연 탐방

**스노클링 & 다이빙** — 주변 작은 섬(안터이 군도)에서 산호초 탐험

---

## 🍜 꼭 먹어봐야 할 음식

- **분 꾸아** (Bún quậy) — 푸꾸옥 전통 게살 국수
- **호추** — 세계적으로 유명한 푸꾸옥 후추 (섬에서 직접 재배)
- **느억맘** — 베트남 최고 품질의 액젓 산지 (푸꾸옥산이 최고급)
- **신선 해산물** — 킹크랩, 가리비, 성게 등 저렴하게!

---

## ✈️ 가는 방법 (한국에서)

- **직항**: 인천 → 푸꾸옥 국제공항 (약 5시간, 직항 편 있음)
- **경유**: 하노이·호치민 경유 (더 저렴한 경우 많음)
- **입국**: 한국인은 **45일 무비자** 입국 가능 ✅

---

## 💡 여행 팁

- 이동 수단은 **오토바이 렌트**(하루 약 7~10달러)가 가장 편리
- 숙소는 롱비치 북쪽(조용)과 즈엉동 시내(활기)로 나뉨
- 우기에 가면 숙박비 **30~50% 저렴**, 단 비 대비 필수
- 최근 카지노, 고급 리조트 급증으로 **세계적인 럭셔리 여행지**로 급부상 중

베트남에서 가장 빠르게 개발되고 있는 섬으로, 지금 가는 게 자연이 더 남아있을 때 가는 거라는 말도 있을 정도입니다! 😄

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
