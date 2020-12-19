addEventListener("load", async () => {
  const getTodos = eel.get_todos(sessionStorage.token)
  const result = await getTodos()

  if (result && result.todos) {
    const html = result.todos.map(buildTodo).join("")
    todoList.innerHTML = html
  } else {
    todoList.innerHTML = `<li>Здесь пусто...</li>`
  }

  function buildTodo(todo) {
    return `<li>${todo.text}</li>`
  }
})

addBtn.onclick = async () => {
  const text = prompt("Введите текст задачи")
  const query = eel.add_todo(sessionStorage.token, text)
  const result = await query()

  if (result.success) {
    location.reload()
  }
}