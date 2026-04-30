import streamlit as st

# ───────────────────────────────────────────────
# 타이틀 HTML (재미있고 화려한 디자인)
# ───────────────────────────────────────────────
TITLE_HTML = """
<div class="title-wrapper">
  <div class="title-bg-decor"></div>

  <div class="title-tag">✈️ 2026 육공회 특별 여행</div>

  <h1 class="title-main">
    <span class="wave">🌊</span>
    <span class="title-text">푸꾸옥으로</span>
    <span class="title-highlight"> 떠나자!</span>
    <span class="wave">🌊</span>
  </h1>

  <div class="title-sub">
    베트남의 <strong>진주섬</strong>에서 만나는 우리들의 특별한 추억
  </div>

  <div class="members-row">
    <span class="member-badge">🧡 금산</span>
    <span class="member-badge">💛 흥준</span>
    <span class="member-badge">💚 응석</span>
    <span class="member-badge">💙 광민</span>
    <span class="member-badge">💜 선원</span>
    <span class="member-badge">❤️ 상휘</span>
  </div>

  <div class="palm-row">🌴 &nbsp; 🐠 &nbsp; 🦀 &nbsp; 🍹 &nbsp; 🐚 &nbsp; 🌅 &nbsp; 🏄 &nbsp; 🐟 &nbsp; 🌴</div>
</div>
"""

# ───────────────────────────────────────────────
# 지도 HTML (OpenStreetMap iframe)
# ───────────────────────────────────────────────
MAP_HTML = """
<div class="map-section">
  <div class="map-label">
    📍 <strong>푸꾸옥 위치</strong> — 베트남 최남단 타이만의 진주
  </div>
  <div class="map-container">
    <iframe
      src="https://www.openstreetmap.org/export/embed.html?bbox=103.8&amp;lat=10.22&amp;lon=103.98&amp;zoom=10&amp;marker=10.22,103.98&amp;layers=M"
      style="width:100%; height:420px; border:none; border-radius:14px;"
      allowfullscreen>
    </iframe>
  </div>
  <div class="map-caption">
    🗺️ 호치민시에서 서쪽으로 약 260km · 캄보디아 국경 근처 · 면적 574km²
  </div>
</div>
"""

# ───────────────────────────────────────────────
# 본문 마크다운 (타이틀·지도 제외)
# ───────────────────────────────────────────────
BODY_MARKDOWN = """
---

## 🏝️ 푸꾸옥 (Phú Quốc) 기본 정보

- **위치**: 베트남 최남단, 캄보디아 국경 근처 타이만(Gulf of Thailand)
- **면적**: 약 574km² — 베트남에서 가장 큰 섬
- **행정**: 끼엔장(Kiên Giang)성 소속, **섬 전체가 하나의 시(市)**로 승격 (2021년)
- **인구**: 약 18만 명
- **별명**: 진주섬 (Đảo Ngọc)

---

## 🌤️ 날씨 & 여행 적기

| 시기 | 날씨 |
|------|------|
| **11월 ~ 4월** | ☀️ 건기 — 최고 여행 시즌, 맑고 파란 바다 |
| **5월 ~ 10월** | 🌧️ 우기 — 비가 잦지만 여행객 적고 숙박비 저렴 |

> 지금(4~5월)은 건기 막바지로 여행하기 좋은 시기입니다!

---

## 🏖️ 주요 해변

**롱비치 (Bãi Trường)** — 섬 서쪽의 가장 긴 해변(약 20km), 리조트 밀집 지역

**바이사오 (Bãi Sao)** — 새하얀 모래와 에메랄드빛 바다, 푸꾸옥에서 가장 아름다운 해변으로 꼽힘

**옹랑 비치 (Ông Lang)** — 조용하고 한적한 분위기, 배낭여행자에게 인기

---

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
# 푸터 HTML
# ───────────────────────────────────────────────
FOOTER_HTML = """
<div class="fun-footer">
  <div class="footer-wave">〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰</div>
  <div class="footer-text">
    🌺 육공회의 행복한 여행을 응원합니다! 🌺<br>
    <span style="font-size:0.85rem; opacity:0.7;">좋은 추억 가득한 푸꾸옥 여행 되세요 🌊✨</span>
  </div>
  <div class="footer-emojis">🌴 🐠 🍹 🌅 🐚 🦀 🏄 🌊 🌴</div>
</div>
"""

# ───────────────────────────────────────────────
# 전체 CSS
# ───────────────────────────────────────────────
FULLSCREEN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Pacifico&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e0f7fa 0%, #e8f5e9 50%, #fff9c4 100%);
    color: #1a1a1a;
}

[data-testid="stSidebar"],
[data-testid="stHeader"],
footer { display: none !important; }

[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    padding: 0 !important;
}
[data-testid="stMain"] { padding: 0 !important; }

/* ── 전체 래퍼 ── */
.markdown-wrapper {
    max-width: 880px;
    margin: 30px auto 60px auto;
    padding: 0 40px 60px 40px;
    font-family: 'Noto Sans KR', sans-serif;
    line-height: 1.9;
    color: #1a1a1a;
    background: rgba(255,255,255,0.92);
    box-shadow: 0 8px 48px rgba(0,150,136,0.12);
    border-radius: 24px;
    overflow: hidden;
}

/* ── 타이틀 섹션 ── */
.title-wrapper {
    position: relative;
    background: linear-gradient(135deg, #00897b 0%, #00acc1 50%, #43a047 100%);
    padding: 50px 40px 40px 40px;
    text-align: center;
    overflow: hidden;
    margin: 0 -40px 40px -40px;
}

.title-bg-decor {
    position: absolute;
    top: -60px; right: -60px;
    width: 240px; height: 240px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}

.title-tag {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    color: #fff;
    font-size: 0.9rem;
    font-weight: 700;
    padding: 6px 18px;
    border-radius: 20px;
    margin-bottom: 18px;
    letter-spacing: 1px;
    border: 1px solid rgba(255,255,255,0.3);
}

.title-main {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 3.2rem;
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 12px 0;
    text-shadow: 0 4px 24px rgba(0,0,0,0.2);
    line-height: 1.2;
}

.title-highlight {
    color: #fff9c4;
    font-style: italic;
}

.wave {
    display: inline-block;
    animation: sway 2s ease-in-out infinite;
}
.wave:last-child { animation-delay: 0.5s; }

@keyframes sway {
    0%, 100% { transform: rotate(-10deg) scale(1); }
    50%       { transform: rotate(10deg)  scale(1.1); }
}

.title-sub {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.92);
    margin-bottom: 24px;
}

.members-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 24px;
}

.member-badge {
    background: rgba(255,255,255,0.22);
    color: #ffffff;
    font-size: 1rem;
    font-weight: 700;
    padding: 7px 18px;
    border-radius: 50px;
    border: 1.5px solid rgba(255,255,255,0.5);
    transition: all 0.2s;
    cursor: default;
}
.member-badge:hover {
    background: rgba(255,255,255,0.38);
    transform: translateY(-3px) scale(1.08);
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
}

.palm-row {
    font-size: 1.6rem;
    letter-spacing: 4px;
    opacity: 0.85;
}

/* ── 지도 섹션 ── */
.map-section {
    margin: 36px 0;
}

.map-label {
    font-size: 1.05rem;
    font-weight: 700;
    color: #00695c;
    margin-bottom: 12px;
    padding-left: 4px;
}

.map-container {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(0,0,0,0.12);
    border: 2px solid #b2dfdb;
}

.map-caption {
    margin-top: 10px;
    font-size: 0.88rem;
    color: #546e7a;
    text-align: center;
    font-style: italic;
}

/* ── 본문 스타일 ── */
.markdown-wrapper h2 {
    font-size: 1.6rem;
    color: #00695c;
    margin-top: 44px;
    margin-bottom: 14px;
    border-left: 5px solid #26c6da;
    padding-left: 14px;
}

.markdown-wrapper hr {
    border: none;
    border-top: 2px dashed #b2dfdb;
    margin: 32px 0;
}

.markdown-wrapper blockquote {
    border-left: 4px solid #26c6da;
    background: #e0f7fa;
    padding: 14px 22px;
    border-radius: 0 10px 10px 0;
    color: #006064;
    font-style: italic;
    margin: 20px 0;
}

.markdown-wrapper table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}

.markdown-wrapper th {
    background: #00897b;
    color: #fff;
    padding: 12px 16px;
    text-align: left;
}

.markdown-wrapper td {
    padding: 10px 16px;
    border-bottom: 1px solid #e0f2f1;
}

.markdown-wrapper tr:hover td {
    background: #e0f7fa;
}

/* ── 푸터 ── */
.fun-footer {
    text-align: center;
    padding: 36px 20px 10px 20px;
    margin: 40px -40px -60px -40px;
    background: linear-gradient(135deg, #00897b, #26c6da);
    color: #fff;
}

.footer-wave {
    font-size: 1.2rem;
    opacity: 0.5;
    margin-bottom: 12px;
    letter-spacing: 2px;
}

.footer-text {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 12px;
    line-height: 1.8;
}

.footer-emojis {
    font-size: 1.5rem;
    letter-spacing: 6px;
    margin-bottom: 20px;
}
</style>
"""

# ───────────────────────────────────────────────
# 렌더링
# ───────────────────────────────────────────────
st.markdown(FULLSCREEN_CSS, unsafe_allow_html=True)

st.markdown('<div class="markdown-wrapper">', unsafe_allow_html=True)

# 1) 재미있는 타이틀
st.markdown(TITLE_HTML, unsafe_allow_html=True)

# 2) 기본 정보 & 지도
st.markdown("""
## 🏝️ 푸꾸옥 (Phú Quốc) 기본 정보

- **위치**: 베트남 최남단, 캄보디아 국경 근처 타이만(Gulf of Thailand)
- **면적**: 약 574km² — 베트남에서 가장 큰 섬
- **행정**: 끼엔장(Kiên Giang)성 소속, **섬 전체가 하나의 시(市)**로 승격 (2021년)
- **인구**: 약 18만 명
- **별명**: 진주섬 (Đảo Ngọc)
""")

# 지도 삽입
st.markdown(MAP_HTML, unsafe_allow_html=True)

# 3) 나머지 본문
st.markdown(BODY_MARKDOWN)

# 4) 푸터
st.markdown(FOOTER_HTML, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
