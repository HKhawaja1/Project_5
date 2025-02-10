document.addEventListener("DOMContentLoaded", function () {
    const questions = {
        Biology: [
            { question: "What is the powerhouse of the cell?", options: ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], answer: "C" },
            { question: "What is the process by which plants make their own food?", options: ["Respiration", "Photosynthesis", "Fermentation", "Digestion"], answer: "B" },
            { question: "Which part of the human brain controls coordination and balance?", options: ["Cerebrum", "Cerebellum", "Medulla", "Hypothalamus"], answer: "B" },
            { question: "What is the function of red blood cells in the human body?", options: ["Transport oxygen", "Fight infection", "Produce energy", "Regulate temperature"], answer: "A" },
            { question: "What is the largest organ in the human body?", options: ["Heart", "Liver", "Skin", "Lungs"], answer: "C" },
            { question: "Which gas do humans inhale during respiration?", options: ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], answer: "A" },
            { question: "What is the scientific term for the study of fungi?", options: ["Zoology", "Botany", "Mycology", "Ecology"], answer: "C" },
            { question: "What type of reproduction requires only one parent?", options: ["Sexual", "Asexual", "Binary fission", "Meiosis"], answer: "B" },
            { question: "What is the name of the pigment that gives plants their green color?", options: ["Carotene", "Chlorophyll", "Xanthophyll", "Melanin"], answer: "B" },
            { question: "What is the main function of the ribosome in a cell?", options: ["Energy production", "Protein synthesis", "Cell division", "DNA replication"], answer: "B" },
            { question: "Which human organ filters waste from the blood to form urine?", options: ["Liver", "Kidney", "Stomach", "Heart"], answer: "B" },
            { question: "What is the process of water movement through a semi-permeable membrane called?", options: ["Diffusion", "Osmosis", "Filtration", "Evaporation"], answer: "B" },
            { question: "What type of blood vessel carries blood away from the heart?", options: ["Veins", "Arteries", "Capillaries", "Lymphatic vessels"], answer: "B" },
            { question: "Which organ in the body produces insulin?", options: ["Liver", "Pancreas", "Stomach", "Kidney"], answer: "B" },
            { question: "What is the smallest unit of life?", options: ["Cell", "Atom", "Molecule", "Organism"], answer: "A" },
            { question: "What is the name of the male reproductive organ in a flower?", options: ["Stigma", "Anther", "Filament", "Ovule"], answer: "B" },
            { question: "Which part of the digestive system absorbs most of the nutrients?", options: ["Mouth", "Stomach", "Small intestine", "Large intestine"], answer: "C" },
            { question: "What is the main function of white blood cells?", options: ["Carry oxygen", "Fight infection", "Transport hormones", "Regulate temperature"], answer: "B" },
            { question: "What is the process by which organisms change over time through natural selection?", options: ["Evolution", "Mimicry", "Adaptation", "Mutation"], answer: "A" },
            { question: "What is the name of the protein that speeds up chemical reactions in the body?", options: ["Collagen", "Enzyme", "Hemoglobin", "Keratin"], answer: "B" }
        ],
        Chemistry: [
            { question: "What is the chemical symbol for gold?", options: ["Au", "Ag", "Hg", "Pb"], answer: "A" },
            { question: "Which element is found in all organic compounds?", options: ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"], answer: "B" },
            { question: "What is the pH of pure water?", options: ["1", "7", "14", "10"], answer: "B" },
            { question: "What type of bond is formed when two atoms share electrons?", options: ["Ionic", "Covalent", "Hydrogen", "Metallic"], answer: "B" },
            { question: "What is the chemical formula for table salt?", options: ["NaCl", "H2O", "CO2", "NaOH"], answer: "A" },
            { question: "Which gas is produced when an acid reacts with a metal?", options: ["Oxygen", "Nitrogen", "Hydrogen", "Carbon dioxide"], answer: "C" },
            { question: "What is the most abundant gas in Earth's atmosphere?", options: ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"], answer: "B" },
            { question: "What is the name of the process in which a solid turns directly into a gas?", options: ["Melting", "Condensation", "Sublimation", "Evaporation"], answer: "C" },
            { question: "What is the atomic number of oxygen?", options: ["6", "8", "10", "12"], answer: "B" },
            { question: "What type of reaction occurs when a fuel reacts with oxygen to produce heat and light?", options: ["Combustion", "Precipitation", "Neutralization", "Displacement"], answer: "A" },
            { question: "What is the name of the horizontal rows in the periodic table?", options: ["Groups", "Periods", "Columns", "Families"], answer: "B" },
            { question: "Which element is a liquid at room temperature?", options: ["Mercury", "Bromine", "Water", "Gallium"], answer: "A" },
            { question: "What is the main gas found in fizzy drinks?", options: ["Oxygen", "Carbon dioxide", "Nitrogen", "Helium"], answer: "B" },
            { question: "What is the term for a substance that speeds up a chemical reaction without being consumed?", options: ["Catalyst", "Solvent", "Reagent", "Buffer"], answer: "A" },
            { question: "What is the common name for dihydrogen monoxide?", options: ["Water", "Hydrogen peroxide", "Ammonia", "Methane"], answer: "A" },
            { question: "What is the hardest naturally occurring mineral?", options: ["Gold", "Diamond", "Iron", "Quartz"], answer: "B" },
            { question: "Which element is responsible for making bananas radioactive?", options: ["Potassium", "Carbon", "Radon", "Uranium"], answer: "A" },
            { question: "What is the chemical symbol for mercury?", options: ["Hg", "Mg", "Mn", "Mo"], answer: "A" },
            { question: "What is the process of breaking down a compound into its elements using electricity?", options: ["Electrolysis", "Reduction", "Oxidation", "Combustion"], answer: "A" },
            { question: "What is the name of the reaction when an acid and a base neutralize each other?", options: ["Displacement", "Neutralization", "Decomposition", "Synthesis"], answer: "B" }
        ],
        Physics: [
            { question: "What is the unit of force?", options: ["Watt", "Joule", "Newton", "Ohm"], answer: "C" },
            { question: "What is the acceleration due to gravity on Earth?", options: ["9.8 m/s²", "10 m/s²", "15 m/s²", "20 m/s²"], answer: "A" },
            { question: "What type of energy is stored in a stretched rubber band?", options: ["Kinetic", "Potential", "Chemical", "Thermal"], answer: "B" },
            { question: "What is the speed of light in a vacuum?", options: ["3 × 10^8 m/s", "2.99 × 10^8 m/s", "3.5 × 10^8 m/s", "2 × 10^8 m/s"], answer: "A" },
            { question: "What is Newton’s Third Law of Motion?", options: ["For every action, there is an equal and opposite reaction", "Force equals mass times acceleration", "An object in motion stays in motion", "Forces cause objects to move"], answer: "A" },
            { question: "What is the SI unit of power?", options: ["Joule", "Newton", "Watt", "Volt"], answer: "C" },
            { question: "What type of lens is used in a magnifying glass?", options: ["Convex", "Concave", "Planar", "Biconcave"], answer: "A" },
            { question: "What is the resistance of a conductor measured in?", options: ["Ohms", "Watts", "Joules", "Amperes"], answer: "A" },
            { question: "Which force keeps planets in orbit around the sun?", options: ["Electromagnetic", "Gravity", "Centrifugal", "Friction"], answer: "B" },
            { question: "What is the formula for kinetic energy?", options: ["E = mc²", "E = 1/2 mv²", "F = ma", "W = Fd"], answer: "B" },
            { question: "What happens to the frequency of a wave as its wavelength increases?", options: ["It increases", "It decreases", "It stays the same", "It depends on the amplitude"], answer: "B" },
            { question: "What is the name of the phenomenon when light bends as it passes from one medium to another?", options: ["Refraction", "Reflection", "Diffraction", "Absorption"], answer: "A" },
            { question: "Which subatomic particle has a negative charge?", options: ["Proton", "Neutron", "Electron", "Positron"], answer: "C" },
            { question: "What type of circuit has only one path for current to flow?", options: ["Series", "Parallel", "Open", "Closed"], answer: "A" },
            { question: "What is the SI unit of charge?", options: ["Coulomb", "Volt", "Ampere", "Tesla"], answer: "A" },
            { question: "What is the term for the bending of sound waves due to temperature differences in air?", options: ["Refraction", "Diffraction", "Doppler effect", "Echo"], answer: "A" },
            { question: "What is the name of the law that relates voltage, current, and resistance?", options: ["Ohm's Law", "Faraday's Law", "Coulomb's Law", "Kirchhoff's Law"], answer: "A" },
            { question: "What is the name of the force that opposes motion between two surfaces?", options: ["Friction", "Gravity", "Tension", "Normal force"], answer: "A" },
            { question: "What is the unit of frequency?", options: ["Hertz", "Ampere", "Volt", "Newton"], answer: "A" },
            { question: "What is the name for the energy stored in an object due to its height above the ground?", options: ["Kinetic energy", "Thermal energy", "Gravitational potential energy", "Elastic potential energy"], answer: "C" }
        ]
    };

    let currentQuestionIndex = 0;
    let selectedTopic = "Biology";
    let userLoggedIn = JSON.parse(document.getElementById("user-status").textContent); // Check if user is logged in

    const topicSelect = document.getElementById("quiz-topic");
    const categoryText = document.getElementById("question-category");
    const questionText = document.getElementById("quiz-question");
    const form = document.getElementById("quiz-form");
    const startButton = document.getElementById("start-quiz");
    const nextButton = document.getElementById("next-question");

    if (!userLoggedIn) {
        topicSelect?.remove();  // Hide topic selection if not logged in
    }

    topicSelect?.addEventListener("change", function () {
        selectedTopic = topicSelect.value;
        categoryText.innerText = selectedTopic;
    });

    function loadQuestion(index) {
        let availableQuestions = questions[selectedTopic];

        // Restrict non-logged-in users to the first 10 Biology questions
        if (!userLoggedIn && selectedTopic === "Biology") {
            availableQuestions = questions.Biology.slice(0, 10);
        }

        if (index >= availableQuestions.length) {
            questionText.innerText = "You have completed the quiz! Great job!";
            form.innerHTML = "";
            nextButton.style.display = "none";
            return;
        }

        const question = availableQuestions[index];
        questionText.innerText = question.question;
        form.innerHTML = "";

        question.options.forEach((option, i) => {
            const radioDiv = document.createElement("div");
            radioDiv.classList.add("radio");

            const label = document.createElement("label");
            label.innerHTML = `<input type="radio" name="answer" value="${String.fromCharCode(65 + i)}"> ${option}`;

            radioDiv.appendChild(label);
            form.appendChild(radioDiv);
        });

        form.appendChild(nextButton);
        nextButton.style.display = "block";
    }

    startButton.addEventListener("click", () => {
        currentQuestionIndex = 0;
        loadQuestion(currentQuestionIndex);
        startButton.style.display = "none";
    });

    nextButton.addEventListener("click", () => {
        currentQuestionIndex++;
        loadQuestion(currentQuestionIndex);
    });
});
