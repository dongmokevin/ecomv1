const messageForm = document.getElementById('message-form')
console.log(messageForm)
const body = document.getElementById('id_body')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const alertBox = document.getElementById('alert-box')

const handleAlert = (type, text) => {
  alertBox.innerHTML = `<div class='alert alert-${type}' role='alert'>
                          ${text}
                        </div>`
}
messageForm.addEventListener('submit', e=>{
  e.preventDefault()

  $.ajax({
    type: 'POST',
    url: messageForm.action,
    data: {
      'csrfmiddlewaretoken': csrf[0].value,
      'body': body.value,
    },
    success: function(response){
      console.log(response);
      const msg =`We've send a message: ${response.body}`
      handleAlert('success', msg)
      MessageForm.reset()
    },
    error: function(error){
      console.log(error);
      handleAlert('danger', 'something went wrong')
    }
  })
})
console.log(body);
