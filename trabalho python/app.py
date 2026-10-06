import streamlit as st
import random

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="CodeQuest",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(105, 70, 255, 0.15), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(0, 220, 255, 0.10), transparent 30%),
        #080812;
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.hero {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        rgba(92, 54, 255, .30),
        rgba(15, 15, 35, .85)
    );
    border: 1px solid rgba(140, 110, 255, .35);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 52px;
    margin-bottom: 5px;
    font-weight: 800;
}

.hero p {
    color: #b9b9d0;
    font-size: 18px;
}

.card {
    background: rgba(20, 20, 35, .88);
    border: 1px solid rgba(120, 100, 255, .20);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 15px;
}

.card:hover {
    border-color: rgba(130, 110, 255, .5);
}

.stat {
    text-align: center;
    padding: 20px;
    background: rgba(25, 25, 45, .8);
    border-radius: 18px;
    border: 1px solid rgba(120, 100, 255, .2);
}

.stat-number {
    font-size: 30px;
    font-weight: 800;
}

.stat-label {
    color: #9999b5;
}

.quest {
    padding: 20px;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        rgba(28, 28, 50, .95),
        rgba(18, 18, 30, .95)
    );
    border: 1px solid rgba(120, 100, 255, .25);
    margin-bottom: 15px;
}

.quest-title {
    font-size: 21px;
    font-weight: 700;
}

.quest-description {
    color: #aaaac0;
}

.locked {
    opacity: .45;
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 4px;
    border-radius: 20px;
    background: rgba(100, 70, 255, .2);
    border: 1px solid rgba(120, 100, 255, .4);
}

.level {
    font-size: 25px;
    font-weight: 800;
}

.question-box {
    padding: 30px;
    border-radius: 22px;
    background: rgba(18, 18, 32, .95);
    border: 1px solid rgba(110, 90, 255, .35);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# BANCO DE QUESTÕES
# ============================================================

QUESTIONS = {

"Python": [

{
"q": "Qual comando é utilizado para mostrar uma mensagem na tela em Python?",
"options": ["print()", "show()", "display()", "write()"],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual símbolo é utilizado para criar um comentário de uma linha em Python?",
"options": ["//", "#", "--", "/*"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual será o valor de x?",
"options": ["5", "10", "15", "20"],
"answer": 2,
"difficulty": 1,
"code": "x = 10\nx = x + 5"
},

{
"q": "Qual é o tipo de dado de 3.14 em Python?",
"options": ["int", "str", "float", "bool"],
"answer": 2,
"difficulty": 1
},

{
"q": "Qual estrutura é utilizada para tomar decisões em Python?",
"options": ["if", "loop", "switch", "define"],
"answer": 0,
"difficulty": 1
},

{
"q": "O que será exibido?",
"options": ["10", "20", "30", "Erro"],
"answer": 1,
"difficulty": 2,
"code": "x = 10\nif x == 10:\n    print(20)"
},

{
"q": "Qual estrutura é normalmente utilizada para repetir um bloco um número conhecido de vezes?",
"options": ["if", "for", "def", "try"],
"answer": 1,
"difficulty": 2
},

{
"q": "Qual palavra-chave cria uma função em Python?",
"options": ["function", "func", "def", "method"],
"answer": 2,
"difficulty": 1
},

{
"q": "Qual estrutura representa uma lista em Python?",
"options": ["(1, 2, 3)", "[1, 2, 3]", "{1:2:3}", "<1,2,3>"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual índice representa o primeiro elemento de uma lista Python?",
"options": ["0", "1", "-1", "10"],
"answer": 0,
"difficulty": 2
},

{
"q": "Qual função retorna o tamanho de uma lista?",
"options": ["size()", "length()", "len()", "count()"],
"answer": 2,
"difficulty": 2
},

{
"q": "O que o operador == verifica?",
"options": [
"Se dois valores são iguais",
"Se dois valores são diferentes",
"Se um valor é maior",
"Se um valor é menor"
],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual operador representa 'diferente de' em Python?",
"options": ["<>", "!=", "!==", "not="],
"answer": 1,
"difficulty": 2
},

{
"q": "Qual comando permite receber dados digitados pelo usuário?",
"options": ["read()", "input()", "scan()", "get()"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual palavra-chave encerra imediatamente um loop?",
"options": ["stop", "exit", "break", "end"],
"answer": 2,
"difficulty": 2
},

],

"Lógica": [

{
"q": "Se A = 10 e B = 5, qual é o resultado de A > B?",
"options": ["Verdadeiro", "Falso", "10", "5"],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual operador lógico representa 'E'?",
"options": ["or", "and", "not", "xor"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual operador lógico representa 'OU'?",
"options": ["or", "and", "not", "if"],
"answer": 0,
"difficulty": 1
},

{
"q": "Se A é verdadeiro e B é falso, qual é o resultado de A AND B?",
"options": ["Verdadeiro", "Falso", "Erro", "Nenhum"],
"answer": 1,
"difficulty": 2
},

{
"q": "Se A é verdadeiro e B é falso, qual é o resultado de A OR B?",
"options": ["Verdadeiro", "Falso", "Erro", "Nenhum"],
"answer": 0,
"difficulty": 2
},

{
"q": "Qual conceito representa dividir um problema grande em problemas menores?",
"options": [
"Decomposição",
"Compilação",
"Renderização",
"Herança"
],
"answer": 0,
"difficulty": 1
},

{
"q": "O que é um algoritmo?",
"options": [
"Uma sequência de passos para resolver um problema",
"Um tipo de computador",
"Uma linguagem de programação",
"Uma placa de vídeo"
],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual estrutura é mais adequada quando queremos escolher entre duas possibilidades?",
"options": ["if/else", "for", "list", "import"],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual é o próximo número da sequência: 2, 4, 6, 8, ?",
"options": ["9", "10", "11", "12"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual é o resultado de 5 * 4 + 2?",
"options": ["30", "22", "20", "14"],
"answer": 1,
"difficulty": 2
},

],

"HTML/CSS": [

{
"q": "Qual linguagem é utilizada principalmente para estruturar páginas web?",
"options": ["Python", "HTML", "CSS", "SQL"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual tag HTML representa um título principal?",
"options": ["<title>", "<h1>", "<header>", "<head>"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual propriedade CSS altera a cor do texto?",
"options": ["text-color", "font-color", "color", "foreground"],
"answer": 2,
"difficulty": 1
},

{
"q": "Qual propriedade CSS altera a cor de fundo?",
"options": ["background-color", "bg", "background-style", "color-bg"],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual tag cria um link?",
"options": ["<link>", "<a>", "<url>", "<href>"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual tag representa uma imagem?",
"options": ["<picture>", "<image>", "<img>", "<src>"],
"answer": 2,
"difficulty": 1
},

{
"q": "Para que serve o CSS?",
"options": [
"Executar código Python",
"Estilizar páginas",
"Criar bancos de dados",
"Controlar servidores"
],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual propriedade altera o tamanho da fonte?",
"options": ["font-size", "text-size", "size", "font-height"],
"answer": 0,
"difficulty": 1
},

],

"JavaScript": [

{
"q": "Qual palavra-chave pode declarar uma variável em JavaScript?",
"options": ["var", "variable", "define", "letvar"],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual comando imprime informações no console?",
"options": [
"print()",
"console.log()",
"terminal.print()",
"write.console()"
],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual operador verifica igualdade estrita?",
"options": ["=", "==", "===", "!="],
"answer": 2,
"difficulty": 2
},

{
"q": "Qual palavra-chave cria uma função?",
"options": ["function", "def", "func", "method"],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual tipo representa verdadeiro ou falso?",
"options": ["String", "Boolean", "Integer", "Array"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual método adiciona um elemento ao final de um Array?",
"options": ["add()", "insert()", "push()", "append()"],
"answer": 2,
"difficulty": 2
},

{
"q": "Qual símbolo inicia um comentário de uma linha?",
"options": ["#", "//", "--", "/*"],
"answer": 1,
"difficulty": 1
},

{
"q": "Qual método transforma uma string em letras maiúsculas?",
"options": ["upper()", "toUpperCase()", "uppercase()", "makeUpper()"],
"answer": 1,
"difficulty": 2
},

],

"Fundamentos": [

{
"q": "O que significa CPU?",
"options": [
"Central Processing Unit",
"Computer Program Utility",
"Central Program User",
"Computer Processing Utility"
],
"answer": 0,
"difficulty": 1
},

{
"q": "O que é RAM?",
"options": [
"Memória de acesso aleatório",
"Processador",
"Placa de vídeo",
"Armazenamento permanente"
],
"answer": 0,
"difficulty": 1
},

{
"q": "Qual destes é um sistema operacional?",
"options": ["Python", "Windows", "HTML", "Git"],
"answer": 1,
"difficulty": 1
},

{
"q": "O que é uma variável?",
"options": [
"Um espaço utilizado para armazenar um valor",
"Um tipo de monitor",
"Uma placa eletrônica",
"Um sistema operacional"
],
"answer": 0,
"difficulty": 1
},

{
"q": "O que é um bug?",
"options": [
"Um erro ou comportamento inesperado no programa",
"Um tipo de linguagem",
"Um computador pequeno",
"Um arquivo de imagem"
],
"answer": 0,
"difficulty": 1
},

{
"q": "O que significa IDE?",
"options": [
"Integrated Development Environment",
"Internet Development Engine",
"Internal Data Editor",
"Integrated Digital Equipment"
],
"answer": 0,
"difficulty": 2
},

{
"q": "Para que serve o Git?",
"options": [
"Controle de versão",
"Edição de imagens",
"Criação de apresentações",
"Modelagem 3D"
],
"answer": 0,
"difficulty": 2
},

{
"q": "O que é um compilador?",
"options": [
"Programa que traduz código para uma forma executável",
"Um editor de imagens",
"Um navegador",
"Um banco de dados"
],
"answer": 0,
"difficulty": 2
},

]
}

# ============================================================
# INICIALIZAÇÃO
# ============================================================

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "coins" not in st.session_state:
    st.session_state.coins = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "correct" not in st.session_state:
    st.session_state.correct = 0

if "answered" not in st.session_state:
    st.session_state.answered = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "best_streak" not in st.session_state:
    st.session_state.best_streak = 0

if "page" not in st.session_state:
    st.session_state.page = "home"

if "subject" not in st.session_state:
    st.session_state.subject = None

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "answered_current" not in st.session_state:
    st.session_state.answered_current = False

if "achievements" not in st.session_state:
    st.session_state.achievements = []

if "completed" not in st.session_state:
    st.session_state.completed = {}

# ============================================================
# FUNÇÕES
# ============================================================

def calculate_level():
    return max(1, st.session_state.xp // 500 + 1)


def xp_to_next_level():
    current_level = calculate_level()
    return current_level * 500


def add_xp(amount):
    old_level = calculate_level()

    st.session_state.xp += amount

    new_level = calculate_level()

    if new_level > old_level:
        st.session_state.level = new_level
        st.balloons()

    else:
        st.session_state.level = new_level


def achievement(name):
    if name not in st.session_state.achievements:
        st.session_state.achievements.append(name)


def progress(subject):
    total = len(QUESTIONS[subject])
    done = st.session_state.completed.get(subject, 0)

    return min(done / total, 1)


def start_subject(subject):
    st.session_state.subject = subject
    st.session_state.current_question = 0
    st.session_state.answered_current = False
    st.session_state.page = "quiz"


def next_question():

    subject = st.session_state.subject

    total = len(QUESTIONS[subject])

    if st.session_state.current_question < total - 1:
        st.session_state.current_question += 1
        st.session_state.answered_current = False
        st.rerun()

    else:
        st.session_state.page = "result"
        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🎮 CodeQuest")

    st.divider()

    if st.button("🏠 Início", use_container_width=True):
        st.session_state.page = "home"

    if st.button("🗺️ Quests", use_container_width=True):
        st.session_state.page = "quests"

    if st.button("🏆 Conquistas", use_container_width=True):
        st.session_state.page = "achievements"

    if st.button("📊 Perfil", use_container_width=True):
        st.session_state.page = "profile"

    st.divider()

    st.markdown(f"### ⭐ Nível {calculate_level()}")

    st.progress(
        (st.session_state.xp % 500) / 500
    )

    st.caption(
        f"{st.session_state.xp % 500}/500 XP"
    )

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <h1>🎮 CodeQuest</h1>
    <p>
        Aprenda programação através de quizzes,
        quests e desafios.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HOME
# ============================================================

if st.session_state.page == "home":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-number">⭐ {st.session_state.xp}</div>
                <div class="stat-label">XP Total</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-number">🏆 {calculate_level()}</div>
                <div class="stat-label">Nível</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-number">🔥 {st.session_state.streak}</div>
                <div class="stat-label">Sequência</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-number">🪙 {st.session_state.coins}</div>
                <div class="stat-label">Moedas</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.subheader("🚀 Continue sua jornada")

    subjects = list(QUESTIONS.keys())

    cols = st.columns(2)

    icons = {
        "Python": "🐍",
        "Lógica": "🧠",
        "HTML/CSS": "🌐",
        "JavaScript": "⚡",
        "Fundamentos": "💻"
    }

    for i, subject in enumerate(subjects):

        with cols[i % 2]:

            p = progress(subject)

            st.markdown(
                f"""
                <div class="card">
                    <h2>{icons[subject]} {subject}</h2>
                    <p>Questões: {len(QUESTIONS[subject])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(p)

            if st.button(
                f"🎯 Jogar {subject}",
                key=f"home_{subject}",
                use_container_width=True
            ):
                start_subject(subject)
                st.rerun()

    st.write("")

    st.subheader("🎯 Como funciona?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>1️⃣ Escolha uma Quest</h3>
        Escolha uma disciplina e comece seu desafio.
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>2️⃣ Responda</h3>
        Cada pergunta testa seus conhecimentos.
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h3>3️⃣ Evolua</h3>
        Ganhe XP, suba de nível e desbloqueie conquistas.
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# QUESTS
# ============================================================

elif st.session_state.page == "quests":

    st.header("🗺️ Mapa de Quests")

    st.write(
        "Complete as disciplinas para se tornar um verdadeiro CodeMaster."
    )

    subjects = list(QUESTIONS.keys())

    for i, subject in enumerate(subjects):

        p = progress(subject)

        unlocked = (
            i == 0
            or progress(subjects[i - 1]) >= 0.5
        )

        if unlocked:

            st.markdown(
                f"""
                <div class="quest">
                    <div class="quest-title">
                        {i+1}. {subject}
                    </div>

                    <div class="quest-description">
                        Complete os quizzes de {subject}.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(p)

            if st.button(
                f"⚔️ Entrar na Quest de {subject}",
                key=f"quest_{subject}",
                use_container_width=True
            ):
                start_subject(subject)
                st.rerun()

        else:

            st.markdown(
                f"""
                <div class="quest locked">
                    <div class="quest-title">
                        🔒 {i+1}. {subject}
                    </div>

                    <div class="quest-description">
                        Complete pelo menos 50% da quest anterior.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# QUIZ
# ============================================================

elif st.session_state.page == "quiz":

    subject = st.session_state.subject
    questions = QUESTIONS[subject]

    index = st.session_state.current_question
    question = questions[index]

    st.header(f"{subject}")

    st.progress(
        (index + 1) / len(questions)
    )

    st.caption(
        f"Questão {index + 1} de {len(questions)}"
    )

    st.markdown(
        f"""
        <div class="question-box">
            <h2>{question["q"]}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    if "code" in question:

        st.code(
            question["code"],
            language="python"
        )

    answer = st.radio(
        "Escolha uma resposta:",
        question["options"],
        index=None,
        disabled=st.session_state.answered_current
    )

    if not st.session_state.answered_current:

        if st.button(
            "✅ Confirmar resposta",
            use_container_width=True
        ):

            if answer is None:
                st.warning("Escolha uma alternativa primeiro.")

            else:

                selected = question["options"].index(answer)

                st.session_state.answered_current = True
                st.session_state.answered += 1

                if selected == question["answer"]:

                    reward = 50 * question["difficulty"]

                    st.session_state.correct += 1
                    st.session_state.streak += 1

                    st.session_state.coins += 10

                    add_xp(reward)

                    st.session_state.completed[subject] = (
                        st.session_state.completed.get(subject, 0) + 1
                    )

                    if st.session_state.streak > st.session_state.best_streak:
                        st.session_state.best_streak = st.session_state.streak

                    achievement("🎯 Primeiro Acerto")

                    if st.session_state.correct >= 10:
                        achievement("🧠 10 Questões")

                    if st.session_state.streak >= 5:
                        achievement("🔥 Sequência de 5")

                    st.success(
                        f"🎉 Resposta correta! +{reward} XP"
                    )

                else:

                    st.session_state.streak = 0

                    st.error(
                        f"❌ Resposta incorreta. "
                        f"A resposta correta era: "
                        f"{question['options'][question['answer']]}"
                    )

    else:

        correct = question["answer"]

        st.info(
            f"💡 Resposta correta: "
            f"{question['options'][correct]}"
        )

    if st.session_state.answered_current:

        if index < len(questions) - 1:

            if st.button(
                "➡️ Próxima questão",
                use_container_width=True
            ):
                next_question()

        else:

            if st.button(
                "🏆 Finalizar Quest",
                use_container_width=True
            ):
                next_question()

# ============================================================
# RESULTADO
# ============================================================

elif st.session_state.page == "result":

    subject = st.session_state.subject

    total = len(QUESTIONS[subject])

    completed = st.session_state.completed.get(subject, 0)

    st.header("🏆 Quest concluída!")

    st.markdown(
        f"""
        <div class="hero">

        <h1>🎉 Parabéns!</h1>

        <p>
        Você terminou a jornada de {subject}.
        </p>

        <h2>
        ⭐ {st.session_state.xp} XP
        </h2>

        <h2>
        🏆 Nível {calculate_level()}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Questões respondidas",
            st.session_state.answered
        )

    with col2:
        st.metric(
            "Acertos",
            st.session_state.correct
        )

    with col3:
        st.metric(
            "Sequência máxima",
            st.session_state.best_streak
        )

    st.write("")

    if st.button(
        "🗺️ Voltar para Quests",
        use_container_width=True
    ):
        st.session_state.page = "quests"
        st.rerun()

# ============================================================
# CONQUISTAS
# ============================================================

elif st.session_state.page == "achievements":

    st.header("🏆 Conquistas")

    achievements = [
        ("🎯 Primeiro Acerto", "Acerte sua primeira questão."),
        ("🧠 10 Questões", "Acerte 10 questões."),
        ("🔥 Sequência de 5", "Acerte 5 questões seguidas."),
        ("🐍 Pythonista", "Complete a jornada Python."),
        ("🧩 Lógico", "Complete a jornada de Lógica."),
        ("🌐 Web Developer", "Complete HTML/CSS."),
        ("⚡ JavaScript", "Complete JavaScript."),
        ("👑 CodeMaster", "Alcance o nível 10.")
    ]

    for name, description in achievements:

        unlocked = name in st.session_state.achievements

        if unlocked:

            st.markdown(
                f"""
                <div class="card">
                    <h2>{name}</h2>
                    <p>{description}</p>
                    <strong>DESBLOQUEADA</strong>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="card" style="opacity:.45">
                    <h2>🔒 {name}</h2>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# PERFIL
# ============================================================

elif st.session_state.page == "profile":

    st.header("👤 Seu Perfil")

    st.markdown(
        f"""
        <div class="hero">

        <h1>👨‍💻 CodeMaster</h1>

        <p>Aprendiz de programação</p>

        <h2>⭐ Nível {calculate_level()}</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "XP",
            st.session_state.xp
        )

    with col2:
        st.metric(
            "Acertos",
            st.session_state.correct
        )

    with col3:
        st.metric(
            "Moedas",
            st.session_state.coins
        )

    st.subheader("📚 Progresso")

    for subject in QUESTIONS:

        p = progress(subject)

        st.write(f"**{subject}**")

        st.progress(p)

        st.caption(
            f"{int(p * 100)}% concluído"
        )

    st.subheader("🏆 Conquistas desbloqueadas")

    if st.session_state.achievements:

        for a in st.session_state.achievements:
            st.markdown(
                f'<span class="badge">{a}</span>',
                unsafe_allow_html=True
            )

    else:
        st.info(
            "Você ainda não desbloqueou nenhuma conquista."
        )