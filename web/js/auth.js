if (localStorage.rememberLogin)
  loginInp.value = localStorage.rememberLogin

if (localStorage.rememberPass)
  passInp.value = localStorage.rememberPass

authBtn.onclick = async () => {
  const login = loginInp.value
  const pass = passInp.value
  const remember = rememberMeInp.checked

  if (remember) {
    localStorage.rememberLogin = login
    localStorage.rememberPass = pass
  }

  const auth = eel.check_user({ login, pass })
  const data = await auth()

  if (data.success) {
    sessionStorage.token = data.token
    location.href = "todos.html"
  } else {
    alert(data.msg)
  }
}