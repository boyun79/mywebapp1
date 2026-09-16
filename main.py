import streamlit as st
import random

# ==========================================
# 페이지 설정
# ==========================================
st.set_page_config(
    page_title="MBTI 최애 찾기 💗",
    page_icon="🎀",
    layout="centered"
)

# ==========================================
# K-POP 추천 데이터
# ==========================================
recommendations = {
    "ISTJ": {
        "idol": "RM",
        "group": "BTS",
        "emoji": "📚",
        "title": "차분하고 똑똑한 매력에 끌리는 당신",
        "message": "논리적이고 계획적인 ISTJ에게는 깊이 있는 생각과 차분한 매력이 돋보이는 RM을 추천해요!",
        "keywords": ["🧠 지적인 매력", "📖 깊은 생각", "🎨 예술 감성"]
    },
    "ISFJ": {
        "idol": "진",
        "group": "BTS",
        "emoji": "🐹",
        "title": "따뜻하고 다정한 사람이 좋은 당신",
        "message": "배려심 많고 따뜻한 ISFJ에게는 유쾌하면서도 다정한 진의 매력이 잘 어울려요!",
        "keywords": ["💕 다정함", "🍳 요리", "😂 유쾌함"]
    },
    "INFJ": {
        "idol": "우지",
        "group": "SEVENTEEN",
        "emoji": "🍚",
        "title": "섬세한 감성을 사랑하는 당신",
        "message": "섬세하고 깊이 있는 INFJ에게는 음악에 진심인 우지의 감성이 찰떡이에요!",
        "keywords": ["🎵 음악", "🌙 섬세함", "💭 감성"]
    },
    "INTJ": {
        "idol": "카리나",
        "group": "aespa",
        "emoji": "🖤",
        "title": "완벽하고 멋진 매력에 끌리는 당신",
        "message": "자신만의 목표가 뚜렷한 INTJ에게는 카리스마와 프로페셔널함이 돋보이는 카리나를 추천해요!",
        "keywords": ["✨ 카리스마", "🎯 프로페셔널", "👑 리더십"]
    },
    "ISTP": {
        "idol": "한",
        "group": "Stray Kids",
        "emoji": "🐿️",
        "title": "자유롭고 재치 있는 사람이 좋은 당신",
        "message": "쿨하고 독립적인 ISTP에게는 다재다능하고 재치 넘치는 한이 잘 어울려요!",
        "keywords": ["🎤 랩", "⚡ 재치", "🎸 다재다능"]
    },
    "ISFP": {
        "idol": "정국",
        "group": "BTS",
        "emoji": "🐰",
        "title": "자연스럽고 사랑스러운 매력에 끌리는 당신",
        "message": "감각적이고 자유로운 ISFP에게는 부드러운 분위기와 다양한 재능을 가진 정국을 추천해요!",
        "keywords": ["🎤 보컬", "🎨 감각", "🐰 사랑스러움"]
    },
    "INFP": {
        "idol": "아이유",
        "group": "Solo",
        "emoji": "🌷",
        "title": "따뜻한 감성과 이야기를 사랑하는 당신",
        "message": "상상력이 풍부한 INFP에게는 섬세한 음악과 따뜻한 이야기를 들려주는 아이유가 잘 어울려요!",
        "keywords": ["🌷 감성", "🎼 음악", "📖 이야기"]
    },
    "INTP": {
        "idol": "태용",
        "group": "NCT",
        "emoji": "🐯",
        "title": "독특하고 창의적인 매력을 좋아하는 당신",
        "message": "호기심 많은 INTP에게는 독특한 스타일과 창의적인 매력을 가진 태용을 추천해요!",
        "keywords": ["🎨 창의성", "🔥 퍼포먼스", "💡 독특함"]
    },
    "ESTP": {
        "idol": "리사",
        "group": "BLACKPINK",
        "emoji": "🐱",
        "title": "강렬하고 자신감 넘치는 매력에 끌리는 당신",
        "message": "에너지 넘치는 ESTP에게는 무대에서 강렬한 존재감을 보여주는 리사가 찰떡이에요!",
        "keywords": ["🔥 카리스마", "💃 퍼포먼스", "✨ 자신감"]
    },
    "ESFP": {
        "idol": "호시",
        "group": "SEVENTEEN",
        "emoji": "🐯",
        "title": "신나고 에너지 넘치는 사람이 좋은 당신",
        "message": "즐거움을 사랑하는 ESFP에게는 무대 위에서 에너지를 뿜어내는 호시를 추천해요!",
        "keywords": ["🐯 에너지", "💃 춤", "🎉 흥"]
    },
    "ENFP": {
        "idol": "승관",
        "group": "SEVENTEEN",
        "emoji": "🍊",
        "title": "밝고 사랑스러운 매력에 끌리는 당신",
        "message": "긍정 에너지가 넘치는 ENFP에게는 밝고 유쾌한 승관이 정말 잘 어울려요!",
        "keywords": ["🍊 밝음", "😂 예능감", "💕 따뜻함"]
    },
    "ENTP": {
        "idol": "제시",
        "group": "Solo",
        "emoji": "🔥",
        "title": "솔직하고 개성 있는 사람이 좋은 당신",
        "message": "아이디어가 넘치는 ENTP에게는 자신만의 개성을 확실하게 보여주는 제시를 추천해요!",
        "keywords": ["🔥 개성", "🎤 카리스마", "😂 솔직함"]
    },
    "ESTJ": {
        "idol": "수호",
        "group": "EXO",
        "emoji": "🐰",
        "title": "책임감 있고 믿음직한 사람이 좋은 당신",
        "message": "리더십이 강한 ESTJ에게는 책임감 있고 안정적인 매력을 가진 수호를 추천해요!",
        "keywords": ["👑 리더십", "💙 책임감", "🎵 보컬"]
    },
    "ESFJ": {
        "idol": "도경수",
        "group": "EXO",
        "emoji": "🐧",
        "title": "따뜻하고 편안한 매력을 좋아하는 당신",
        "message": "사람을 좋아하고 정이 많은 ESFJ에게는 편안하고 따뜻한 도경수가 잘 어울려요!",
        "keywords": ["🍳 요리", "🎬 연기", "💕 따뜻함"]
    },
    "ENFJ": {
        "idol": "방찬",
        "group": "Stray Kids",
        "emoji": "🐺",
        "title": "사람을 이끄는 따뜻한 리더가 좋은 당신",
        "message": "사람을 챙기고 응원하는 ENFJ에게는 따뜻한 리더십이 돋보이는 방찬을 추천해요!",
        "keywords": ["🐺 리더십", "💕 배려", "🎤 음악"]
    },
    "ENTJ": {
        "idol": "소연",
        "group": "(G)I-DLE",
        "emoji": "👑",
        "title": "당당하고 카리스마 있는 사람이 좋은 당신",
        "message": "목표를 향해 달려가는 ENTJ에게는 강한 리더십과 창작 능력을 보여주는 소연을 추천해요!",
        "keywords": ["👑 리더", "✍️ 프로듀싱", "🔥 카리스마"]
    }
}

# ==========================================
# CSS
# ==========================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        180deg,
        #fff5fa 0%,
        #f8f5ff 50%,
        #fffafa 100%
    );
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    color: #ff6b9a;
    margin-top: 20px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #888888;
    margin-bottom: 35px;
}

.ribbon {
    text-align: center;
    font-size: 35px;
    margin-bottom: 5px;
}

.select-box {
    background: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.result-card {
    background: white;
    padding: 35px;
    border-radius: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    text-align: center;
    margin-top: 25px;
    border: 2px solid #ffe0eb;
}

.result-emoji {
    font-size: 70px;
}

.result-idol {
    font-size: 40px;
    font-weight: 900;
    color: #ff5f91;
    margin: 5px;
}

.result-group {
    font-size: 18px;
    color: #999999;
}

.result-title {
    font-size: 22px;
    font-weight: 700;
    color: #555555;
    margin-top: 15px;
}

.message {
    font-size: 16px;
    line-height: 1.8;
    color: #777777;
    margin: 15px;
}

.keyword {
    background: #fff0f5;
    border-radius: 15px;
    padding: 10px;
    margin: 6px;
    font-size: 15px;
}

.footer {
    text-align: center;
    color: #bbbbbb;
    font-size: 13px;
    margin-top: 45px;
    margin-bottom: 20px;
}

div.stButton > button {
    border-radius: 25px;
    border: none;
    background: #ff82aa;
    color: white;
    font-size: 18px;
    font-weight: 700;
    padding: 12px;
}

div.stButton > button:hover {
    background: #ff5f91;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 제목
# ==========================================
st.markdown('<div class="ribbon">🎀 ✨ 🎀</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">💗 MBTI 최애 찾기 💗</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">나와 찰떡궁합인 K-POP 최애를 찾아보자! 🎤✨</div>',
    unsafe_allow_html=True
)

# ==========================================
# MBTI 선택
# ==========================================
st.markdown('<div class="select-box">', unsafe_allow_html=True)

st.markdown("### 🌸 먼저 MBTI를 골라주세요!")

mbti = st.selectbox(
    "나의 MBTI",
    list(recommendations.keys()),
    index=None,
    placeholder="💌 MBTI를 선택해주세요!"
)

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 추천
# ==========================================
if mbti:

    if st.button("🎀 내 최애 찾기 💗", use_container_width=True):

        result = recommendations[mbti]

        st.balloons()

        st.markdown(
            f"""
            <div class="result-card">

                <div class="result-emoji">
                    {result["emoji"]}
                </div>

                <div class="result-idol">
                    {result["idol"]}
                </div>

                <div class="result-group">
                    {result["group"]}
                </div>

                <div class="result-title">
                    {result["title"]}
                </div>

                <div class="message">
                    {result["message"]}
                </div>

                <hr>

                <div style="font-size:18px; font-weight:bold; color:#666;">
                    ✨ 이런 매력에 빠질 거예요! ✨
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # 키워드
        for keyword in result["keywords"]:
            st.markdown(
                f'<div class="keyword">{keyword}</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div style="
                text-align:center;
                margin-top:25px;
                color:#ff7da5;
                font-size:18px;
                font-weight:bold;
            ">
                💕 {mbti}인 당신의 새로운 최애를 응원해요! 💕
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================
# Footer
# ==========================================
st.markdown(
    '<div class="footer">Made with 💕 and a little bit of K-POP magic 🎤✨</div>',
    unsafe_allow_html=True
)
