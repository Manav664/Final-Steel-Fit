const form = document.getElementById("input-form");
const inputField = document.getElementById("input-field");
const conversation = document.getElementById("conversation");
var hi_done = "false"
var specifications = "false"
var name_enterd = "false"
var user_name = ""
var company_enterd = "false"
var user_company = ""
var phone_enterd = "false"
var user_phone = ""
var product_enterd = "false"
var user_product = ""
var specification_enterd = "false"
var user_specification = ""

function scrollConversationToBottom() {
  const conversation = document.getElementById("conversation");
  conversation.scrollTop = conversation.scrollHeight;
}

function createButton(textContent) {
  console.log("Button creation is being called");
  
  const button = document.createElement("button");
  button.id = "my-button";
  button.style.padding = "10px 20px";
  button.style.border = "none";
  button.style.borderRadius = "5px";
  button.style.background = "#4CAF50";
  button.style.color = "white";
  button.style.fontWeight = "bold";
  button.textContent = textContent;
  button.addEventListener("click", function() {
    user_product = textContent;
    product_enterd = "true";
    const chatbotMessage = document.createElement("div");
    chatbotMessage.classList.add("chatbot-message");
    const chatbotText = document.createElement("p");
    chatbotText.classList.add("chatbot-text");
    chatbotText.textContent = "Is " + user_product + " is your product type?";
    chatbotMessage.appendChild(chatbotText);
    conversation.appendChild(chatbotMessage);
    scrollConversationToBottom();
  });

  const buttonContainer = document.createElement("div");
  buttonContainer.classList.add("chatbot-message");
  buttonContainer.style.paddingBottom = "20px";
  buttonContainer.appendChild(button);
  
  conversation.appendChild(buttonContainer);
}

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

  scrollConversationToBottom();

  if (user_input) {
    // Send an AJAX request to the chatbot_response URL
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        const response = JSON.parse(xhr.responseText).response; // extract the response from the JSON object
        hi_done = JSON.parse(xhr.responseText).hi_done;
        specifications = JSON.parse(xhr.responseText).specifications;
        name_enterd = JSON.parse(xhr.responseText).name_enterd;
        user_name = JSON.parse(xhr.responseText).user_name;
        company_enterd = JSON.parse(xhr.responseText).company_enterd;
        user_company = JSON.parse(xhr.responseText).user_company;
        phone_enterd = JSON.parse(xhr.responseText).phone_enterd;
        user_phone = JSON.parse(xhr.responseText).user_phone;
        product_enterd = JSON.parse(xhr.responseText).product_enterd;
        user_product = JSON.parse(xhr.responseText).user_product;
        specification_enterd = JSON.parse(xhr.responseText).specification_enterd;
        user_specification = JSON.parse(xhr.responseText).user_specification;

        // Add the chatbot's response to the conversation
        for (let i = 0; i < response.length; i++) {
        
        const chatbotMessage = document.createElement("div");
        chatbotMessage.classList.add("chatbot-message");
        const chatbotText = document.createElement("p");
        chatbotText.classList.add("chatbot-text");
        chatbotText.textContent = response[i];
        chatbotMessage.appendChild(chatbotText);
        conversation.appendChild(chatbotMessage);
        }
        scrollConversationToBottom();

        if (phone_enterd == "true" && product_enterd=="false")

        {
          let products = ["item1", "item2", "item3","item4","others"];
          for (let i = 0; i < products.length; i++)
          {
            createButton(products[i]);
            scrollConversationToBottom();
          }
        
      }
      }
      scrollConversationToBottom();
    };

    xhr.open("GET", "/chatbot-response/?user_input=" + user_input + "&hi_done=" + hi_done + "&specifications=" + specifications + "&name_enterd=" + name_enterd + "&user_name=" + user_name + "&company_enterd=" + company_enterd + "&user_company=" + user_company + "&phone_enterd=" + phone_enterd + "&user_phone=" + user_phone + "&product_enterd=" + product_enterd + "&user_product=" + user_product + "&specification_enterd=" + specification_enterd + "&user_specification=" + user_specification);
    xhr.send();
  }
});




