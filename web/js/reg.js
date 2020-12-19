if (localStorage.rememberLogin)
  loginInp.value = localStorage.rememberLogin

if (localStorage.rememberPass)
  passInp.value = localStorage.rememberPass

regBtn.onclick = async () => {
  const login = loginInp.value
  const pass = passInp.value
  const remember = rememberMeInp.checked
  let err

  if (login.length < 2)
    err = "Логин должен содержать не менее 2 символов"
  else if (pass.length < 8)
    err = "Пароль должен содержать не менее 8 символов"

  if (err)
    return alert(err)

  if (remember) {
    localStorage.rememberLogin = login
    localStorage.rememberPass = pass
  }

  const reg = eel.reg_user({ login, pass })
  const data = await reg()

  if (data == "success") {
    sessionStorage.login = login
    location.href = "/todos"
  } else {
    alert(data)
  }
}