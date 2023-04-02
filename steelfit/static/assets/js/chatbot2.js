// chatbot.js
const form = document.getElementById("input-form");
const inputField = document.getElementById("input-field");
const conversation = document.getElementById("conversation");
var hi_done = "false"

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const user_input = inputField.value.trim();
  inputField.value = "";

  // Clear input field
  inputField.value = '';
  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: "2-digit" });

  // Add user input to conversation
  let message = document.createElement('div');
  message.classList.add('chatbot-message', 'user-message');
  message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${user_input}</p>`;
  conversation.appendChild(message);

  if (user_input) {
    // Send an AJAX request to the chatbot_response URL
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        const response = JSON.parse(xhr.responseText).response; // extract the response from the JSON object
        hi_done = JSON.parse(xhr.responseText).hi_done;
        // Add the chatbot's response to the conversation
        const chatbotMessage = document.createElement("div");
        chatbotMessage.classList.add("chatbot-message");
        const chatbotText = document.createElement("p");
        chatbotText.classList.add("chatbot-text");
        chatbotText.textContent = response;
        chatbotMessage.appendChild(chatbotText);
        conversation.appendChild(chatbotMessage);
      }
    };

    xhr.open("GET", "/chatbot-response/?user_input=" + user_input + "&hi_done=" + hi_done);
    xhr.send();
  }
});




