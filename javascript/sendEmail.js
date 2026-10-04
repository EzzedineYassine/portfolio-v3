const sendBtn = document.getElementById('sendButton');
const form = document.getElementById('sendForm');
const nameField = document.getElementById('name');
const emailField = document.getElementById('email');
const messageField = document.getElementById('message');
const formInfo = document.getElementById('form__info');
const formPopupTxt = document.getElementById('form__popup-txt');

if (form) {
  form.addEventListener('submit', sendEmail);
}

async function sendEmail(e) {
  e.preventDefault();
  formInfo.classList.add('hide');
  const originalBtnValue = sendBtn.value;
  sendBtn.value = 'Sending...';

  const endpoint = 'https://formspree.io/f/xzebklwk';

  try {
    const formData = new FormData(form);
    const response = await fetch(endpoint, {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json'
      }
    });

    if (response.ok) {
      sendBtn.value = originalBtnValue;
      nameField.value = '';
      emailField.value = '';
      messageField.value = '';
      formInfo.style.backgroundColor = 'rgb(0 113 12)';
      formPopupTxt.textContent = 'Email was successfully sent!';
      formInfo.classList.remove('hide');
    } else {
      throw new Error('Formspree response error');
    }
  } catch (err) {
    sendBtn.value = originalBtnValue;
    formInfo.style.backgroundColor = '#8b1a09';
    formPopupTxt.textContent = 'Error sending email! Try again!';
    formInfo.classList.remove('hide');
  }
}

export { sendEmail };
