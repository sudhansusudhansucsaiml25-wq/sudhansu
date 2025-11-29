const questions = [
    {
        question: "Which HTML tag creates the largest heading?",
        options: ["<h6>", "<h1>", "<title>", "<header>"],
        answer: 1
    },
    {
        question: "CSS stands for?",
        options: ["Creative Style Sheets", "Cascading Style Sheets", "Computer Styled System", "Color Sheet Syntax"],
        answer: 1
    },
    {
        question: "Which CSS property changes text color?",
        options: ["font-color", "text-color", "color", "fgcolor"],
        answer: 2
    },
    {
        question: "Which HTML tag inserts an image?",
        options: ["<img>", "<image>", "<pic>", "<src>"],
        answer: 0
    },
    {
        question: "JavaScript is placed inside which HTML tag?",
        options: ["<script>", "<javascript>", "<code>", "<js>"],
        answer: 0
    },
    {
        question: "Which property changes background color?",
        options: ["bgcolor", "background", "background-color", "color-bg"],
        answer: 2
    },
    {
        question: "HTML stands for?",
        options: [
            "HyperText Markup Language",
            "HighText Machine Language",
            "Home Tool Marking Language",
            "Hyperlinks Markup List"
        ],
        answer: 0
    },
    {
        question: "Which is used for a single-line JS comment?",
        options: ["<!-- -->", "//", "##", "??"],
        answer: 1
    },
    {
        question: "Which tag makes text bold?",
        options: ["<strong>", "<b>", "<bold>", "<important>"],
        answer: 1
    },
    {
        question: "Which symbol represents ID in CSS?",
        options: [".", "#", "@", "$"],
        answer: 1
    },
    {
        question: "Which tag is used for list item?",
        options: ["<li>", "<item>", "<list>", "<ul>"],
        answer: 0
    },
    {
        question: "JavaScript arrays use?",
        options: ["{}", "()", "[]", "<>"],
        answer: 2
    },
    {
        question: "Which event occurs when clicking a button?",
        options: ["onpress", "onclick", "onhover", "onstart"],
        answer: 1
    },
    {
        question: "Which HTML attribute applies inline CSS?",
        options: ["style", "class", "css", "font"],
        answer: 0
    },
    {
        question: "Which tag creates a table row?",
        options: ["<tr>", "<td>", "<row>", "<table>"],
        answer: 0
    }
];

// -------------------------------------------
// VARIABLES
// -------------------------------------------
let index = 0;
let score = 0;

const mainBox = document.querySelector(".main-box");
const startBtn = document.querySelector(".start-btn");

startBtn.addEventListener("click", startTest);

// -------------------------------------------
// START TEST
// -------------------------------------------
function startTest() {
    mainBox.innerHTML = `
        <div id="question-box" style="background:#f0f6ff; padding:20px; border-radius:10px;"></div>
        <button id="next-btn" class="start-btn" style="margin-top:20px;">Next</button>
    `;

    loadQuestion();

    document.getElementById("next-btn").onclick = nextQuestion;
}

// -------------------------------------------
// LOAD QUESTION
// -------------------------------------------
function loadQuestion() {
    const q = questions[index];

    document.getElementById("question-box").innerHTML = `
        <h2 style="color:#1e3a8a;">${index + 1}. ${q.question}</h2>
        ${q.options
            .map(
                (opt, i) =>
                    `<label style="display:block; margin:10px; font-size:18px;">
                        <input type="radio" name="option" value="${i}">
                        ${opt}
                    </label>`
            )
            .join("")}
    `;
}

// -------------------------------------------
// NEXT QUESTION
// -------------------------------------------
function nextQuestion() {
    const selected = document.querySelector('input[name="option"]:checked');
    if (!selected) {
        alert("Please select an option!");
        return;
    }

    if (parseInt(selected.value) === questions[index].answer) {
        score++;
    }

    index++;

    if (index < questions.length) {
        loadQuestion();
    } else {
        showResult();
    }
}

// -------------------------------------------
// SHOW RESULT
// -------------------------------------------
function showResult() {
    mainBox.innerHTML = `
        <div style="background:#f0f6ff; padding:20px; border-radius:10px;">
            <h2 style="color:#1e3a8a;">Quiz Completed!</h2>
            <p style="font-size:20px;">Your Score: ${score} / ${questions.length}</p>
            <button class="start-btn" onclick="restartQuiz()">Restart</button>
        </div>
    `;
}

// -------------------------------------------
// RESTART QUIZ
// -------------------------------------------
function restartQuiz() {
    index = 0;
    score = 0;
    startTest();
}