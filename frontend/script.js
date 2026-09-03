const API_URL = "http://127.0.0.1:8000";

let token = "";


/* =========================
   LOGIN
========================= */

async function login() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;


    const response = await fetch(
        `${API_URL}/auth/login`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })
        }
    );


    const data = await response.json();


    if (!response.ok) {

        document.getElementById(
            "loginMessage"
        ).textContent = data.detail || "Login failed";

        return;
    }


    token = data.access_token;


    document.getElementById(
        "loginMessage"
    ).textContent = "Login successful ✅";

}


/* =========================
   LOAD STUDENTS
========================= */

async function loadStudents() {

    if (!token) {

        document.getElementById(
            "students"
        ).textContent = "Please login first.";

        return;
    }


    const response = await fetch(
        `${API_URL}/students/`,
        {
            method: "GET",

            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    );


    const data = await response.json();


    if (!response.ok) {

        document.getElementById(
            "students"
        ).textContent = data.detail || "Failed to load students";

        return;
    }


    const studentsContainer =
        document.getElementById("students");


    studentsContainer.innerHTML = "";


    data.forEach(student => {

        const div =
            document.createElement("div");

        div.className = "student";


        div.innerHTML = `
            <strong>ID:</strong> ${student.id}<br>
            <strong>Name:</strong> ${student.name}<br>
            <strong>Department:</strong> ${student.department}<br>
            <strong>Year:</strong> ${student.year}
        `;


        studentsContainer.appendChild(div);

    });

}


/* =========================
   ADD STUDENT
========================= */

async function addStudent() {

    if (!token) {

        document.getElementById(
            "studentMessage"
        ).textContent = "Please login first.";

        return;
    }


    const name =
        document.getElementById("studentName").value;

    const department =
        document.getElementById("department").value;

    const year =
        Number(
            document.getElementById("year").value
        );


    const response = await fetch(
        `${API_URL}/students/`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },

            body: JSON.stringify({
                name: name,
                department: department,
                year: year
            })
        }
    );


    const data = await response.json();


    if (!response.ok) {

        document.getElementById(
            "studentMessage"
        ).textContent =
            data.detail || "Failed to add student";

        return;
    }


    document.getElementById(
        "studentMessage"
    ).textContent =
        "Student added successfully ✅";


    loadStudents();

}

/* =========================
   ASK AI
========================= */

async function askAI() {

    const question =
        document.getElementById("question").value.trim();

    const aiMessage =
        document.getElementById("aiMessage");

    const aiAnswer =
        document.getElementById("aiAnswer");


    if (!question) {

        aiMessage.textContent =
            "Please enter a question.";

        return;
    }


    aiMessage.textContent =
        "AI is thinking...";


    aiAnswer.textContent = "";


    try {

        const response = await fetch(
            `${API_URL}/rag/ask`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        const data = await response.json();


        if (!response.ok) {

            aiMessage.textContent =
                data.detail || "AI request failed.";

            return;
        }


        aiMessage.textContent =
            "AI response:";

        aiAnswer.textContent =
            data.answer;

    }

    catch (error) {

        aiMessage.textContent =
            "Could not connect to the AI service.";

    }
}