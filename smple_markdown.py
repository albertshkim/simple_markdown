import streamlit as st
from pathlib import Path

# ───────────────────────────────────────────────
# 페이지 설정
# ───────────────────────────────────────────────
st.set_page_config(page_title="🌴 육공회 푸꾸옥 여행", layout="wide")

# ───────────────────────────────────────────────
# 이미지 경로 (같은 폴더)
# ───────────────────────────────────────────────
MAP_IMAGE   = Path(__file__).parent / "puku.png"
FRIEND_IMAGE = Path(__file__).parent / "fri.png"

# ───────────────────────────────────────────────
# CSS
# ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e0f7fa 0%, #e8f5e9 50%, #fff9c4 100%);
    color: #1a1a1a;
}
[data-testid="stSidebar"], [data-testid="stHeader"], footer { display: none !important; }
[data-testid="stMainBlockContainer"] { max-width: 100% !important; padding: 0 !important; }
[data-testid="stMain"] { padding: 0 !important; }

.wrapper {
    max-width: 900px;
    margin: 30px auto 60px auto;
    padding: 0 40px 60px 40px;
    font-family: 'Noto Sans KR', sans-serif;
    line-height: 1.9;
    color: #1a1a1a;
    background: rgba(255,255,255,0.93);
    box-shadow: 0 8px 48px rgba(0,150,136,0.13);
    border-radius: 24px;
    overflow: hidden;
}

/* ── 타이틀 배너 ── */
.title-banner {
    position: relative;
    background: linear-gradient(135deg, #00897b 0%, #00acc1 55%, #43a047 100%);
    padding: 52px 40px 42px 40px;
    text-align: center;
    margin: 0 -40px 40px -40px;
    overflow: hidden;
}
.title-banner::before {
    content: "";
    position: absolute; top: -70px; right: -70px;
    width: 260px; height: 260px;
    background: rgba(255,255,255,0.07); border-radius: 50%;
}
.title-banner::after {
    content: "";
    position: absolute; bottom: -50px; left: -50px;
    width: 180px; height: 180px;
    background: rgba(255,255,255,0.05); border-radius: 50%;
}
.title-chip {
    display: inline-block;
    background: rgba(255,255,255,0.22);
    color: #fff; font-size: 0.88rem; font-weight: 700;
    padding: 5px 18px; border-radius: 20px; margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.35); letter-spacing: 1px;
}
.title-main {
    font-size: 3rem; font-weight: 900; color: #fff;
    margin: 0 0 10px 0;
    text-shadow: 0 4px 20px rgba(0,0,0,0.2); line-height: 1.25;
}
.title-highlight { color: #fff9c4; font-style: italic; }
.wave { display: inline-block; animation: sway 2s ease-in-out infinite; }
.wave:last-child { animation-delay: 0.6s; }
@keyframes sway {
    0%,100% { transform: rotate(-10deg) scale(1.0); }
    50%      { transform: rotate(10deg)  scale(1.12); }
}
.title-sub { font-size: 1.08rem; color: rgba(255,255,255,0.9); margin-bottom: 26px; }
.members-row {
    display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-bottom: 26px;
}
.mbadge {
    background: rgba(255,255,255,0.22); color: #fff;
    font-size: 0.98rem; font-weight: 700;
    padding: 7px 20px; border-radius: 50px;
    border: 1.5px solid rgba(255,255,255,0.45);
    transition: all .2s; cursor: default;
}
.mbadge:hover {
    background: rgba(255,255,255,0.38);
    transform: translateY(-3px) scale(1.07);
    box-shadow: 0 4px 14px rgba(0,0,0,0.14);
}
.emoji-row { font-size: 1.55rem; letter-spacing: 5px; opacity: 0.88; }

/* ── 섹션 공통 ── */
.section-label {
    font-size: 1.05rem; font-weight: 700; color: #00695c;
    margin: 4px 0 10px 0; padding-left: 4px;
}
.img-frame {
    border-radius: 16px; overflow: hidden;
    border: 2px solid #b2dfdb;
    box-shadow: 0 4px 24px rgba(0,0,0,0.10);
}
.caption {
    text-align: center; font-size: 0.87rem; color: #546e7a;
    font-style: italic; margin-top: 8px; margin-bottom: 20px;
}

/* ── 본문 ── */
.wrapper h2 {
    font-size: 1.55rem; color: #00695c;
    margin-top: 44px; margin-bottom: 14px;
    border-left: 5px solid #26c6da; padding-left: 14px;
}
.wrapper hr { border: none; border-top: 2px dashed #b2dfdb; margin: 30px 0; }
.wrapper blockquote {
    border-left: 4px solid #26c6da; background: #e0f7fa;
    padding: 14px 22px; border-radius: 0 10px 10px 0;
    color: #006064; font-style: italic; margin: 20px 0;
}
.wrapper table {
    width: 100%; border-collapse: collapse; margin: 20px 0;
    border-radius: 10px; overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}
.wrapper th { background: #00897b; color: #fff; padding: 12px 16px; text-align: left; }
.wrapper td { padding: 10px 16px; border-bottom: 1px solid #e0f2f1; }
.wrapper tr:hover td { background: #e0f7fa; }

/* ── 푸터 ── */
.footer {
    text-align: center; padding: 36px 20px 22px 20px;
    margin: 44px -40px -60px -40px;
    background: linear-gradient(135deg, #00897b, #26c6da); color: #fff;
}
.footer-wave { font-size: 1.15rem; opacity: 0.45; margin-bottom: 12px; letter-spacing: 2px; }
.footer-text { font-size: 1.1rem; font-weight: 700; margin-bottom: 12px; line-height: 1.8; }
.footer-emojis { font-size: 1.45rem; letter-spacing: 6px; margin-bottom: 18px; }
</style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# 레이아웃 시작
# ───────────────────────────────────────────────
st.markdown('<div class="wrapper">', unsafe_allow_html=True)

# ① 타이틀 배너
st.markdown("""
<div class="title-banner">
  <div class="title-chip">✈️ 2026 육공회 특별 여행</div>
  <h1 class="title-main">
    <span class="wave">🌊</span>
    푸꾸옥으로
    <span class="title-highlight"> 떠나자!</span>
    <span class="wave">🌊</span>
  </h1>
  <div class="title-sub">베트남의 <strong>진주섬</strong>에서 만나는 우리들의 특별한 추억</div>
  <div class="members-row">
    <span class="mbadge">🧡 금산</span>
    <span class="mbadge">💛 흥준</span>
    <span class="mbadge">💚 응석</span>
    <span class="mbadge">💙 광민</span>
    <span class="mbadge">💜 선원</span>
    <span class="mbadge">❤️ 상휘</span>
  </div>
  <div class="emoji-row">🌴 🐠 🦀 🍹 🐚 🌅 🏄 🐟 🌴</div>
</div>
""", unsafe_allow_html=True)

# ② 친구들 사진
if FRIEND_IMAGE.exists():
    st.markdown('<div class="section-label">📸 우리들의 이야기</div>', unsafe_allow_html=True)
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image(str(FRIEND_IMAGE), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="caption">🤝 육공회 — 함께라서 더 즐거운 여행!</div>', unsafe_allow_html=True)
else:
    st.info("📸 fri.png 파일을 같은 폴더에 넣어주세요.")

st.markdown("---")

# ③ 위치 지도 이미지
st.markdown('<div class="section-label">📍 푸꾸옥 위치 — 베트남 최남단, 타이만의 진주섬</div>', unsafe_allow_html=True)

if MAP_IMAGE.exists():
    st.markdown('<div class="img-frame">', unsafe_allow_html=True)
    st.image(str(MAP_IMAGE), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="caption">
      🗺️ 호치민시에서 서쪽으로 약 260km &nbsp;·&nbsp; 캄보디아 국경 근처 &nbsp;·&nbsp; 면적 574km²
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("🗺️ puku.png 파일을 같은 폴더에 넣어주세요.")

# ④ 기본 정보 & 본문
st.markdown("""
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
""")

# ⑤ 푸터
st.markdown("""
<div class="footer">
  <div class="footer-wave">〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰</div>
  <div class="footer-text">
    🌺 육공회의 행복한 여행을 응원합니다! 🌺<br>
    <span style="font-size:0.85rem; opacity:0.75;">좋은 추억 가득한 푸꾸옥 여행 되세요 🌊✨</span>
  </div>
  <div class="footer-emojis">🌴 🐠 🍹 🌅 🐚 🦀 🏄 🌊 🌴</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
