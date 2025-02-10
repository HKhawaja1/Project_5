document.addEventListener("DOMContentLoaded", function () {
    const questions = [
        { question: "What is the powerhouse of the cell?", options: ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], answer: "C" },
        { question: "What is the process by which plants make their own food?", options: ["Respiration", "Photosynthesis", "Fermentation", "Digestion"], answer: "B" },
        { question: "Which part of the human brain controls coordination and balance?", options: ["Cerebrum", "Cerebellum", "Medulla", "Hypothalamus"], answer: "B" },
        { question: "What is the function of red blood cells in the human body?", options: ["Transport oxygen", "Fight infection", "Produce energy", "Regulate temperature"], answer: "A" },
        { question: "What is the largest organ in the human body?", options: ["Heart", "Liver", "Skin", "Lungs"], answer: "C" },
        { question: "Which gas do humans inhale during respiration?", options: ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], answer: "A" },
        { question: "What is the scientific term for the study of fungi?", options: ["Zoology", "Botany", "Mycology", "Ecology"], answer: "C" },
        { question: "What type of reproduction requires only one parent?", options: ["Sexual", "Asexual", "Binary fission", "Meiosis"], answer: "B" },
        { question: "What is the name of the pigment that gives plants their green color?", options: ["Carotene", "Chlorophyll", "Xanthophyll", "Melanin"], answer: "B" },
        { question: "What is the main function of the ribosome in a cell?", options: ["Energy production", "Protein synthesis", "Cell division", "DNA replication"], answer: "B" }
    ];

    let currentQuestionIndex = 0;
    let quizCompleted = false; // Flag to track quiz completion

    // Get elements from HTML
    const questionText = document.getElementById("quiz-question");
    const form = document.getElementById("quiz-form");
    const nextButton = document.getElementById("next-question");

    // Ensure elements exist before running the script
    if (!questionText || !form || !nextButton) {
        console.error("Quiz elements not found. Check your HTML structure.");
        return;
    }

    function loadQuestion(index) {
        const question = questions[index];
        questionText.innerText = question.question;

        // Clear previous options
        form.innerHTML = "";

        // Generate new radio buttons
        question.options.forEach((option, i) => {
            const radioDiv = document.createElement("div");
            radioDiv.classList.add("radio");

            const label = document.createElement("label");
            label.innerHTML = `<input type="radio" name="answer" value="${String.fromCharCode(65 + i)}"> ${option}`;

            radioDiv.appendChild(label);
            form.appendChild(radioDiv);
        });

        // Append Next Button
        form.appendChild(nextButton);
        nextButton.innerText = "Next Question"; // Reset button text
        nextButton.classList.remove("btn-login"); // Ensure it is not styled as the login button
        quizCompleted = false; // Reset flag
    }

    nextButton.addEventListener("click", () => {
        if (quizCompleted) {
            // Redirect directly to login page when quiz is completed
            window.location.href = "/login";
            return;
        }

        // Check if an answer was selected
        const selectedAnswer = form.querySelector("input[name='answer']:checked");
        if (!selectedAnswer) {
            alert("Please select an answer before proceeding.");
            return;
        }

        // Move to the next question
        currentQuestionIndex++;

        if (currentQuestionIndex < questions.length) {
            loadQuestion(currentQuestionIndex);
        } else {
            // Quiz completed - Change button to "Login"
            questionText.innerText = "You have completed the quiz! Log in to view all questions and track your progress.";
            questionText.style.fontWeight = "bold"; // Make message bold
            questionText.style.color = "#2D3E51"; // Ensure visibility

            form.innerHTML = ""; // Clear form options

            nextButton.innerText = "Login";
            nextButton.classList.add("btn-login");
            quizCompleted = true; // Set quiz completion flag

            form.appendChild(nextButton);
        }
    });

    // Load the first question on page load
    loadQuestion(currentQuestionIndex);
});
