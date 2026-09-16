import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI 여행친구 ✈️",
    page_icon="🌷",
    layout="centered"
)

# -----------------------------
# 여행지 데이터
# -----------------------------
travel_data = {
    "ISTJ": {
        "title": "차분하고 알찬 여행을 좋아하는 당신 💼",
        "place": "🇯🇵 교토, 일본",
        "description": "계획을 세우고 하나씩 구경하는 여행이 잘 어울려요. 전통 거리와 아름다운 사찰을 천천히 둘러보세요!",
        "spots": ["⛩️ 후시미이나리", "🌸 기온 거리", "🍵 아라시야마"],
        "color": "#E8F5E9"
    },
    "ISFJ": {
        "title": "따뜻하고 편안한 여행을 좋아하는 당신 🧸",
        "place": "🇯🇵 후쿠오카, 일본",
        "description": "맛있는 음식과 여유로운 산책을 즐길 수 있는 후쿠오카가 잘 어울려요. 부담 없이 힐링해보세요!",
        "spots": ["🍜 하카타 라멘", "🌊 모모치 해변", "🌿 오호리 공원"],
        "color": "#FFF3E0"
    },
    "INFJ": {
        "title": "감성과 의미를 찾아 떠나는 당신 🌙",
        "place": "🇫🇷 파리, 프랑스",
        "description": "예술과 낭만, 조용한 골목길을 좋아한다면 파리가 딱이에요. 카페에서 여유롭게 시간을 보내보세요.",
        "spots": ["🗼 에펠탑", "🎨 루브르 박물관", "☕ 몽마르트르"],
        "color": "#F3E5F5"
    },
    "INTJ": {
        "title": "새로운 세계를 탐험하는 전략가 🔭",
        "place": "🇸🇬 싱가포르",
        "description": "효율적인 도시 여행과 독특한 건축물을 좋아한다면 싱가포르를 추천해요!",
        "spots": ["🌳 가든스 바이 더 베이", "🏙️ 마리나 베이", "🦁 센토사"],
        "color": "#E3F2FD"
    },
    "ISTP": {
        "title": "자유롭게 움직이는 모험가 🛵",
        "place": "🇹🇭 치앙마이, 태국",
        "description": "정해진 일정 없이 마음 가는 대로 돌아다니는 여행을 즐겨보세요!",
        "spots": ["🏔️ 도이수텝", "☕ 감성 카페", "🌿 님만해민"],
        "color": "#E0F7FA"
    },
    "ISFP": {
        "title": "감성을 충전하는 예술가 🎨",
        "place": "🇮🇹 피렌체, 이탈리아",
        "description": "예쁜 골목과 맛있는 음식, 아름다운 예술 작품을 천천히 즐겨보세요.",
        "spots": ["🎨 우피치 미술관", "🌉 베키오 다리", "🍕 피렌체 골목"],
        "color": "#FCE4EC"
    },
    "INFP": {
        "title": "동화 같은 여행을 꿈꾸는 당신 🧚",
        "place": "🇨🇭 인터라켄, 스위스",
        "description": "아름다운 자연 속에서 조용히 나만의 시간을 가져보세요. 동화 속에 들어온 기분이 들 거예요.",
        "spots": ["🏔️ 융프라우", "🚞 산악열차", "🌿 호수 산책"],
        "color": "#F1F8E9"
    },
    "INTP": {
        "title": "호기심 가득한 탐험가 🔬",
        "place": "🇩🇪 베를린, 독일",
        "description": "역사와 과학, 독특한 문화가 공존하는 베를린에서 새로운 것을 발견해보세요!",
        "spots": ["🏛️ 박물관섬", "🧱 베를린 장벽", "🎨 이스트 사이드 갤러리"],
        "color": "#EDE7F6"
    },
    "ESTP": {
        "title": "신나게 즐기는 액티비티 마스터 🎢",
        "place": "🇦🇺 골드코스트, 호주",
        "description": "바다와 액티비티를 좋아한다면 골드코스트! 신나는 하루를 마음껏 즐겨보세요.",
        "spots": ["🏄 서퍼스 파라다이스", "🎢 테마파크", "🌊 해변 드라이브"],
        "color": "#FFF8E1"
    },
    "ESFP": {
        "title": "즐거움이 가득한 파티 여행자 🎉",
        "place": "🇪🇸 바르셀로나, 스페인",
        "description": "맛있는 음식과 예쁜 건축물, 활기찬 분위기를 모두 즐길 수 있는 도시예요!",
        "spots": ["⛪ 사그라다 파밀리아", "🥘 타파스", "🏖️ 바르셀로네타"],
        "color": "#FFEBEE"
    },
    "ENFP": {
        "title": "설렘을 찾아 떠나는 자유로운 영혼 🌈",
        "place": "🇵🇹 리스본, 포르투갈",
        "description": "예쁜 골목과 알록달록한 풍경을 따라 걷다 보면 새로운 재미를 계속 발견할 수 있어요!",
        "spots": ["🚋 트램 28", "🌊 벨렝", "🍮 에그타르트"],
        "color": "#FFF3E0"
    },
    "ENTP": {
        "title": "새로운 경험을 찾아다니는 아이디어 뱅크 💡",
        "place": "🇺🇸 뉴욕, 미국",
        "description": "볼거리도 많고 매일 새로운 일이 벌어지는 뉴욕에서 마음껏 돌아다녀보세요!",
        "spots": ["🗽 자유의 여신상", "🌳 센트럴파크", "🎭 브로드웨이"],
        "color": "#E8EAF6"
    },
    "ESTJ": {
        "title": "알차게 정복하는 여행 리더 👑",
        "place": "🇬🇧 런던, 영국",
        "description": "유명 명소부터 맛집까지 알차게 돌아보는 여행을 즐겨보세요!",
        "spots": ["🎡 런던아이", "🏰 타워 브리지", "☕ 애프터눈 티"],
        "color": "#E3F2FD"
    },
    "ESFJ": {
        "title": "함께라서 더 행복한 여행자 💕",
        "place": "🇰🇷 제주도, 대한민국",
        "description": "친구나 가족과 함께 맛있는 것도 먹고 예쁜 풍경도 보는 여행을 추천해요!",
        "spots": ["🌊 협재해변", "🌸 유채꽃길", "🍊 제주 카페"],
        "color": "#FFF0F5"
    },
    "ENFJ": {
        "title": "사람과 추억을 사랑하는 여행자 🌷",
        "place": "🇮🇹 로마, 이탈리아",
        "description": "사람들과 함께 역사와 문화를 느끼고 맛있는 음식을 즐겨보세요!",
        "spots": ["🏛️ 콜로세움", "⛲ 트레비 분수", "🍝 로마 맛집"],
        "color": "#FCE4EC"
    },
    "ENTJ": {
        "title": "세상을 누비는 당당한 리더 🚀",
        "place": "🇦🇪 두바이, UAE",
        "description": "화려한 도시와 새로운 경험을 좋아하는 당신에게 잘 어울리는 여행지예요!",
        "spots": ["🏙️ 부르즈 할리파", "🏝️ 팜 주메이라", "🛍️ 두바이 몰"],
        "color": "#E8EAF6"
    }
}

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #FFF8FC 0%, #F7F9FF 100%);
    }

    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #FF6F91;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #777777;
        margin-bottom: 35px;
    }

    .cute-box {
        background: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    .result-title {
        font-size: 25px;
        font-weight: 700;
        color: #555555;
        margin-bottom: 8px;
    }

    .destination {
        font-size: 38px;
        font-weight: 800;
        color: #FF6F91;
        margin: 10px 0;
    }

    .description {
        font-size: 17px;
        line-height: 1.7;
        color: #666666;
    }

    .spot {
        background: rgba(255,255,255,0.75);
        padding: 12px;
        border-radius: 15px;
        margin: 7px 0;
        font-size: 16px;
    }

    .footer {
        text-align: center;
        color: #AAAAAA;
        margin-top: 40px;
        font-size: 14px;
    }

    div.stButton > button {
        border-radius: 20px;
        border: none;
        background: #FF8FAB;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 25px;
    }

    div.stButton > button:hover {
        background: #FF6F91;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    '<div class="main-title">🌷 MBTI 여행친구 ✈️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">나와 찰떡궁합인 여행지를 찾아볼까요? 🧳💕</div>',
    unsafe_allow_html=True
)

# -----------------------------
# MBTI 선택
# -----------------------------
st.markdown(
    '<div class="cute-box">',
    unsafe_allow_html=True
)

mbti = st.selectbox(
    "💌 나의 MBTI를 골라주세요!",
    list(travel_data.keys()),
    index=None,
    placeholder="MBTI를 선택해주세요 🌸"
)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 추천 버튼
# -----------------------------
if mbti:
    if st.button("💖 여행지 추천받기!", use_container_width=True):

        data = travel_data[mbti]

        st.balloons()

        st.markdown(
            f"""
            <div class="cute-box" style="background:{data['color']}">
                <div class="result-title">{data['title']}</div>
                <div class="destination">{data['place']}</div>
                <div class="description">
                    {data['description']}
                </div>
                <br>
                <b>✨ 이런 곳을 가보세요!</b>
            """,
            unsafe_allow_html=True
        )

        for spot in data["spots"]:
            st.markdown(
                f'<div class="spot">{spot}</div>',
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="cute-box">
                <div style="text-align:center; font-size:20px;">
                    🌸 <b>{mbti}</b> 여행자의 행복한 여행을 응원해요! 🌸
                </div>
                <div style="text-align:center; margin-top:10px; color:#888;">
                    좋은 여행은 좋은 추억이 됩니다 💕
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# 하단
# -----------------------------
st.markdown(
    '<div class="footer">Made with 💕 for happy travelers ✈️🌷</div>',
    unsafe_allow_html=True
)
