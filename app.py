import random
from html import escape
from textwrap import dedent

import streamlit as st


# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------
st.set_page_config(
    page_title="Veda The Queen 👑",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# HTML rendering helper
# ---------------------------------------------------------
def render_html(source: str):
    """Render HTML without Streamlit displaying it as code."""
    compact_html = " ".join(
        line.strip()
        for line in dedent(source).splitlines()
        if line.strip()
    )

    st.markdown(compact_html, unsafe_allow_html=True)


# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown(
    dedent(
        """
        <style>
            /* ---------------------------------------------
               REMOVE THE SIDEBAR COMPLETELY
            --------------------------------------------- */
            section[data-testid="stSidebar"],
            [data-testid="stSidebar"],
            [data-testid="stSidebarCollapsedControl"],
            [data-testid="collapsedControl"] {
                display: none !important;
            }

            /* Prevent the hidden sidebar from taking space */
            [data-testid="stAppViewContainer"] {
                margin-left: 0 !important;
            }

            /* Main page width and spacing */
            .main .block-container,
            [data-testid="stMainBlockContainer"] {
                max-width: 1400px !important;
                padding-top: 2.5rem !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
                padding-bottom: 2rem !important;
            }

            header[data-testid="stHeader"] {
                background: transparent !important;
            }

            /* ---------------------------------------------
               PAGE BACKGROUND
            --------------------------------------------- */
            .stApp,
            [data-testid="stAppViewContainer"] {
                background:
                    radial-gradient(
                        circle at top left,
                        #fff0f6 0%,
                        transparent 35%
                    ),
                    radial-gradient(
                        circle at top right,
                        #f3e8ff 0%,
                        transparent 35%
                    ),
                    linear-gradient(
                        135deg,
                        #fffafc 0%,
                        #fff4f8 50%,
                        #f8f0ff 100%
                    ) !important;
            }

            /* ---------------------------------------------
               MAKE ALL NORMAL TEXT VISIBLE
            --------------------------------------------- */
            .stApp,
            .stApp p,
            .stApp span,
            .stApp label,
            .stApp li,
            .stApp h1,
            .stApp h2,
            .stApp h3,
            .stApp h4,
            .stApp h5,
            .stApp h6,
            [data-testid="stMarkdownContainer"],
            [data-testid="stMarkdownContainer"] p,
            [data-testid="stMarkdownContainer"] span,
            [data-testid="stWidgetLabel"],
            [data-testid="stWidgetLabel"] p,
            [data-testid="stCaptionContainer"],
            [data-testid="stCaptionContainer"] p {
                color: #41243c !important;
            }

            /* ---------------------------------------------
               HERO SECTION
            --------------------------------------------- */
            .hero {
                text-align: center;
                padding: 3rem 1.5rem;
                margin-bottom: 1.5rem;
                border-radius: 30px;
                background: linear-gradient(
                    135deg,
                    #d63384,
                    #8b5cf6
                );
                box-shadow:
                    0 18px 45px rgba(139, 92, 246, 0.25);
                position: relative;
                overflow: hidden;
            }

            .hero::before,
            .hero::after {
                content: "❤";
                position: absolute;
                font-size: 8rem;
                opacity: 0.08;
                color: white;
            }

            .hero::before {
                left: 4%;
                top: -25px;
                transform: rotate(-20deg);
            }

            .hero::after {
                right: 5%;
                bottom: -50px;
                transform: rotate(20deg);
            }

            /* Keep all hero text white */
            .hero,
            .hero *,
            .hero h1,
            .hero h2,
            .hero p,
            .hero span,
            .hero strong {
                color: #ffffff !important;
            }

            .hero h1 {
                font-size: clamp(2.7rem, 7vw, 5.5rem);
                margin: 0 !important;
                line-height: 1.1;
                font-weight: 800;
            }

            .hero h2 {
                font-weight: 500;
                margin-top: 0.8rem;
                margin-bottom: 0.8rem;
            }

            .hero p {
                font-size: 1.08rem;
                margin-bottom: 0;
            }

            .crown {
                display: inline-block;
                font-size: 4.5rem;
                animation: float 2.5s ease-in-out infinite;
            }

            @keyframes float {
                0%, 100% {
                    transform: translateY(0) rotate(-3deg);
                }

                50% {
                    transform: translateY(-12px) rotate(3deg);
                }
            }

            /* ---------------------------------------------
               METRIC CARDS
            --------------------------------------------- */
            [data-testid="stMetric"] {
                background: rgba(255, 255, 255, 0.95) !important;
                border: 1px solid #e9bfd7;
                padding: 1.2rem !important;
                border-radius: 18px;
                text-align: center;
                box-shadow:
                    0 8px 25px rgba(106, 48, 89, 0.08);
            }

            [data-testid="stMetricLabel"],
            [data-testid="stMetricLabel"] p,
            [data-testid="stMetricLabel"] div {
                color: #70425f !important;
                font-weight: 700 !important;
            }

            [data-testid="stMetricValue"],
            [data-testid="stMetricValue"] div {
                color: #b4236c !important;
                font-weight: 800 !important;
            }

            /* ---------------------------------------------
               CHARACTER CARDS
            --------------------------------------------- */
            .card-grid {
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(220px, 1fr));
                gap: 1rem;
                margin: 1.3rem 0;
            }

            .veda-card {
                background: rgba(255, 255, 255, 0.95);
                color: #41243c !important;
                padding: 1.5rem;
                border-radius: 22px;
                border: 1px solid #f1d5e5;
                box-shadow:
                    0 8px 25px rgba(106, 48, 89, 0.08);
                transition:
                    transform 0.2s ease,
                    box-shadow 0.2s ease;
            }

            .veda-card:hover {
                transform: translateY(-6px);
                box-shadow:
                    0 14px 32px rgba(106, 48, 89, 0.15);
            }

            .veda-card h3 {
                color: #b4236c !important;
                margin-top: 0;
                margin-bottom: 1rem;
            }

            .veda-card p {
                color: #41243c !important;
                line-height: 1.7;
            }

            /* ---------------------------------------------
               STRENGTH TIMELINE
            --------------------------------------------- */
            .timeline-card {
                background: #ffffff;
                color: #41243c !important;
                border-left: 6px solid #d63384;
                border-radius: 12px 22px 22px 12px;
                padding: 1.3rem 1.5rem;
                margin: 1rem 0;
                box-shadow:
                    0 8px 25px rgba(106, 48, 89, 0.08);
            }

            .timeline-card h3 {
                color: #b4236c !important;
            }

            .timeline-card p {
                color: #41243c !important;
                line-height: 1.7;
            }

            /* ---------------------------------------------
               LOVE MESSAGE CARD
            --------------------------------------------- */
            .big-love {
                text-align: center;
                padding: 2rem;
                border-radius: 24px;
                background: linear-gradient(
                    135deg,
                    #ffe0ec,
                    #ede2ff
                );
                font-size: 1.4rem;
                color: #8d1b57 !important;
                font-weight: 700;
                animation:
                    glow 1.8s ease-in-out infinite alternate;
            }

            .big-love * {
                color: #8d1b57 !important;
            }

            @keyframes glow {
                from {
                    box-shadow:
                        0 0 10px rgba(214, 51, 132, 0.15);
                }

                to {
                    box-shadow:
                        0 0 28px rgba(214, 51, 132, 0.35);
                }
            }

            /* ---------------------------------------------
               LOVE LETTER
            --------------------------------------------- */
            .letter {
                background: #fffdf8;
                color: #41243c !important;
                border: 1px solid #edd9c8;
                border-radius: 24px;
                padding: 2rem;
                line-height: 1.9;
                font-family: Georgia, serif;
                font-size: 1.08rem;
                box-shadow:
                    0 12px 32px rgba(106, 48, 89, 0.11);
            }

            .letter,
            .letter p,
            .letter span,
            .letter strong {
                color: #41243c !important;
            }

            /* ---------------------------------------------
               BUTTONS
            --------------------------------------------- */
            .stButton > button,
            .stDownloadButton > button,
            .stFormSubmitButton > button {
                border: none !important;
                border-radius: 999px !important;
                padding: 0.65rem 1.25rem !important;
                font-weight: 700 !important;
                color: #ffffff !important;
                background: linear-gradient(
                    90deg,
                    #d63384,
                    #8b5cf6
                ) !important;
                transition:
                    transform 0.2s ease,
                    box-shadow 0.2s ease;
            }

            .stButton > button:hover,
            .stDownloadButton > button:hover,
            .stFormSubmitButton > button:hover {
                color: #ffffff !important;
                transform: translateY(-2px);
                box-shadow:
                    0 8px 18px rgba(139, 92, 246, 0.25);
            }

            /* Keep all text inside buttons white */
            .stButton > button *,
            .stDownloadButton > button *,
            .stFormSubmitButton > button * {
                color: #ffffff !important;
            }

            /* ---------------------------------------------
               TABS
            --------------------------------------------- */
            .stTabs [data-baseweb="tab-list"] {
                gap: 0.4rem;
            }

            .stTabs [data-baseweb="tab"] {
                background: rgba(255, 255, 255, 0.8);
                border-radius: 12px 12px 0 0;
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .stTabs [data-baseweb="tab"] p,
            .stTabs [data-baseweb="tab"] span {
                color: #6f365b !important;
                font-weight: 700 !important;
            }

            .stTabs [aria-selected="true"] {
                background: #ffe0ec !important;
            }

            .stTabs [aria-selected="true"] p,
            .stTabs [aria-selected="true"] span {
                color: #c21f70 !important;
            }

            /* ---------------------------------------------
               INPUTS AND SELECT BOXES
            --------------------------------------------- */
            [data-baseweb="input"],
            [data-baseweb="textarea"],
            [data-baseweb="select"] > div {
                background-color: #ffffff !important;
                color: #41243c !important;
                border-color: #d9a9c5 !important;
            }

            input,
            textarea {
                background-color: #ffffff !important;
                color: #41243c !important;
                -webkit-text-fill-color: #41243c !important;
            }

            input::placeholder,
            textarea::placeholder {
                color: #916f84 !important;
                opacity: 1 !important;
            }

            [data-baseweb="select"] span,
            [data-baseweb="select"] div {
                color: #41243c !important;
            }

            [data-baseweb="tag"] {
                background-color: #f7d7e8 !important;
            }

            [data-baseweb="tag"] span {
                color: #7e2458 !important;
            }

            [role="listbox"],
            [role="option"] {
                background-color: #ffffff !important;
                color: #41243c !important;
            }

            /* ---------------------------------------------
               INFORMATION AND SUCCESS MESSAGES
            --------------------------------------------- */
            [data-testid="stAlert"] {
                background-color: rgba(
                    255,
                    255,
                    255,
                    0.95
                ) !important;
                border: 1px solid #e7bfd6 !important;
            }

            [data-testid="stAlert"] p,
            [data-testid="stAlert"] span,
            [data-testid="stAlert"] div {
                color: #41243c !important;
            }

            /* Form and bordered container backgrounds */
            [data-testid="stForm"],
            [data-testid="stVerticalBlockBorderWrapper"] {
                background: rgba(255, 255, 255, 0.7);
                border-radius: 18px;
            }

            /* Divider */
            hr {
                border-color: #e6bfd6 !important;
            }

            /* ---------------------------------------------
               FOOTER
            --------------------------------------------- */
            .footer {
                text-align: center;
                color: #70425f !important;
                margin-top: 3rem;
                padding: 1.5rem;
            }

            .footer,
            .footer strong {
                color: #70425f !important;
            }

            /* ---------------------------------------------
               MOBILE RESPONSIVENESS
            --------------------------------------------- */
            @media (max-width: 768px) {
                .main .block-container,
                [data-testid="stMainBlockContainer"] {
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                    padding-top: 1.5rem !important;
                }

                .hero {
                    padding: 2rem 1rem;
                    border-radius: 22px;
                }

                .hero h1 {
                    font-size: 2.7rem;
                }

                .hero h2 {
                    font-size: 1.4rem;
                }

                .card-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """
    ),
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------
if "love_taps" not in st.session_state:
    st.session_state.love_taps = 0

if "reason" not in st.session_state:
    st.session_state.reason = None

if "compliment" not in st.session_state:
    st.session_state.compliment = None

if "memories" not in st.session_state:
    st.session_state.memories = []

if "final_surprise" not in st.session_state:
    st.session_state.final_surprise = False


# ---------------------------------------------------------
# Sender name
# Change this text to your own name
# ---------------------------------------------------------
sender_name = "Mahendra"
safe_sender = escape(sender_name)


# ---------------------------------------------------------
# Hero section
# ---------------------------------------------------------
render_html(
    f"""
    <div class="hero">
        <div class="crown">👑</div>

        <h1>Veda The Queen</h1>

        <h2>
            Sweet. Caring. Loving. Strong.
        </h2>

        <p>
            A little corner of the internet made with endless love by
            <strong>{safe_sender}</strong>.
        </p>
    </div>
    """
)


# ---------------------------------------------------------
# Metrics
# ---------------------------------------------------------
metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        label="Children Raised With Courage",
        value="2",
    )

with metric2:
    st.metric(
        label="Love for Veda",
        value="∞",
    )

with metric3:
    st.metric(
        label="One Unforgettable Queen",
        value="1 👑",
    )


# ---------------------------------------------------------
# Heart buttons
# ---------------------------------------------------------
action1, action2 = st.columns(2)

with action1:
    if st.button(
        "💗 Send a Heart to Veda",
        use_container_width=True,
        type="primary",
    ):
        st.session_state.love_taps += 1
        st.balloons()

with action2:
    if st.button(
        "👑 Crown Veda Again",
        use_container_width=True,
    ):
        st.session_state.love_taps += 5
        st.balloons()

        st.success(
            "Veda has been crowned Queen of every heart!"
        )


st.caption(
    f"Veda has received "
    f"{st.session_state.love_taps:,} virtual hearts "
    f"in this session. 💕"
)


# ---------------------------------------------------------
# Main interactive sections
# ---------------------------------------------------------
home_tab, love_tab, strength_tab, memory_tab, letter_tab = st.tabs(
    [
        "🏠 For Veda",
        "💗 Love Meter",
        "💪 Her Strength",
        "🌷 Memory Garden",
        "💌 Love Letter",
    ]
)


# ---------------------------------------------------------
# Home tab
# ---------------------------------------------------------
with home_tab:
    st.header("The Wonderful Veda")

    render_html(
        """
        <div class="card-grid">
            <div class="veda-card">
                <h3>🌸 Sweet</h3>

                <p>
                    Veda's sweetness makes ordinary moments feel
                    special. Her gentle nature brings comfort,
                    happiness, and peace.
                </p>
            </div>

            <div class="veda-card">
                <h3>🤗 Caring</h3>

                <p>
                    She notices what others need and gives from
                    her heart. Her care can be felt even in the
                    smallest things she does.
                </p>
            </div>

            <div class="veda-card">
                <h3>💞 Loving</h3>

                <p>
                    Her love is warm, patient, and unconditional.
                    It is the kind of love that helps people feel
                    safe and understood.
                </p>
            </div>

            <div class="veda-card">
                <h3>🦋 Strong</h3>

                <p>
                    Behind her gentle smile is a courageous woman
                    who has faced life's challenges without losing
                    her beautiful heart.
                </p>
            </div>
        </div>
        """
    )

    render_html(
        """
        <div class="big-love">
            Veda, your strength made a family feel safe,
            and your sweetness made that family feel loved.
            You are truly extraordinary. 💖
        </div>
        """
    )


# ---------------------------------------------------------
# Love meter tab
# ---------------------------------------------------------
with love_tab:
    st.header("How Much Do I Love Veda?")

    love_level = st.slider(
        label="Try to measure my love for Veda",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
    )

    st.progress(love_level)

    if love_level < 25:
        st.info(
            "That is only the beginning—the real amount "
            "is much greater. 💗"
        )

    elif love_level < 75:
        st.info(
            "Getting closer, but no number can fully "
            "measure it. 💞"
        )

    elif love_level < 100:
        st.success(
            "Almost full, but my love still goes far "
            "beyond this meter. 💖"
        )

    else:
        st.success(
            "100% on the meter—and still nowhere near enough. "
            "My love for Veda is infinite. ♾️"
        )

    st.divider()

    reasons = [
        "Because your sweetness makes difficult days feel lighter.",
        "Because your caring heart always makes people feel seen.",
        "Because you remained loving even when life demanded so much from you.",
        "Because you raised two children independently with courage and devotion.",
        "Because your sacrifices helped build a safer and brighter future.",
        "Because you are gentle without ever being weak.",
        "Because your smile carries warmth, comfort, and hope.",
        "Because you give love without asking for recognition.",
        "Because your strength inspires everyone fortunate enough to know you.",
        "Simply because you are Veda—and there is no one else like you.",
    ]

    if st.button(
        "✨ Tell Veda One Reason",
        use_container_width=True,
    ):
        st.session_state.reason = random.choice(reasons)

    if st.session_state.reason:
        safe_reason = escape(st.session_state.reason)

        render_html(
            f"""
            <div class="big-love">
                {safe_reason}
            </div>
            """
        )

    st.subheader("Create a Compliment for Veda")

    selected_qualities = st.multiselect(
        label="Choose the qualities that describe her",
        options=[
            "sweet",
            "caring",
            "loving",
            "strong",
            "beautiful",
            "selfless",
            "brave",
            "graceful",
            "inspiring",
        ],
        default=[
            "sweet",
            "caring",
            "loving",
            "strong",
        ],
    )

    def natural_join(items):
        if len(items) == 1:
            return items[0]

        if len(items) == 2:
            return f"{items[0]} and {items[1]}"

        return ", ".join(items[:-1]) + f", and {items[-1]}"

    if st.button(
        "💫 Create Her Compliment",
        use_container_width=True,
    ):
        if selected_qualities:
            qualities_text = natural_join(selected_qualities)

            st.session_state.compliment = (
                f"Veda, you are {qualities_text}. "
                "The love and strength you carry make you "
                "truly one of a kind."
            )

        else:
            st.warning(
                "Choose at least one beautiful quality."
            )

    if st.session_state.compliment:
        st.success(st.session_state.compliment)


# ---------------------------------------------------------
# Strength tab
# ---------------------------------------------------------
with strength_tab:
    st.header("The Strength Behind Her Gentle Heart")

    render_html(
        """
        <div class="timeline-card">
            <h3>🌱 A Life of Sacrifice</h3>

            <p>
                Veda, so many of your sacrifices may have
                happened quietly: the long days, the hidden
                worries, the difficult choices, and the times
                you placed your children's needs before your own.
                Those sacrifices are seen, respected, and deeply
                appreciated.
            </p>
        </div>

        <div class="timeline-card">
            <h3>👩‍👧‍👦 Raising Two Children Independently</h3>

            <p>
                You carried responsibility, made difficult
                decisions, and kept moving forward while raising
                two children independently. You gave them more
                than care—you gave them courage, stability,
                guidance, and unconditional love.
            </p>
        </div>

        <div class="timeline-card">
            <h3>💪 Strength Without Losing Sweetness</h3>

            <p>
                Life asked you to be strong, but strength never
                made your heart hard. You remained sweet, caring,
                gentle, and loving. That is one of the most
                beautiful things about you.
            </p>
        </div>

        <div class="timeline-card">
            <h3>👑 A Queen in Every Sense</h3>

            <p>
                A true queen is not defined by a crown. She is
                defined by the lives she protects, the love she
                gives, and the hope she creates. Veda, that is
                why you will always be The Queen.
            </p>
        </div>
        """
    )

    if st.button(
        "🌟 Celebrate Veda's Strength",
        use_container_width=True,
    ):
        st.balloons()

        st.success(
            "For every challenge Veda overcame, every sacrifice "
            "she made, and every loving moment she created—we "
            "celebrate her!"
        )


# ---------------------------------------------------------
# Memory garden tab
# ---------------------------------------------------------
with memory_tab:
    st.header("Veda's Memory Garden 🌷")

    st.write(
        "Add your favorite moments with Veda. "
        "Each memory becomes another flower in "
        "her virtual garden."
    )

    with st.form(
        key="memory_form",
        clear_on_submit=True,
    ):
        memory_title = st.text_input(
            label="Memory title",
            placeholder=(
                "For example: The day your smile made "
                "everything better"
            ),
        )

        memory_text = st.text_area(
            label="Write the memory",
            placeholder=(
                "Describe a beautiful, funny, or meaningful "
                "moment with Veda..."
            ),
        )

        add_memory = st.form_submit_button(
            label="🌷 Plant This Memory",
            use_container_width=True,
        )

    if add_memory:
        if memory_text.strip():
            st.session_state.memories.append(
                {
                    "title": (
                        memory_title.strip()
                        or "A Beautiful Memory"
                    ),
                    "text": memory_text.strip(),
                }
            )

            st.success(
                "A new memory has bloomed in "
                "Veda's garden! 🌸"
            )

            st.balloons()

        else:
            st.warning(
                "Write a memory before planting it."
            )

    if st.session_state.memories:
        st.subheader("Flowers in Her Garden")

        for memory in reversed(st.session_state.memories):
            with st.container(border=True):
                st.markdown(
                    f"### 🌺 {memory['title']}"
                )

                st.write(memory["text"])

        if st.button(
            "Clear Memory Garden",
            use_container_width=True,
        ):
            st.session_state.memories = []
            st.rerun()

    else:
        st.info(
            "The garden is waiting for its first memory. "
            "Plant one using the form above."
        )

    st.caption(
        "Memories are stored only for the current browser "
        "session and are not uploaded elsewhere."
    )


# ---------------------------------------------------------
# Letter tab
# ---------------------------------------------------------
with letter_tab:
    st.header("A Letter for Veda The Queen")

    letter_text = f"""Dear Veda The Queen,

I wish words could fully express how much I love and appreciate you.

You have spent so much of your life giving, caring, and making sacrifices for the people you love. Many of those sacrifices may have happened quietly, without recognition, but they have never been meaningless. They built a family, created safety, and gave two children the courage to move forward.

Raising two children independently required a kind of strength that is difficult to put into words. You carried responsibilities, faced difficult days, made hard choices, and kept going even when you may have been tired.

Yet through everything, you remained sweet, caring, loving, and kind. Life made you strong, but it never took away the gentleness in your heart.

I love you for your warmth.
I admire you for your courage.
I respect you for your sacrifices.
I am grateful for every moment of care you have given.

You are not only strong because of what you survived. You are extraordinary because you continued to love so deeply through it all.

Veda, you deserve happiness, peace, appreciation, laughter, and all the love you have given to return to you many times over.

You are our strength, our comfort, and forever our Queen.

With all my love,

{sender_name}
"""

    render_html(
        f"""
        <div class="letter">
            <strong>Dear Veda The Queen,</strong>
            <br><br>

            I wish words could fully express how much I love
            and appreciate you.
            <br><br>

            You have spent so much of your life giving, caring,
            and making sacrifices for the people you love.
            Many of those sacrifices may have happened quietly,
            without recognition, but they have never been
            meaningless. They built a family, created safety,
            and gave two children the courage to move forward.
            <br><br>

            Raising two children independently required a kind
            of strength that is difficult to put into words.
            You carried responsibilities, faced difficult days,
            made hard choices, and kept going even when you may
            have been tired.
            <br><br>

            Yet through everything, you remained sweet, caring,
            loving, and kind. Life made you strong, but it never
            took away the gentleness in your heart.
            <br><br>

            I love you for your warmth.
            <br>

            I admire you for your courage.
            <br>

            I respect you for your sacrifices.
            <br>

            I am grateful for every moment of care you have given.
            <br><br>

            You are not only strong because of what you survived.
            You are extraordinary because you continued to love
            so deeply through it all.
            <br><br>

            Veda, you deserve happiness, peace, appreciation,
            laughter, and all the love you have given to return
            to you many times over.
            <br><br>

            You are our strength, our comfort, and forever
            our Queen.
            <br><br>

            <strong>
                With all my love,
                <br>
                {safe_sender}
            </strong>
        </div>
        """
    )

    st.download_button(
        label="💌 Download Veda's Letter",
        data=letter_text,
        file_name="A_Letter_For_Veda_The_Queen.txt",
        mime="text/plain",
        use_container_width=True,
    )

    if st.button(
        "🎁 Open the Final Surprise",
        use_container_width=True,
    ):
        st.session_state.final_surprise = True
        st.balloons()

    if st.session_state.final_surprise:
        render_html(
            """
            <div class="big-love">
                Veda, if every sacrifice became a star,
                your sky would shine brighter than the universe.
                You are loved more than words can say—today,
                tomorrow, and always. 👑💖
            </div>
            """
        )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
render_html(
    """
    <div class="footer">
        Made with endless love for
        <strong>Veda The Queen</strong> 👑
        <br>
        Sweet • Caring • Loving • Strong
    </div>
    """
)